# 💼 Salary Prediction Machine Learning App

**A complete Machine Learning-based web application built using Streamlit that predicts an employee's salary based on years of professional experience.**

This project demonstrates an end-to-end machine learning workflow, covering data preprocessing, model training, evaluation, and deployment through an interactive web interface.

---

## 📋 Project Overview

Salary prediction is a supervised regression problem. This application uses a **Linear Regression model** to identify relationships between years of experience and salary, enabling real-time predictions via a web-based interface.

### ❓ Problem Statement
**Can salary be accurately predicted using years of professional experience?**

---

## 🎯 Solution Approach

- Train a Linear Regression model on historical salary data
- Persist the trained model using **joblib**
- Load the model into a **Streamlit** application
- Provide real-time salary predictions based on user input

---

## ✨ Features

- 📊 Interactive web application using Streamlit
- 🤖 Machine learning implementation with Scikit-learn
- 📁 CSV-based dataset handling
- 💾 Persisted trained model (`.joblib`)
- ⚡ Real-time salary prediction
- 📈 Data preprocessing and visualization
- 📓 Jupyter Notebook for training and analysis

---

## 🛠️ Technology Stack

| Category | Tools |
|--------|------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Model Persistence | Joblib |
| Web Framework | Streamlit |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```text
salary-prediction-ml/
├── app3.py                 # Streamlit application
├── code.ipynb              # Model training & analysis
├── salaryprediction.csv    # Dataset
├── linear_model.joblib     # Trained model
├── req.txt                 # Project dependencies
├── README.md               # Documentation
└── .gitignore              # Ignored files
```

---

## 📊 Dataset Information

**File:** `salaryprediction.csv`  
**Type:** Structured CSV  
**Learning Type:** Supervised Regression

### Dataset Columns

| Column | Type | Description |
|------|------|-------------|
| Experience | Numeric | Years of professional experience |
| Salary | Numeric | Corresponding salary value |

---

## 🤖 Machine Learning Model

- **Algorithm:** Linear Regression
- **Learning Type:** Supervised Learning
- **Input Feature:** Years of Experience
- **Output:** Salary Prediction

### Why Linear Regression?

- ✔ High interpretability
- ✔ Suitable for continuous numerical prediction
- ✔ Strong baseline model for regression problems

---

## 🚀 Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kalilinux16112004/salary-prediction-ml.git
cd salary-prediction-ml
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv env
```

### 3️⃣ Activate the Virtual Environment

**Windows (PowerShell):**
```bash
env\Scripts\activate
```

**Linux / macOS:**
```bash
source env/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r req.txt
```

---

## ▶️ Running the Application

```bash
streamlit run app3.py
```

🌐 The application will be available at: **http://localhost:8501**

---

## 📝 Model File Generation (If Missing)

If `linear_model.joblib` is not present:

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open `code.ipynb`
3. Run all cells sequentially
4. Confirm model file generation
5. Restart the Streamlit app

---

## 📓 Jupyter Notebook Details

The notebook (`code.ipynb`) includes:

- Data loading & exploration
- Exploratory Data Analysis (EDA)
- Model training & evaluation
- Model persistence using Joblib

---

## 🔮 Future Enhancements

- Add features like education, job role & location
- Implement advanced regression models
- Deploy on Streamlit Cloud
- Expose predictions via REST APIs (Flask/FastAPI)
- Improve accuracy using feature engineering

---

## 👨‍💻 Author

**Vishnuraj Vishwakarma**  
🔗 GitHub: https://github.com/kalilinux16112004

---

## 📄 License

This project is licensed under the **MIT License**.

