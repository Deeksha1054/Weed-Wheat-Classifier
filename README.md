### README.md

---

# Wheat and Weed Classification Model 🌾

This repository hosts a **PyTorch-trained deep learning model** designed to classify images into three categories: **Other**, **Weed**, and **Wheat**. The project combines advanced machine learning techniques with an intuitive deployment framework to assist in agricultural applications.

---

## 🚀 Features

- **Accurate Multi-Class Classification**  
   Trained to distinguish between:
   - **Other**: Non-crop objects or irrelevant content.
   - **Weed**: Unwanted plants competing with crops.
   - **Wheat**: Target crop for agricultural purposes.

- **Real-Time Deployment**  
   Integrated Flask web application for seamless image upload and prediction.

- **Customizable & Scalable**  
   Open for enhancements and integration with other agricultural systems.

---

## 📂 Project Structure

```plaintext
.
├── model/                   # Contains the PyTorch-trained model
│   └── best_model.pth       # Saved model file
├── static/                  # CSS and other static assets
│   └── styles.css           # Styling for the web app
├── templates/               # HTML templates for Flask
│   ├── index.html           # Main user interface
│   └── upload.html          # Image upload & prediction page
├── app.py                   # Flask application for deployment
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🔧 Setup & Usage

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or above
- Pip package manager
- PyTorch and its dependencies

### Steps to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/wheat-weed-classification.git
   cd wheat-weed-classification
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask App**
   ```bash
   python app.py
   ```

4. **Access the Application**  
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

5. **Upload an Image**  
   - Use the interface to upload an image.
   - View predictions and results directly on the page.

---

## 🛠 Model Details

- **Framework**: PyTorch
- **Architecture**: Custom CNN for classification
- **Trained On**: A balanced dataset containing labeled images of wheat, weed, and other objects.
- **Performance**: Optimized for precision and accuracy with minimal overfitting.

---

## 🖼 Labels

- **Other**: Represented by **0** (Non-relevant objects).
- **Weed**: Represented by **1** (Unwanted plants).
- **Wheat**: Represented by **2** (Target crop).

---

## 👥 About Us

This project was created by a team of AI enthusiasts aiming to bring innovation to agriculture:

| Name                     | Role                  |
|------------------        |-----------------------|
| *Deeksha R G*         | Team Lead             |
| *S B Gnanashree Jain* | Teammate 2            |
| *Siddaraju B R*        | Teammate 3            |
| *Supriya S*            | Teammate 4            |
| *Akasha S*             | Teammate 5            |
---

## 🙏 Acknowledgement

We extend our heartfelt gratitude to:

- **Dr. S R Hemanth**, our mentor, for his invaluable guidance and support throughout this project.  
- **Dr. Agughasi Victor I.**, our instructor, for providing us with the foundational knowledge and encouragement to successfully complete this project.

Their expertise and mentorship have been instrumental in shaping this work. 

---

## 🚀 Future Improvements

- Expanding to other crop types.
- Integrating advanced data preprocessing techniques.
- Deploying the application on cloud platforms for scalability.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute and enhance this repository to make it better for agricultural advancements!
