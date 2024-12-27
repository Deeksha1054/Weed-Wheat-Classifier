from flask import Flask, render_template, request, jsonify
import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import io
import os

app = Flask(__name__)

# Define class labels
class_labels = {0: 'Other', 1: 'Weed', 2: 'Wheat'}

# Load your trained model (make sure to adjust this if your model is different)
model = torch.load('best_model.pth', map_location=torch.device('cpu'))
model.eval()  # Set the model to evaluation mode

# Image transformation for inference
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Validate the file type (only images allowed)
    if file and allowed_file(file.filename):
        try:
            # Process the uploaded image
            img = Image.open(file.stream)
            img = transform(img).unsqueeze(0)  # Add batch dimension

            # Predict the class
            with torch.no_grad():
                output = model(img)

            # Get predicted class
            prediction = np.argmax(output.numpy(), axis=1)[0]
            predicted_label = class_labels.get(prediction, 'Unknown')

            return jsonify({'prediction': predicted_label})

        except Exception as e:
            return jsonify({'error': f'Error in processing the image: {str(e)}'})

    else:
        return jsonify({'error': 'Invalid file format. Please upload a valid image file.'})

def allowed_file(filename):
    """Check if the file has a valid image extension"""
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
