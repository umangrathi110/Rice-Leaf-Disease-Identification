function predict() {
    var formData = new FormData();
    var file = document.getElementById('file').files[0];
    formData.append('file', file);

    fetch('/predict', {
        method: 'POST',
        body: formData
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        var resultDiv = document.getElementById('result');
        var image = document.createElement('img');
        image.src = '/?file=' + data.filename;
        resultDiv.appendChild(image);
        var p = document.createElement('p');
        p.textContent = 'Predicted class: ' + data.class;
        resultDiv.appendChild(p);
    }).catch(function(error) {
        console.error(error);
    });
}

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); 
    predict();
}); 
