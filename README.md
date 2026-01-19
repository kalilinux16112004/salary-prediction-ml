# 💼 Salary Prediction Machine Learning App

A complete **Machine Learning–powered web application** built using **Streamlit** that predicts an employee’s **salary based on years of experience**.  
This project demonstrates the **end-to-end Machine Learning workflow** — from data preprocessing and model training to deployment using a web interface.

---

## 📌 Project Overview

Salary prediction is a classic **supervised regression problem**.  
This application uses **Linear Regression** to learn patterns from historical salary data and provides real-time predictions through an interactive UI.

### 🔍 Problem Statement
Can we accurately predict a person’s salary using their years of experience?

### 🎯 Solution
- Train a regression model using historical salary data
- Save the trained model using `joblib`
- Load the model into a Streamlit web application
- Allow users to input experience and get salary predictions instantly

---

## 🚀 Features

- 📊 Interactive Streamlit web interface  
- 🧠 Machine Learning model using **Scikit-learn**  
- 📁 CSV-based dataset  
- 💾 Saved trained model (`.joblib`)  
- ⚡ Real-time salary prediction  
- 📉 Data preprocessing & scaling  
- 🧪 Jupyter Notebook for training and analysis  

---

## 🧰 Tech Stack

| Category | Tools |
|--------|-------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Model Persistence | Joblib |
| Web Framework | Streamlit |
| Environment | Virtual Environment (venv) |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```text
ML_Project/
│
├── app3.py                  # Streamlit web application
├── code.ipynb               # Model training & data analysis
├── salaryprediction.csv     # Dataset
├── linear_model.joblib      # Saved trained model
├── req.txt                  # Project dependencies
├── README.md                # Project documentation
├── .gitignore               # Ignored files
└── .venv/                   # Virtual environment (not pushed to GitHub)
## 📊 Dataset Information

**File:** `salaryprediction.csv`

| Column | Description |
|------|-------------|
| Experience | Years of experience |
| Salary | Corresponding salary |

- Clean and small dataset  
- Ideal for regression learning  
- Used for training and predictions  

---

## 🧠 Machine Learning Model

- **Algorithm:** Linear Regression  
- **Learning Type:** Supervised Learning  
- **Feature Variable:** Years of Experience  
- **Target Variable:** Salary  

### Why Linear Regression?
- Simple and interpretable  
- Excellent for understanding regression fundamentals  
- Commonly used in salary prediction problems  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kalilinux16112004/salary-prediction-ml.git
cd salary-prediction-ml
