from firebase import db

doc_ref = db.collection("test").add({
    "status": "firebase connected"
})

print("Firebase connected successfully")
