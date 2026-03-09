async function predict(){

let review = document.getElementById("review").value;

let response = await fetch("/predict",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({review:review})
})

let data = await response.json()

document.getElementById("result").innerHTML =
data.prediction + "<br>Confidence: " + data.confidence + "%"

}