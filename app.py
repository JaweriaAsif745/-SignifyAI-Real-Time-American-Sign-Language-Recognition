from flask import Flask, request, jsonify, render_template
import torch
import torch.nn.functional as F
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import json
import os
from PIL import ImageOps

app = Flask(__name__)

# -------------------------------
# Paths
# -------------------------------
model_path = "model/asl_model_files_re/asl_model.pth"
classes_path = "model/asl_model_files_re/asl_classes.json"


# -------------------------------
# Device
# -------------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# -------------------------------
# Load Classes
# -------------------------------
with open(classes_path, "r") as f:
    classes = json.load(f)

print(classes)
# -------------------------------
# Define Model (ResNet18)
# -------------------------------

model = models.resnet18(weights=None)   # no internet download, empty init

# Freeze all layers
for param in model.parameters():
    param.requires_grad = False

# Unfreeze last ResNet block (layer4)
for param in model.layer4.parameters():
    param.requires_grad = True

# Replace final fully connected (FC) layer with our 29 classes
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 29)

# Load saved model
model.load_state_dict(torch.load(model_path, map_location=device))
model = model.to(device)
model.eval()


# -------------------------------
# Define Image Transform
# -------------------------------
image_size = 224
val_transforms = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])  # <-- SAME as training
])



from PIL import ImageOps

# -------------------------------
# Prediction Function (with preprocessing)
# -------------------------------
def predict_image(img_path):
    # Open as RGB (keep it same as training data)
    img = Image.open(img_path).convert("RGB")

    # Apply transforms
    img_tensor = val_transforms(img).unsqueeze(0).to(device)

    # Predict
    with torch.no_grad():
        outputs = model(img_tensor)
        probs = F.softmax(outputs, dim=1)
        conf, pred = torch.max(probs, 1)

    return classes[pred.item()], float(conf.item())



# -------------------------------
# Routes
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/alphabets")
def alphabets():
    return render_template("alphabets.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

# Webcam-based recognition
@app.route("/recognize")
def recognize():
    return render_template("recognize.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filepath = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(filepath)

    pred_class, confidence = predict_image(filepath)

    # ✅ Delete file after prediction
    if os.path.exists(filepath):
        os.remove(filepath)

    return jsonify({"prediction": pred_class, "confidence": confidence})


# Image upload-based recognition
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "file" not in request.files:
            return "⚠️ No file uploaded"

        file = request.files["file"]
        if file.filename == "":
            return "⚠️ No selected file"

        filepath = os.path.join("uploads", file.filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(filepath)

        pred_class, confidence = predict_image(filepath)

        # ✅ Delete file after prediction
        if os.path.exists(filepath):
            os.remove(filepath)

        return render_template("upload_result.html",
                               filename=file.filename,
                               prediction=pred_class,
                               confidence=round(confidence*100, 2))
    return render_template("upload.html")


# -------------------------------
# Run
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
