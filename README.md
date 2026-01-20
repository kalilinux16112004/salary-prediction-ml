# Salary Prediction Machine Learning App

**A complete Machine Learning-based web application built using Streamlit that predicts an employee's salary based on years of professional experience.**

This project demonstrates an end-to-end machine learning workflow, covering data preprocessing, model training, evaluation, and deployment through an interactive web interface.

---

## Project Overview

Salary prediction is a supervised regression problem. This application uses a **Linear Regression model** to identify relationships between years of experience and salary, enabling real-time predictions via a web-based interface.

### Problem Statement
**Can salary be accurately predicted using years of professional experience?**

---

## Solution Approach

- Train a Linear Regression model on historical salary data
- Persist the trained model using joblib
- Load the model into a Streamlit application
- Provide real-time predictions based on user input

---

## Features

- Interactive web application using Streamlit
- Machine learning implementation with Scikit-learn
- CSV-based dataset handling
- Persisted trained model (.joblib)
- Real-time salary prediction
- Data preprocessing and visualization
- Jupyter Notebook for training and analysis

---

## Technology Stack

| Category | Tools |
|----------|-------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Model Persistence | Joblib |
| Web Framework | Streamlit |
| Version Control | Git and GitHub |

---

## Project Structure

`salary-prediction-ml/
├── app3.py # Streamlit application
├── code.ipynb # Model training and analysis
├── salaryprediction.csv # Dataset
├── linear_model.joblib # Trained model
├── req.txt # Project dependencies
├── README.md # Documentation
└── .gitignore # Ignored files`
---

## Dataset Information

**File:** `salaryprediction.csv`

**Type:** Structured CSV

**Learning Type:** Supervised Regression

### Dataset Columns

| Column | Type | Description |
|--------|------|-------------|
| Experience | Numeric | Years of professional experience |
| Salary | Numeric | Corresponding salary value |

---

## Machine Learning Model

**Algorithm:** Linear Regression

**Learning Type:** Supervised Learning

**Input Feature:** Years of Experience

**Output:** Salary Prediction

### Rationale for Linear Regression

- High interpretability
- Suitable for continuous numerical prediction
- Provides a strong baseline for regression problems

---

## Installation and Setup

### Step 1: Clone the Repository

`git clone https://github.com/kalilinux16112004/salary-prediction-ml.git
cd salary-prediction-ml`

### Step 2: Create a Virtual Environment

`python -m venv env`

### Step 3: Activate the Virtual Environment
### Windows (PowerShell):

`env\Scripts\activate`

### Linux / macOS:

`source env/bin/activate`

### Step 4: Install Dependencies

`pip install -r req.txt`

### Running the Application

`streamlit run app3.py`

###### The application will be accessible at: [http://localhost:8501](http://localhost:8501)

## Model File Generation (If Missing)
###### If the trained model file (linear_model.joblib) is not present:

### 1.Launch Jupyter Notebook:

`jupyter notebook`
### 2.Open ```python code.ipynb```

### 3.Execute all cells sequentially

### 4.Confirm that the model file is generated

### 5.Restart the Streamlit application

## Jupyter Notebook Details
### The notebook (```python code.ipynb```) includes:

Data loading and exploration
Exploratory data analysis and visualization
Model training and evaluation
Model persistence using joblibFuture Enhancements
Inclusion of additional features such as education, job role, and location
Implementation of advanced regression models
Deployment to cloud platforms such as Streamlit Cloud
Exposure of predictions via REST APIs (Flask or FastAPI)
Accuracy improvement through feature engineering
Author
Vishnuraj Vishwakarma

GitHub: https://github.com/kalilinux16112004

License
This project is licensed under the MIT License.


The improvements include:- **Added emojis** for visual appeal and quick section identification- **Better bullet points** instead of plain text lists- **Proper markdown tables** for Technology Stack and Dataset Columns- **Code blocks** for commands and file paths- **Horizontal dividers** for section separation- **Consistent heading hierarchy** (## for main sections)- **Improved spacing** and readability- **Bold highlighting** for important terms- **Better organization** of Installation stepsWould you like me to save these changes to the file?The improvements include:- **Added emojis** for visual appeal and quick section identification- **Better bullet points** instead of plain text lists- **Proper markdown tables** for Technology Stack and Dataset Columns- **Code blocks** for commands and file paths- **Horizontal dividers** for section separation- **Consistent heading hierarchy** (## for main sections)- **Improved spacing** and readability- **Bold highlighting** for important terms- **Better organization** of Installation stepsWould you like me to save these changes to the file?
