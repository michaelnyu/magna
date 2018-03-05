Panda.init('pk_test_2C04UlQCKet4YoLtQVNkNQ', 'panda_cc_form');
var panda_token;

Panda.on('success', function(cardToken) {
  console.log(cardToken);
  panda_token = cardToken;
});

Panda.on('error', function(errors) {
  console.log(errors.message)
});

async function donationCreate(){
  const email = document.querySelector('#email').value;
  let donation = Number(document.querySelector('#amount').value) * 100;

  let test_payload = {
    "source": panda_token,
    "amount": String(donation),
    "destination": "73-1710135",
    "receipt_email": email,
    "currency": "usd",
  }
  console.log(test_payload);

  try {
    const response = await fetch("https://api.pandapay.io/v1/donations/", {
      type: 'POST',
      headers: {
        'Content-Type': "application/json",
        'Authorization': 'Basic ' + btoa('PLACE TEST KEY HERE'),
      },
      data: JSON.stringify(test_payload),
    });
    const status = await response.status;
    if (status >= 200 && status < 300) {
      const json = await response.json();
      console.log(json);
    }else{
      throw new Error(status);
    }
  }catch(e){
    throw new Error(e.message);
  }
}
var submit_button = document.querySelector('#donate');
submit_button.addEventListener('click', ()=>{ donationCreate() });



/* POST USER ENTRY */

const apibase = "http://159.203.117.240/api/"
// const apibase = "http://localhost:8000/api/";

async function sendData(){
  const name = document.querySelector('#name').value;
  const text = document.querySelector('#text').value;
  const donation = Number(document.querySelector('#donation').value);

  const characterJSON = {
    "head": ";laskjdfl;", 
    "penis": "laksjdf",
  }


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
        "votes": 0,
        "character": characterJSON
      })
    });
    const status = await response.status;
    if (status >= 200 && status < 300) {
      console.log("success", status);
    }else{
      throw new Error(status);
    }

  }catch(e){
    throw new Error(e.message);
  }
}


var submit_button = document.querySelector('#post-entry');
submit_button.addEventListener('click', ()=>{ sendData() });  
