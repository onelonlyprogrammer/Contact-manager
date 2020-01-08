var str, output;
function init() {
    str = document.getElementById("query").value;
    output = document.getElementById("output");
}
//Takes name of contact and returns contents if found
function find() {
    init();
    output.innerHTML = "";
    eel.findContact(str)(function(ret) {
        for (var i = 0; i < ret.length; i++) {
            output.innerHTML += `${ret[i]} <hr>`;
        }
    });
}
//Takes name of contact and if found removes contact
function remove() {
    init();
    args = str.split(", ");
    eel.deleteContact(str)(function(ret) {
    	output.innerHTML = ret;
    });
}
//Takes four arguments and sends them to addContact
function add() {
    init();
    args = str.split(", ");
    if (args.length == 4) {
    	eel.addContact(args[0], args[1], args[2], args[3])(function(ret) {
            console.log("running")
   	    output.innerHTML = "Added " + args[0];
    	});
    }
    else {
    	output.innerHTML = "Invalid input. Input 4 items. Example (John Doe, (123)-456-7890, johndoe@email.com, 123 Some Street)";
    }
}
