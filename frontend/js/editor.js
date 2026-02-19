console.log("EDITOR.JS LOADED");

const formContainer = document.getElementById("formContainer");

fetch("http://127.0.0.1:8000/api/generated-form")
  .then(res => {
    if (!res.ok) throw new Error("Failed to load form");
    return res.text();
  })
  .then(html => {
    formContainer.innerHTML = html;
  })
  .catch(err => {
    console.error(err);
    formContainer.innerText = "Error loading accessible form";
  });

function saveForm() {
  alert("Form data saved (PDF generation is next step)");
}
const sigUpload = document.getElementById("signatureUpload");
const sigCanvas = document.getElementById("signaturePad");
const sigCtx = sigCanvas.getContext("2d");

sigUpload.addEventListener("change", e => {
  const file = e.target.files[0];
  if (!file) return;

  const img = new Image();
  img.onload = () => {
    sigCtx.clearRect(0, 0, sigCanvas.width, sigCanvas.height);

    // scale image to fit signature box
    const scale = Math.min(
      sigCanvas.width / img.width,
      sigCanvas.height / img.height
    );

    const w = img.width * scale;
    const h = img.height * scale;

    sigCtx.drawImage(
      img,
      (sigCanvas.width - w) / 2,
      (sigCanvas.height - h) / 2,
      w,
      h
    );
  };

  img.src = URL.createObjectURL(file);
});
