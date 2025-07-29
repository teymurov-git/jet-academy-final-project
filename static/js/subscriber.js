let subscriptionForm = document.getElementById('subscription-form');

subscriptionForm.addEventListener('submit', function(event){
    event.preventDefault();

    let email = document.getElementById('email').value;
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('http://127.0.0.1:8000/api/subscriber/', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body: JSON.stringify({'email' : email})
    }).then(response => {
        if (response.ok){
            subscriptionForm.innerHTML = `<h2>Thanks for your subscription!</h2>`;
        } else {
            alert('Error');
        }
    });
});