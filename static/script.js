function predict() {

    let review = document.getElementById("review").value;

    document.getElementById("loader").style.display = "block";

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: review })
    })

    .then(res => res.json())

    .then(data => {

        document.getElementById("loader").style.display = "none";

        let resultBox = document.getElementById("result");

        resultBox.innerHTML = "Prediction: " + data.prediction;

        let confidence = Math.round(data.confidence * 100);

        let bar = document.getElementById("confidence-bar");

        bar.style.width = confidence + "%";
        bar.innerHTML = confidence + "%";

    });

}

function clearText() {

    document.getElementById("review").value = "";

    document.getElementById("result").innerHTML = "";

    let bar = document.getElementById("confidence-bar");

    bar.style.width = "0%";
    bar.innerHTML = "";

}