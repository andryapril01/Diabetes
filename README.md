# Diabetes

# Diabetes Prediction Using Machine Learning

A Machine Learning based web application for predicting diabetes risk using a **Random Forest Classifier** integrated with a **Flask Web Framework**.

This project aims to build a simple prediction system that can help estimate diabetes risk based on several health-related parameters.

---

## Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help individuals become more aware of their health condition and encourage preventive actions.

In this project, a machine learning model is developed to classify whether a person is likely to have diabetes based on input features such as glucose level, BMI, age, and other medical attributes.

The trained model is deployed into a web application using Flask, allowing users to enter their health information and receive prediction results.

---

## Features

✅ Diabetes risk prediction  
✅ Machine Learning classification model  
✅ Random Forest algorithm implementation  
✅ Data preprocessing using RobustScaler  
✅ Flask-based web application  
✅ Interactive user interface  
✅ Real-time prediction through web form  

---

## Machine Learning Workflow

The workflow of this project:

```
Dataset
   |
   ↓
Data Preprocessing
   |
   ↓
Feature Scaling (RobustScaler)
   |
   ↓
Model Training
   |
   ↓
Random Forest Classifier
   |
   ↓
Model Evaluation
   |
   ↓
Flask Deployment
   |
   ↓
Web Prediction System
```

---

## Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Web Framework
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Development Tools
- Jupyter Notebook
- Visual Studio Code

---

## Project Structure

```
DIABETES/
│
├── app.py
├── diabetes.csv
├── hay.ipynb
│
├── Model_random_forsest_diabetes.pkl
├── scaler_diabetes.pkl
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## Model Information

Algorithm used:

**Random Forest Classifier**

Reason for choosing Random Forest:

- Handles classification problems effectively
- Reduces overfitting compared to single decision trees
- Works well with mixed medical features
- Provides stable prediction performance

---

## Installation

Clone this repository:

```bash
git clone https://github.com/andryapril01/Diabetes.git
```

Move into project directory:

```bash
cd Diabetes
```

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## Run Application

Start Flask application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## Prediction Input Features

The model uses several health parameters:

- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

## Model Output

The application provides prediction results:

- Diabetes Risk Detected
- No Diabetes Risk Detected

---

## Future Improvements

Possible improvements:

- Improve model performance using hyperparameter tuning
- Add more machine learning algorithms comparison
- Deploy application to cloud platform
- Add prediction history database
- Improve UI/UX design

---

## Author

**Andry April**

Machine Learning & Data Science Project

GitHub:
https://github.com/andryapril01

---

## Disclaimer

This application is developed for educational and research purposes only.

The prediction result should not be considered as a medical diagnosis. Always consult healthcare professionals for accurate medical assessment.
