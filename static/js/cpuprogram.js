var id = 0
document.addEventListener('submit', (e) => {
    // Store reference to form to make later code easier to read
    const form = e.target;
    var response = ""
    fetch(form.action, {
	method: form.method,
	body: new FormData(form),
    })
	.then(response => {
	   // console.log(response.ok);
	    
	    if (response.ok){
		document.getElementById("input-form").reset();
		document.getElementById("success").hidden = false;
		document.getElementById("failure").hidden = true;
		setTimeout(() => {document.getElementById("success").hidden = true;}, 2000);
		
	    } else {
		document.getElementById("failure").hidden = false;
		document.getElementById("success").hidden = true;
		setTimeout(() => {document.getElementById("failure").hidden = true;}, 2000);
	    }
	    return response.json()
	    
	})
	.then(data => {
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
function update_cp() {
    fetch("./api/current-program")
	.then(response => response.json())
	.then(data => {
	    let rows = document.getElementsByClassName("cp_table_td")
	    
	    for (let i = 0; i < rows.length; i++) {
		rows[i].innerHTML = "";
	    }
	    document.getElementById("cp0in").innerHTML = "None"
	    if (data != "No programs"){
		let program = data.program;
		for (let ind = 0; ind < program.length; ind++) {
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
    fetch(`./api/position?id=${id}`)
	.then(response => response.json())
	.then(data => {
	    if (data != "Id isn't present") {

		document.getElementById("position-label").innerHTML = `Your position in queue: ${data}`
	    } else {
		document.getElementById("position-label").innerHTML = "Your position in queue: N/A"	
	    }
	})
}
var intervalId = window.setInterval(function(){
    update_cp()
}, 5000);
