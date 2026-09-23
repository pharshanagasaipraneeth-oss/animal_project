# 🦁 Animal Image Classification using Machine Learning

## 📌 Project Overview

**Animal Image Classification using Machine Learning** is an image classification project that identifies an animal from an uploaded image.

The model is trained to classify images into three categories:

* 🦁 Lion
* 🐆 Leopard
* 🐎 Horse

The project includes **Exploratory Data Analysis (EDA), image preprocessing, model building, model evaluation, prediction, and deployment using Streamlit**.

---

## 🎯 Objectives

* Classify animal images into predefined categories.
* Understand and preprocess image datasets.
* Build a machine learning/deep learning image classification model.
* Evaluate the model using performance metrics.
* Predict the animal class from a new image.
* Deploy the trained model using Streamlit.

---

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Pillow (PIL)**
* **TensorFlow / Keras**
* **Scikit-learn**
* **Streamlit**
* **Jupyter Notebook**

---

## 📂 Project Structure

```text
animal_project/
│
├── app.py
├── animal_classification_model.keras
├── requirements.txt
├── README.md
│
├── animal_dataset/
│   ├── Lion/
│   ├── Leopard/
│   └── Horse/
│
└── notebook/
    └── animal_classification.ipynb
```

> The exact file names may vary depending on the saved model and notebook used in the project.

---

## 📊 Dataset

The project uses an animal image dataset containing images of different animal categories.

For this project, three classes were selected:

| Class      | Description        |
| ---------- | ------------------ |
| 🦁 Lion    | Images of lions    |
| 🐆 Leopard | Images of leopards |
| 🐎 Horse   | Images of horses   |

The selected images were divided into training and testing datasets.

---

## 🔍 Exploratory Data Analysis

The following EDA steps were performed:

* Examined the dataset structure.
* Identified the available animal classes.
* Counted images in each class.
* Visualized sample animal images.
* Analyzed class distribution.
* Used a pie chart to visualize the distribution of classes.

---

## 🧹 Image Preprocessing

Before training the model, the images were preprocessed.

### Steps performed:

1. Loaded the images.
2. Converted images into a consistent format.
3. Resized images to:

```text
128 × 128
```

4. Converted images into NumPy arrays.
5. Normalized pixel values:

```text
Pixel Value / 255.0
```

6. Assigned numerical labels to the animal classes.
7. Split the dataset into training and testing data.

---

## 🤖 Model Architecture

A Convolutional Neural Network (CNN) was used for image classification.

The model architecture consists of:

```text
Input Image
     ↓
Conv2D - 32 Filters
     ↓
MaxPooling2D
     ↓
Conv2D - 64 Filters
     ↓
MaxPooling2D
     ↓
Conv2D - 128 Filters
     ↓
MaxPooling2D
     ↓
Flatten
     ↓
Dense - 128 Neurons
     ↓
Dropout - 0.5
     ↓
Output Layer - 3 Classes
```

The output layer uses **Softmax activation** to generate probabilities for the three animal classes.

---

## ⚙️ Model Compilation

The model was compiled using:

```python
optimizer = "Adam"
loss = "sparse_categorical_crossentropy"
metrics = ["accuracy"]
```

---

## 📈 Model Evaluation

The trained model was evaluated using the test dataset.

Evaluation included:

* Accuracy
* Confusion Matrix
* Prediction results
* Confidence score

The confusion matrix was used to understand how well the model classified each animal category.

---

## 🔮 Prediction

The trained model can classify a new uploaded image.

The prediction process is:

```text
Upload Image
      ↓
Resize to 128 × 128
      ↓
Normalize Pixel Values
      ↓
Model Prediction
      ↓
Find Highest Probability
      ↓
Display Animal Class
      ↓
Display Confidence
```

Example:

```text
Animal: Leopard
Confidence: 87.45%
```

---

## 🌐 Streamlit Deployment

The trained model is deployed using **Streamlit**.

The application allows the user to:

1. Upload an animal image.
2. Display the uploaded image.
3. Process the image.
4. Predict the animal.
5. Display the predicted class.
6. Display the prediction confidence.

Run the application using:

```bash
streamlit run app.py
```

---

## 📦 Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Go to the project directory:

```bash
cd animal_project
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📋 Requirements

Example `requirements.txt`:

```text
numpy
pandas
matplotlib
Pillow
tensorflow
scikit-learn
streamlit
```

---

## 💡 Features

* 🦁 Lion classification
* 🐆 Leopard classification
* 🐎 Horse classification
* 🖼️ Image upload
* 🤖 Machine learning model prediction
* 📊 Confidence score
* 📈 Model evaluation
* 🌐 Streamlit web application

---

## 🚀 Future Improvements

The project can be improved by:

* Adding more animal classes.
* Increasing the dataset size.
* Using data augmentation.
* Improving model accuracy.
* Using transfer learning models such as MobileNet, VGG16, or ResNet.
* Adding more evaluation metrics.
* Deploying the application online.

---

## 🎓 Learning Outcomes

Through this project, I learned:

* Image dataset handling
* Exploratory Data Analysis
* Image preprocessing
* Feature extraction
* CNN model building
* Model training and evaluation
* Confusion matrix analysis
* Image prediction
* Model saving and loading
* Streamlit deployment
* GitHub project management

---

## 👨‍💻 Author

**P. Harsha Naga Sai Praneeth**

MSc Computer Science

---

## ⭐ Project

**Animal Image Classification using Machine Learning**

A machine learning project that classifies animal images into **Lion, Leopard, and Horse** categories using a CNN-based image classification model and Streamlit deployment.
