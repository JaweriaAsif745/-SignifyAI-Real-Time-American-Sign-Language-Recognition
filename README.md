# ✋ SignifyAI: Real-Time American Sign Language Recognition 

### 📌 Overview

SignifyAI is an intelligent system that recognizes **American Sign Language (ASL)** hand gestures using **deep learning** and **computer vision**.  
It allows users to upload ASL gesture images **or use their webcam** for **real-time recognition**, translating hand gestures into corresponding English alphabets.

---

## 🌟 Features

✅ **ASL Alphabet Recognition** (A–Z + special signs)  
✅ **Upload Image Prediction** – Detects gestures from uploaded images  
✅ **Live Webcam Mode** – Real-time ASL recognition directly from camera  
✅ **Interactive Web Interface** built using **Flask**  
✅ **Pretrained ResNet18 model** fine-tuned for ASL dataset  
✅ **Data Augmentation** for better lighting & background adaptability  
✅ **Automatic Cleanup** of uploaded files after prediction  
---

## 🏗️ Project Structure

```
SignifyAI: Real-Time American Sign Language Recognition/
│
├── model/
│   └── asl_model_files_re/
│       ├── asl_model.pth
│       └── asl_classes.json
|
|__ notebook/
|   |__ asl-signlanguage-detector.ipynb
│
├── static/
│   ├── css/
│   ├── js/
|   |   |___quiz.js
|   |   |___script.js
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── upload.html
│   ├── upload_result.html
│   ├── recognize.html
│   ├── alphabets.html
│   └── quiz.html
│
├── uploads/               # temporary folder for uploaded files
│
├── app.py                 # main Flask app
├── requirements.txt       # dependencies
└── README.md
```

---

## 🧩 Model Details

* **Architecture:** ResNet18
* **Framework:** PyTorch
* **Training Augmentations:**

  * Random rotations
  * Color jitter
  * Random affine transformations
  * Normalization with ImageNet stats
* **Validation Transform:** Resize → Normalize → Tensor
* **Accuracy:** High accuracy on clean dataset and improved real-world performance after retraining.

---

## 🎬 Demo Videos

📸 **1. Website Walkthrough:**  
👉  https://github.com/user-attachments/assets/73fef755-8e1f-4bc5-b384-34790c39c9a2

🖼️ **2. Upload Recognition (Image Prediction):**  
👉  https://github.com/user-attachments/assets/2099a1af-6b1d-453a-870c-20049fd8fc22

📹 **3. Live Webcam Recognition:**  
👉  https://github.com/user-attachments/assets/981924ae-1a94-4d59-a4e7-f2bc925a8ddb

---

## ⚙️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/JaweriaAsif745/-SignifyAI-Real-Time-American-Sign-Language-Recognition.git
cd ASL-Recognition-System
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask app

```bash
python app.py
```

### 4️⃣ Open in browser

Go to: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

🧩 Usage
🔹 Image Upload Mode

Open the Upload page.
Upload a hand gesture image.
The model predicts the alphabet and confidence score.

🔹 Live Webcam Mode

Go to the Recognize page.
Allow camera permissions.
Show your ASL gesture in front of the webcam.
See live predictions appear instantly.
---
## 🖼️📸 Screenshots
## 🏠 Home Page
<img width="1521" height="1704" alt="127 0 0 1_5000_ (1)" src="https://github.com/user-attachments/assets/cfc77130-0423-4121-9eb3-f5025782c425" />

## 🧠 Alphabets Page
<img width="1886" height="892" alt="image" src="https://github.com/user-attachments/assets/e5f040d5-459c-498b-9937-4db96ad44b71" />

## 📹 Quiz Page
<img width="1689" height="1208" alt="127 0 0 1_5000_quiz" src="https://github.com/user-attachments/assets/bc0ec5b6-72f1-42c2-8fd4-d53c7ac66a95" />

## 📤 Image Upload Page
<img width="1909" height="871" alt="image" src="https://github.com/user-attachments/assets/77243686-e2ad-4258-bd18-e39a2214e4fe" />

## 📤 Image Result Page
<img width="783" height="555" alt="image" src="https://github.com/user-attachments/assets/4a86fabe-5ba9-4f59-9e1e-2dd4e68130b3" />


## 🤖 Webcam Detection
<img width="1064" height="513" alt="image" src="https://github.com/user-attachments/assets/12e8a47b-4594-4023-b8f7-4823732f90a9" />


---
## 🧰 Tech Stack

| Category       | Tools                 |
| -------------- | --------------------- |
| **Backend**    | Flask, Python         |
| **Frontend**   | HTML, CSS, JavaScript |
| **AI/ML**      | PyTorch, ResNet18     |
| **Deployment** | Localhost (Flask)     |
| **Dataset**    | ASL Alphabet Dataset  |

---
## 🧾 License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).
---

## 💡 Future Improvements

* Implement **word-level ASL translation** (sequence-based using video frames).
* Add **voice output** (text-to-speech).
* Improve real-time performance using **ONNX** or **TensorRT**.

---

## 👩‍💻 Author

**Jaweria Asif**
📍 Pakistan
💬 *“Building AI that understands human gestures.”*
🔗 https://github.com/JaweriaAsif745

---
⭐ If you like this project, give it a star on GitHub!

---


