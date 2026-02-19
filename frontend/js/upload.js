console.log("upload.js loaded");

document.getElementById("uploadBtn").addEventListener("click", async () => {
  const fileInput = document.getElementById("pdfFile");
  const file = fileInput.files[0];

  if (!file) {
    alert("Please select a PDF");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch("http://127.0.0.1:8000/api/upload", {
    method: "POST",
    body: formData
  });

  if (res.ok) {
    window.location.href = "editor.html";
  } else {
    alert("Upload failed");
  }
});
