# ================================
# IMPORTS
# ================================
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================================
# THEME STATE
# ================================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# ================================
# THEME TOGGLE
# ================================
top_col1, top_col2 = st.columns([10, 1])
with top_col2:
    if st.button("🌗"):
        st.session_state.theme = (
            "light" if st.session_state.theme == "dark" else "dark"
        )

# ================================
# APPLE GLASS CSS (ADAPTIVE)
# ================================
st.markdown(f"""
<style>

/* ===============================
   COLOR VARIABLES
================================ */
:root {{
  --bg-main: #f5f5f7;
  --bg-gradient: linear-gradient(180deg, #ffffff, #f2f2f7);
  --glass-bg: rgba(255,255,255,0.6);
  --glass-border: rgba(0,0,0,0.08);
  --glass-hover: rgba(255,255,255,0.8);
  --text-primary: #1d1d1f;
  --text-secondary: rgba(0,0,0,0.6);
  --shadow: 0 20px 40px rgba(0,0,0,0.12);
}}

[data-theme="dark"] {{
  --bg-main: #000000;
  --bg-gradient: linear-gradient(180deg, #0e0e13, #050507);
  --glass-bg: rgba(255,255,255,0.08);
  --glass-border: rgba(255,255,255,0.18);
  --glass-hover: rgba(255,255,255,0.14);
  --text-primary: #ffffff;
  --text-secondary: rgba(255,255,255,0.65);
  --shadow: 0 30px 80px rgba(0,0,0,0.6);
}}

/* ===============================
   BASE
================================ */
.stApp {{
  background: var(--bg-main);
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif;
}}

.main {{
  background: var(--bg-gradient);
  background-attachment: fixed;
}}

.block-container {{
  padding: 3rem 4rem !important;
}}

/* ===============================
   GLASS COMPONENTS
================================ */
.glass {{
  background: var(--glass-bg);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border-radius: 24px;
  border: 1px solid var(--glass-border);
  padding: 2.5rem;
  box-shadow: var(--shadow);
  transition: all 0.3s ease;
}}

.glass:hover {{
  background: var(--glass-hover);
  transform: translateY(-2px);
}}

/* ===============================
   TEXT
================================ */
h1, h2, h3 {{
  color: var(--text-primary) !important;
  font-weight: 700;
}}

p, label, span {{
  color: var(--text-secondary);
}}

/* ===============================
   BUTTONS
================================ */
.stButton > button,
.stDownloadButton > button {{
  background: var(--glass-bg);
  color: var(--text-primary);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  padding: 1rem 2.5rem;
  font-weight: 700;
  backdrop-filter: blur(20px);
  transition: all 0.3s ease;
}}

.stButton > button:hover {{
  background: var(--glass-hover);
  transform: translateY(-2px);
}}

/* ===============================
   INPUTS
================================ */
.stSelectbox > div > div,
.stSlider > div > div {{
  background: var(--glass-bg) !important;
  color: var(--text-primary) !important;
  border-radius: 14px;
  border: 1px solid var(--glass-border);
}}

/* ===============================
   METRICS
================================ */
div[data-testid="metric-container"] {{
  background: var(--glass-bg);
  backdrop-filter: blur(20px);
  border-radius: 18px;
  border: 1px solid var(--glass-border);
  box-shadow: var(--shadow);
}}

div[data-testid="stMetricValue"] {{
  color: var(--text-primary);
  font-weight: 700;
}}

</style>

<script>
document.documentElement.setAttribute("data-theme", "{st.session_state.theme}");
</script>
""", unsafe_allow_html=True)

# ================================
# LOAD MODEL
# ================================
@st.cache_resource
def load_model(name):
    models = {
        "Linear Regression": "linear_model.joblib",
        "Lasso Regression": "lasso_model.joblib",
        "Ridge Regression": "ridge_model.joblib",
        "Elastic Net": "elastic_model.joblib",
    }
    return (
        joblib.load(models[name]),
        joblib.load("scaler.joblib"),
        joblib.load("model_columns.joblib"),
    )

# ================================
# HERO
# ================================
st.markdown("""
<div class="glass" style="text-align:center;">
  <h1>💎 Salary Predictor</h1>
  <p>Apple-style AI Salary Intelligence</p>
</div>
""", unsafe_allow_html=True)

# ================================
# MODEL SELECTION
# ================================
st.markdown('<div class="glass">', unsafe_allow_html=True)
model_choice = st.selectbox(
    "🤖 Select Model",
    ["Linear Regression", "Lasso Regression", "Ridge Regression", "Elastic Net"]
)
st.markdown('</div>', unsafe_allow_html=True)

model, scaler, columns = load_model(model_choice)

# ================================
# PREDICTION FUNCTION
# ================================
def predict(df):
    df = df.reindex(columns=columns, fill_value=0)
    return model.predict(scaler.transform(df))

# ================================
# TABS
# ================================
tab1, tab2 = st.tabs(["👤 Single Prediction", "📊 Bulk Prediction"])

# ---------------- SINGLE
with tab1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    age = st.slider("Age", 18, 60, 30)
    years = st.slider("Total Working Years", 0, 40, 10)
    job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
    overtime = st.radio("Overtime", ["Yes", "No"], horizontal=True)

    st.markdown('</div>', unsafe_allow_html=True)

    df = pd.DataFrame([{
        "Age": age,
        "TotalWorkingYears": years,
        "JobLevel": job_level,
        "OverTime_Yes": 1 if overtime == "Yes" else 0
    }])

    if st.button("✨ Predict Salary"):
        salary = predict(df)[0]

        c1, c2, c3 = st.columns(3)
        c1.metric("💵 Monthly", f"${salary:,.2f}")
        c2.metric("📅 Annual", f"${salary*12:,.2f}")
        c3.metric("⏱ Hourly", f"${salary/160:,.2f}")

# ---------------- BULK
with tab2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    file = st.file_uploader("Upload CSV", type=["csv"])
    st.markdown('</div>', unsafe_allow_html=True)

    if file:
        df = pd.read_csv(file)
        preds = predict(df)
        df["Predicted_Monthly_Income"] = preds

        st.dataframe(df.head(20), use_container_width=True)

        st.download_button(
            "⬇ Download Results",
            df.to_csv(index=False).encode("utf-8"),
            "salary_predictions.csv",
            "text/csv"
        )

# ================================
# FOOTER
# ================================
st.markdown("""
<p style="text-align:center; opacity:0.6; margin-top:3rem;">
Apple-grade Glass UI • Streamlit • AI Powered
</p>
""", unsafe_allow_html=True)
