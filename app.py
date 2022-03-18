from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

conn = MongoClient('localhost',27017)
db = conn.todos
coll_todo = db.todo

@app.route('/')
def index():
    todos = coll_todo.find()
    return render_template('base.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    new_todo = request.form.get('new-todo')

    coll_todo.insert_one(
        {'text' : new_todo,
        'complete' : False}
    )

    return redirect(url_for('index'))

@app.route('/update/<id>/<newtext>')
def update_todo(id, newtext):
    
    new_text = newtext

    coll_todo.update_one(
        {"_id": ObjectId(str(id))},
        {"$set": {"text": new_text}}
    )

    return redirect(url_for('index'))

@app.route('/update-status/<id>/<complete>')
def update_complete(id,complete):

    if complete.lower() == "true":
        coll_todo.update_one(
        {"_id": ObjectId(str(id))},
        {"$set": {"complete": False}}
    )
    else:
        coll_todo.update_one(
        {"_id": ObjectId(str(id))},
        {"$set": {"complete": True}}
    )
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete_todo(id):

    coll_todo.delete_one(
        {"_id": ObjectId(str(id))}
    )

    return redirect(url_for('index'))

@app.route('/delete-all')
def delete_all():
    coll_todo.delete_many({})
    return redirect(url_for('index'))

@app.route('/sortcomplete')
def sortcomplete():
    todos = coll_todo.find().sort("complete", 1)
    return render_template('base.html', todos=todos)


@app.route('/search', methods=['POST'])
def search():
    keywords = request.form.get('keyword')

    myquery = { "text": {"$gt": keywords} }
    todos = coll_todo.find(myquery)
    
    query = {
    "text": {
    "$regex": keywords,
    }
    }

    todos = coll_todo.find(query)

    return render_template('base.html', todos=todos)
