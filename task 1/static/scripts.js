document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        predict();
    });
});

async function predict() {
    const textInput = document.getElementById('textInput').value;

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ 'textInput': textInput }),
    });

    const result = await response.json();
    displayPrediction(result.prediction);
}

function displayPrediction(prediction) {
    const predictionResultElement = document.getElementById('predictionResult');
    predictionResultElement.innerText = `Predicted Target Labels: ${prediction}`;
}
