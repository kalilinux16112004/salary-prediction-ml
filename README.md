# Salary Prediction Machine Learning App

A complete **Machine Learning–powered web application** built using **Streamlit** that predicts employee salary based on years of experience.

This project demonstrates the **end-to-end ML workflow** — from data preprocessing and model training to deployment using an interactive web interface.

---

## Project Overview

Salary prediction is a classic **supervised regression problem**. This application uses **Linear Regression** to learn patterns from historical salary data and provides **real-time predictions** through a user-friendly UI.

**Problem Statement:** Can we accurately predict salary using years of experience?

**Solution Approach:**
- Train a Linear Regression model on historical data
- Save the model using `joblib`
- Load into a Streamlit web application
- Enable real-time salary predictions via user input

---

## Features

- Interactive Streamlit web interface
- Machine Learning with Scikit-learn
- CSV-based dataset
- Saved trained model (`.joblib`)
- Real-time predictions
- Data preprocessing
- Jupyter Notebook for training & analysis

---

## Tech Stack

| Category | Tools |
|----------|-------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Model Persistence | Joblib |
| Web Framework | Streamlit |
| Version Control | Git & GitHub |

---

## Project Structure

```
ML_Project/
├── app3.py                  # Streamlit application
├── code.ipynb               # Model training & analysis
├── salaryprediction.csv     # Dataset
├── linear_model.joblib      # Trained model
├── req.txt                  # Dependencies
├── README.md                # Documentation
└── .gitignore               # Ignored files
```

---

## Dataset Information

**File:** `salaryprediction.csv`  
**Type:** Structured CSV  
**Problem Type:** Supervised Regression

### Dataset Columns

| Column | Type | Description |
|--------|------|-------------|
| Experience | Numeric | Years of work experience |
| Salary | Numeric | Corresponding salary |

### Sample Data

| Experience (Years) | Salary |
|-------------------|--------|
| 1.0 | 30,000 |
| 2.0 | 35,000 |
| 4.5 | 52,000 |
| 8.0 | 85,000 |

---

## Machine Learning Model

**Algorithm:** Linear Regression  
**Type:** Supervised Learning  
**Input:** Years of Experience  
**Output:** Salary Prediction

**Why Linear Regression?**
- Simple and interpretable
- Ideal for numerical predictions
- Strong foundation for advanced models

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/kalilinux16112004/salary-prediction-ml.git
cd salary-prediction-ml
```

### 2. Create Virtual Environment
### For Linux Or MacOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### For Windows 
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r req.txt
```

---

## Running the Application

```bash
streamlit run app3.py
```

Open browser: `http://localhost:8501`

### If Model File is Missing

1. Open `code.ipynb`
2. Run all cells sequentially
3. Re-run the Streamlit app

---

## Jupyter Notebook Usage

`code.ipynb` contains:
- Data loading & exploration
- Dataset visualization
- Model training & evaluation
- Model persistence

---

## Future Improvements

- Add more features (education, role, location)
- Implement Polynomial/Random Forest Regression
- Deploy on Streamlit Cloud
- Convert to REST API (Flask/FastAPI)
- Improve accuracy via feature engineering

---

## 👨‍💻 Author

**Vishnuraj Vishwakarma**  
[GitHub](https://github.com/kalilinux16112004)

---

## 📜 License

Educational use only. Free to fork and modify.
