const today = new Date();

document.getElementById("today").innerHTML =
today.toLocaleDateString("en-GB",{
    day:"2-digit",
    month:"long",
    year:"numeric"
});