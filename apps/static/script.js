// Create weather with all details
document.getElementById('weather-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const city = document.getElementById('city').value;
    const date = document.getElementById('date').value;
    const temperature = parseFloat(document.getElementById('temp').value);
    const description = document.getElementById('desc').value;
    
    const response = await fetch('/weather', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ city, date, temperature, description })
    });
    
    const result = await response.json();
    document.getElementById('weather-result').innerText = result.message;
});

//Create weather with city
document.getElementById('weather-form2').addEventListener('submit', async function(event) {
    event.preventDefault();
    const city = document.getElementById('autoCity').value;

    const response = await fetch('/open_weather', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ city })
    });

    const result = await response.json();
    document.getElementById('weather-result').innerText = result.message;
});


// Retrieve weather data
weatherId = document.getElementById('weather-form3')
weatherId.addEventListener('submit', function(e) {
    e.preventDefault();
    const city = document.getElementById('retCity').value;
    fetch(`/weather/${city}`).then(response => response.json()).then(data => {
        if(data.message){
            document.getElementById('weather-result').innerText = data.message; 
        }else{
            const result = `
                <h2>Weather in ${data[0].city}</h2>
                <p>Date: ${data[0].date}</p>
                <p>Temperature: ${data[0].temperature} deg C</p>
                <p>Description: ${data[0].description}</p>
            `;
            document.getElementById('weather-result').innerHTML = result;
        }
    }).catch(error => {document.getElementById('weather-result').innerText = 'Error with data retrieval';})
});
