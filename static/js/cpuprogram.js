var id = 0 // Var id keeps track of the id of the user. It's default is 0 but there is no id 0.
document.addEventListener('submit', (e) => { //Function that when the form is submitted, it overrides the HTML form function, to be able to process the request.
    // Store reference to form to make later code easier to read
    const form = e.target;
    var response = ""
    fetch(form.action, {
	method: form.method,
	body: new FormData(form),
    })
	.then(response => {
	   // console.log(response.ok);
	    
	    if (response.ok){ //If response was successful, it provides a success message.
		document.getElementById("input-form").reset();
		document.getElementById("success").hidden = false;
		document.getElementById("failure").hidden = true;
		setTimeout(() => {document.getElementById("success").hidden = true;}, 2000);
		
	    } else { // If request was not successful, a failure message is provided.
		document.getElementById("failure").hidden = false;
		document.getElementById("success").hidden = true;
		setTimeout(() => {document.getElementById("failure").hidden = true;}, 2000);
	    }
	    return response.json()
	    
	})
	.then(data => { //Get id and position in queue from request.
	    id = data.id;
	    document.getElementById("position-label").innerHTML = `Your position in queue: ${data.position}`;
	})
    /*
    console.log(response);
    if (response == "200") {
	    document.getElementById("input-form").reset();
	}
  */  

    // Prevent the default form submit
    e.preventDefault();
});
function update_cp() { //Function that fetches the current program and updates the table. It also updates the user's position in queue
    fetch("./api/current-program")
	.then(response => response.json())
	.then(data => {
	    let rows = document.getElementsByClassName("cp_table_td")
	    
	    for (let i = 0; i < rows.length; i++) {
		rows[i].innerHTML = "";
	    }
	    document.getElementById("cp0in").innerHTML = "None"
	    if (data != "No programs"){ //Only add current program if programs are present.
		let program = data.program;
		for (let ind = 0; ind < program.length; ind++) { //Iterate over every instruction and add it to current program table.
		    let instruct = program[ind];
		    let address = instruct.address;
		    let ad = "cp" + address + "ad";
		    let inst = "cp" + address + "in";
		    let val = "cp" + address + "val";
		    document.getElementById(ad).innerHTML = instruct.address;
		    document.getElementById(inst).innerHTML = instruct.instruct;
		    document.getElementById(val).innerHTML = instruct.value;
		}
	    }
	    
	})
    fetch(`./api/position?id=${id}`) //Fetch that takes the user's ID and gets their position in queue.
	.then(response => response.json())
	.then(data => {
	    if (data != "Id isn't present") {
		document.getElementById("position-label").innerHTML = `Your position in queue: ${data}`
	    } else {
		document.getElementById("position-label").innerHTML = "Your position in queue: N/A"	
	    }
	})
}
var intervalId = window.setInterval(function(){ //Line that will call update_cp() every 5000 milliseconds.
    update_cp()
}, 5000);

let allowed_programs = ["NOP", "LDA", "ADD", "SUB", "STA", "LDI", "JMP", "JC", "JZ", "JC ", "JZ ", "OUT", "HLT"] //List of programs use to reference user input against.

function program_input_check(name) { //Function that checks the users input across the list of programs to make sure it is valid.
    let value = document.getElementsByName(name)[0].value
    let okay = false;
    for (i=0;i < allowed_programs.length; i++) {
	program = allowed_programs[i]
	
	if (program.startsWith(value)) {
	    okay = true
	} 
    }
    if (okay) {
	document.getElementById("invalid").hidden = true
    } else {
	document.getElementById("invalid").hidden = false
    }
    allowSubmission()
}

let allowed_values = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"] //List of values that are allowed.

function value_input_check(name) { //Function that checks the users input across the list of values to make sure it is valid
    let value = document.getElementsByName(name)[0].value
    let okay = false;
    for (i=0;i < allowed_values.length; i++) {
	a_value = allowed_values[i]
	
	if (a_value.startsWith(value)) {
	    okay = true
	} 
    }
    if (okay) {
	document.getElementById("invalid").hidden = true
    } else {
	document.getElementById("invalid").hidden = false
    }
    allowSubmission()
}
function isHidden(item) { //Function to see if see if a item is hidden or not.
    
    if (window.getComputedStyle(item).display === "none") {
	return true
    } else {
	return false
    }
}

function allowSubmission() { //Function that disables submission of programs if there are errors present.
    let message = document.getElementById('invalid')
    if (!isHidden(message)) {
	document.getElementById('submitButton').disabled = true;
    } else {
	document.getElementById('submitButton').disabled = false;
    }
}
