function toggleEnable(elem) {
    document.getElementById(elem).disabled = false;
    document.getElementById(elem).focus();
}

function handleEnter(e,itemid,elem){

    if(e.keyCode == 13){
        e.preventDefault(); // Ensure it is only this code that runs

        let newtext = document.getElementById(elem).value;

        if (confirm("Update your todo list?") == true) 
        {
            let updatepage = "http://127.0.0.1:5000/update/" + itemid + "/" + newtext;
            window.location.href = updatepage;
        } 
        else 
        {
            window.location.href = "http://127.0.0.1:5000";
        }
    }
}

function deleteAllConfirm(){
    if (confirm("Are you confirm to delete everything in todo list?") == true) 
    {
        let deleteallpage = "http://127.0.0.1:5000/delete-all";
         window.location.href = deleteallpage;
    } 
    else 
    {
        window.location.href = "http://127.0.0.1:5000";
    }
}