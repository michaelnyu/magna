Panda.init('pk_test_2C04UlQCKet4YoLtQVNkNQ', 'panda_cc_form');
var panda_token;


Panda.on('success', function(cardToken) {
  // You now have a token you can use to refer to that credit card later.
  // This token is used in PandaPay API calls for creating donations and grants
  // so that you don't have to worry about security concerns with dealing with
  // credit card data.
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
    // "receipt_email": email,
    "currency": "usd",
  }
  console.log(test_payload);

  try {
    const response = await fetch("https://api.pandapay.io/v1/donations/", {
      type: 'POST',
      // credentials: 'include',
      headers: {
        'Content-Type': "application/json",
        'Authorization': 'Basic ' + btoa('PLACE TEST KEY HERE'),

        // 'X-Auth-Token': 'sk_test_ehg1TY6M9ACY8k13VKgyAw',     
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
