const form = document.getElementById("predictForm");
const button = document.getElementById("submitBtn");

form.addEventListener("submit", function () {
  button.innerText = "Memproses prediksi...";
  button.disabled = true;
});