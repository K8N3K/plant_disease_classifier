🌱 Plant Disease Prediction

A deep-learning-based web application that predicts plant diseases from leaf images. The model was trained using the PlantVillage dataset, packaged into a Streamlit application, containerized with Docker, published to Docker Hub, and deployed as a live web application using Render.

🚀 Project Overview

This project demonstrates an end-to-end machine learning deployment workflow:

PlantVillage Dataset
        ↓
CNN Model Training
        ↓
Model Evaluation
        ↓
Streamlit Application
        ↓
Docker Containerization
        ↓
Docker Hub
        ↓
Render Deployment
        ↓
🌐 Live Web Application

The application allows users to upload an image of a plant leaf and receive a predicted disease class along with the model's confidence.

🧠 Machine Learning Model

The model is a Convolutional Neural Network (CNN) designed for image classification.

The input images are resized to:

224 × 224 × 3

and pixel values are normalized to the range:

0 – 1

The model uses convolutional layers to learn visual features from plant leaves, followed by fully connected layers for classification.

The final layer uses softmax activation to produce a probability for each disease class.

Model workflow
Input Leaf Image
       ↓
Resize to 224 × 224
       ↓
Normalize Pixel Values
       ↓
Convolutional Layers
       ↓
Feature Extraction
       ↓
Dense Layer
       ↓
Softmax
       ↓
Predicted Plant Disease
📊 Model Evaluation

Model performance was evaluated using a validation dataset.

In addition to accuracy, a confusion matrix was used to examine how well the model distinguished between individual disease classes.

The confusion matrix was particularly useful for identifying classes that were being confused with one another.

For reliable evaluation, the validation data generator was configured with:

shuffle=False

This ensures that predictions remain aligned with their corresponding true labels when calculating the confusion matrix.

🌐 Streamlit Web Application

A Streamlit interface was created around the trained model.

Users can:

Open the web application.
Upload a plant leaf image.
View the uploaded image.
Run the trained model.
See the predicted disease.
View the prediction confidence.

The application performs the same preprocessing used during model training before passing the image to the neural network.

🐳 Dockerization

The application was containerized using Docker so that the model, Python environment, dependencies, and Streamlit application could be packaged together.

A typical Docker workflow for the project is:

docker build -t plant-disease-prediction .

Run the container locally:

docker run -p 8501:8501 plant-disease-prediction

The application can then be accessed through:

http://localhost:8501
Why Docker?

Docker makes the application environment reproducible.

Instead of requiring every user or deployment platform to manually install:

Python
TensorFlow
Streamlit
NumPy
Pillow
other dependencies

the required environment is packaged into the Docker image.

📦 Docker Hub

After building and testing the Docker image, the image was uploaded to Docker Hub.

The deployment workflow becomes:

Source Code
     ↓
Dockerfile
     ↓
Docker Image
     ↓
Docker Hub
     ↓
Render

Docker Hub acts as the image repository from which the deployment platform can obtain the application image.

☁️ Deployment with Render

The Dockerized application was subsequently deployed using Render.

Render pulls the Docker image, starts the container, and exposes the Streamlit application as a web service.

The resulting deployment provides a publicly accessible website without requiring users to run the project locally.

Docker Hub
     ↓
   Render
     ↓
Docker Container
     ↓
Streamlit
     ↓
Public Website
🛠️ Technologies Used
Python — Programming language
TensorFlow / Keras — Deep learning and model training
NumPy — Numerical processing
Pillow — Image processing
Streamlit — Web application interface
Scikit-learn — Model evaluation
Matplotlib / Seaborn — Visualization and confusion matrix
Docker — Application containerization
Docker Hub — Container image hosting
Render — Cloud deployment
📁 Project Structure
Plant_Disease/
│
├── app.py
├── plant_disease_prediction_model.h5
├── class_indices.json
├── requirements.txt
├── Dockerfile
└── README.md
⚙️ Running Locally

Clone the repository:

git clone <repository-url>
cd Plant_Disease

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py
🐳 Running with Docker

Build the image:

docker build -t plant-disease-prediction .

Run it:

docker run -p 8501:8501 plant-disease-prediction

Open:

http://localhost:8501
☁️ Deployment Architecture
                  ┌─────────────────────┐
                  │   PlantVillage      │
                  │      Dataset        │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   CNN / TensorFlow  │
                  │       Model         │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │     Streamlit       │
                  │        App          │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │       Docker        │
                  │       Image         │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │     Docker Hub      │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │       Render        │
                  │   Cloud Deployment  │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   🌐 Live Website   │
                  └─────────────────────┘
🔮 Future Improvements

Potential improvements include:

Transfer learning with architectures such as MobileNetV2 or EfficientNet
Additional data augmentation
Improved handling of class imbalance
More extensive real-world testing
Improved UI/UX
Confidence visualization
Disease information and treatment recommendations
Larger and more diverse datasets
Continuous model evaluation on real-world images
