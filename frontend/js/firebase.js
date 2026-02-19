// firebase.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyDQBQPvnnd3VkimczOmgnH4njnSK_om1ME",
  authDomain: "ai-pdf-accessibility-sys-581e5.firebaseapp.com",
  projectId: "ai-pdf-accessibility-sys-581e5",
  storageBucket: "ai-pdf-accessibility-sys-581e5.firebasestorage.app",
  messagingSenderId: "229103030080",
  appId: "1:229103030080:web:49ea65836550bfa0a9f4a5"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
