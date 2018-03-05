// var apibase = "http://159.203.117.240/api/v1/"
const apibase = "http://localhost:8000/api/v1/"

async function sendData(){
	var name = document.querySelector('#name').value;
	var text = document.querySelector('#text').value;
	var donation = Number(document.querySelector('#donation').value);

	try {
		const response = await fetch(apibase+"entries/", {
			method: 'POST',
			headers: {
				'Content-Type': "application/json",
			},
			body: JSON.stringify({
				"name": name,
				"text": text,
				"donation": donation,
			})
		});
		const status = await response.status;
		if (status >= 200 && status < 300) {
			console.log("success");
		}else{
			throw new Error(status);
		}

	}catch(e){
		throw new Error(e.message);
	}
}


var submit_button = document.querySelector('#submit');
submit_button.addEventListener('click', ()=>{ sendData() });	
