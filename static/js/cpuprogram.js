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
