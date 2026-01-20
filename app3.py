import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Configuration ---
st.set_page_config(
    page_title="Salary Prediction App",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Premium Apple Glass UI CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;500;600;700&display=swap');
    
    /* Force remove sidebar completely */
    [data-testid="stSidebar"],
    section[data-testid="stSidebar"],
    [data-testid="stSidebarNav"] {
        display: none !important;
        width: 0 !important;
    }
    
    button[kind="header"] {
        display: none !important;
    }
    
    /* Main app styling */
    .stApp {
        background: #000000;
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif;
    }
    
    .main {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        background-attachment: fixed;
        padding: 0 !important;
    }
    
    .block-container {
        max-width: 100% !important;
        padding: 3rem 4rem !important;
    }
    
    /* Animated gradient background */
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 30%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(72, 149, 239, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, rgba(162, 155, 254, 0.2) 0%, transparent 50%);
        pointer-events: none;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    /* Premium Glass Card */
    .glass-container {
        position: relative;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: saturate(180%) blur(20px);
        -webkit-backdrop-filter: saturate(180%) blur(20px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 
            0 8px 32px 0 rgba(0, 0, 0, 0.37),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .glass-container:hover {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.25);
        transform: translateY(-2px);
        box-shadow: 
            0 12px 48px 0 rgba(0, 0, 0, 0.5),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
    }
    
    /* Hero Header */
    .hero-header {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: saturate(180%) blur(30px);
        -webkit-backdrop-filter: saturate(180%) blur(30px);
        border-radius: 28px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 4rem 3rem;
        margin-bottom: 3rem;
        text-align: center;
        box-shadow: 
            0 20px 60px 0 rgba(0, 0, 0, 0.5),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
        position: relative;
        overflow: hidden;
    }
    
    .hero-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    }
    
    .hero-header h1 {
        background: linear-gradient(135deg, #ffffff 0%, #e0e0ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 4rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -2px;
        text-shadow: 0 0 30px rgba(255,255,255,0.1);
    }
    
    .hero-header p {
        color: rgba(255, 255, 255, 0.7);
        font-size: 1.3rem;
        margin-top: 1rem;
        font-weight: 400;
    }
    
    /* Section headers */
    .section-header {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        padding-bottom: 0.8rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        letter-spacing: -0.5px;
    }
    
    /* Tabs - Apple Style */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 0.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: rgba(255, 255, 255, 0.6);
        border-radius: 12px;
        padding: 1rem 2.5rem;
        font-weight: 600;
        font-size: 1.05rem;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: rgba(255, 255, 255, 0.9);
        background: rgba(255, 255, 255, 0.05);
    }
    
    .stTabs [aria-selected="true"] {
        background: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    
    /* Input Fields */
    .stSelectbox label, .stSlider label, .stRadio label, .stFileUploader label {
        color: rgba(255, 255, 255, 0.85) !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Select boxes */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 12px !important;
        color: white !important;
    }
    
    .stSelectbox > div > div:hover {
        background: rgba(255, 255, 255, 0.12) !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
    }
    
    /* Slider */
    .stSlider > div > div > div {
        background: rgba(255, 255, 255, 0.1) !important;
    }
    
    .stSlider [role="slider"] {
        background: white !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Radio buttons */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.05);
        padding: 0.8rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .stRadio label {
        color: rgba(255, 255, 255, 0.85) !important;
    }
    
    /* Premium Button */
    .stButton > button {
        width: 100%;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: saturate(180%) blur(20px);
        -webkit-backdrop-filter: saturate(180%) blur(20px);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 1.2rem 3rem;
        font-size: 1.1rem;
        font-weight: 700;
        border-radius: 16px;
        box-shadow: 
            0 8px 24px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 1.5rem;
    }
    
    .stButton > button:hover {
        background: rgba(255, 255, 255, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.4);
        transform: translateY(-3px);
        box-shadow: 
            0 16px 40px rgba(0, 0, 0, 0.6),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    /* Metrics - Apple Style */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: saturate(180%) blur(15px);
        -webkit-backdrop-filter: saturate(180%) blur(15px);
        padding: 2rem 1.5rem;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 
            0 4px 16px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    div[data-testid="metric-container"]:hover {
        background: rgba(255, 255, 255, 0.12);
        transform: translateY(-2px);
        box-shadow: 
            0 8px 24px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.15);
    }
    
    div[data-testid="metric-container"] label {
        color: rgba(255, 255, 255, 0.7) !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }
    
    div[data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: white !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* File Uploader */
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        padding: 3rem;
        border-radius: 20px;
        border: 2px dashed rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"]:hover {
        background: rgba(255, 255, 255, 0.08);
        border: 2px dashed rgba(255, 255, 255, 0.5);
    }
    
    /* Alert boxes */
    .stSuccess, .stInfo, .stWarning {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
        padding: 1rem 1.5rem;
    }
    
    /* DataFrame */
    [data-testid="stDataFrame"] {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        overflow: hidden;
    }
    
    /* All text colors */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
        font-weight: 700 !important;
    }
    
    p, span, div, label {
        color: rgba(255, 255, 255, 0.9);
    }
    
    /* Download button */
    .stDownloadButton > button {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(20px);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 14px;
        font-weight: 700;
        padding: 1rem 2.5rem;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: white !important;
    }
    
    /* Model selector card */
    .model-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: saturate(180%) blur(20px);
        border-radius: 18px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 2rem;
        box-shadow: 
            0 8px 24px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# --- Load Model & Artifacts ---
@st.cache_resource
def load_model(model_name):
    model_filename_map = {
        'Linear Regression': 'linear_model.joblib',
        'Lasso Regression': 'lasso_model.joblib',
        'Ridge Regression': 'ridge_model.joblib',
        'Elastic Net': 'elastic_model.joblib'
    }
    model = joblib.load(model_filename_map[model_name])
    scaler = joblib.load('scaler.joblib')
    model_columns = joblib.load('model_columns.joblib')
    return model, scaler, model_columns

# --- Hero Header ---
st.markdown("""
    <div class="hero-header">
        <h1>💎 Salary Predictor</h1>
        <p>AI-Powered Income Intelligence with Premium Design</p>
        <div style='margin-top: 1.5rem; display: flex; gap: 2rem; justify-content: center; flex-wrap: wrap;'>
            <div style='text-align: center;'>
                <p style='font-size: 2.5rem; margin: 0;'>🎯</p>
                <p style='color: rgba(255,255,255,0.7); font-size: 0.9rem; margin: 0.5rem 0 0 0;'>Accurate Predictions</p>
            </div>
            <div style='text-align: center;'>
                <p style='font-size: 2.5rem; margin: 0;'>⚡</p>
                <p style='color: rgba(255,255,255,0.7); font-size: 0.9rem; margin: 0.5rem 0 0 0;'>Instant Results</p>
            </div>
            <div style='text-align: center;'>
                <p style='font-size: 2.5rem; margin: 0;'>🔒</p>
                <p style='color: rgba(255,255,255,0.7); font-size: 0.9rem; margin: 0.5rem 0 0 0;'>Multiple Models</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Model Selector ---
st.markdown('<div class="model-card">', unsafe_allow_html=True)
model_choice = st.selectbox(
    '🤖 Select Prediction Model',
    ('Linear Regression', 'Lasso Regression', 'Ridge Regression', 'Elastic Net')
)
st.markdown('</div>', unsafe_allow_html=True)

model, scaler, model_columns = load_model(model_choice)

# --- Prediction Function ---
def predict_salary(input_df):
    input_df = input_df.reindex(columns=model_columns, fill_value=0)
    scaled_input = scaler.transform(input_df)
    predictions = model.predict(scaled_input)
    return predictions

# --- Tabs ---
tab1, tab2 = st.tabs(["👤 Single Prediction", "📊 Bulk Prediction"])

# ==================== TAB 1: SINGLE PREDICTION ====================
with tab1:
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<p class="section-header">👤 Personal Information</p>', unsafe_allow_html=True)
        age = st.slider('Age', 18, 60, 30)
        gender = st.radio('Gender', ('Male', 'Female'), horizontal=True)
        marital_status = st.selectbox('Marital Status', ('Single', 'Married', 'Divorced'))
        distance_from_home = st.slider('Distance From Home (km)', 1, 29, 10)
        
        st.markdown('<p class="section-header">💼 Job Position</p>', unsafe_allow_html=True)
        department = st.selectbox('Department', ('Sales', 'Research & Development', 'Human Resources'))
        job_role = st.selectbox('Job Role', ('Sales Executive', 'Research Scientist', 'Laboratory Technician', 
                                              'Manufacturing Director', 'Healthcare Representative', 'Manager', 
                                              'Sales Representative', 'Research Director', 'Human Resources'))
        job_level = st.selectbox('Job Level', (1, 2, 3, 4, 5), index=1)
        overtime = st.radio('OverTime', ('No', 'Yes'), horizontal=True)
    
    with col2:
        st.markdown('<p class="section-header">🎓 Education</p>', unsafe_allow_html=True)
        education_field = st.selectbox('Field', ('Life Sciences', 'Medical', 'Marketing', 
                                                   'Technical Degree', 'Human Resources', 'Other'))
        education = st.selectbox('Level (1-5)', (1, 2, 3, 4, 5), index=2)
        
        st.markdown('<p class="section-header">📅 Experience</p>', unsafe_allow_html=True)
        total_working_years = st.slider('Total Working Years', 0, 40, 10)
        years_at_company = st.slider('Years at Company', 0, 40, 5)
        num_companies_worked = st.slider('Companies Worked', 0, 9, 2)
        business_travel = st.selectbox('Business Travel', ('Travel_Rarely', 'Travel_Frequently', 'Non-Travel'))
    
    with col3:
        st.markdown('<p class="section-header">📈 Performance</p>', unsafe_allow_html=True)
        performance_rating = st.selectbox('Performance Rating (1-4)', (1, 2, 3, 4), index=2)
        percent_salary_hike = st.slider('Salary Hike %', 11, 25, 15)
        job_involvement = st.selectbox('Job Involvement (1-4)', (1, 2, 3, 4), index=2)
        
        st.markdown('<p class="section-header">😊 Satisfaction</p>', unsafe_allow_html=True)
        environment_satisfaction = st.selectbox('Environment (1-4)', (1, 2, 3, 4), index=2)
        relationship_satisfaction = st.selectbox('Relationship (1-4)', (1, 2, 3, 4), index=2)
        work_life_balance = st.selectbox('Work-Life Balance (1-4)', (1, 2, 3, 4), index=2)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Prepare data
    data = {
        'Age': age, 'DistanceFromHome': distance_from_home, 'Education': education,
        'EnvironmentSatisfaction': environment_satisfaction, 'JobInvolvement': job_involvement,
        'JobLevel': job_level, 'NumCompaniesWorked': num_companies_worked,
        'PercentSalaryHike': percent_salary_hike, 'PerformanceRating': performance_rating,
        'RelationshipSatisfaction': relationship_satisfaction, 'TotalWorkingYears': total_working_years,
        'WorkLifeBalance': work_life_balance, 'YearsAtCompany': years_at_company,
        'BusinessTravel_Travel_Frequently': 1 if business_travel == 'Travel_Frequently' else 0,
        'BusinessTravel_Travel_Rarely': 1 if business_travel == 'Travel_Rarely' else 0,
        'Department_Research & Development': 1 if department == 'Research & Development' else 0,
        'Department_Sales': 1 if department == 'Sales' else 0,
        'EducationField_Human Resources': 1 if education_field == 'Human Resources' else 0,
        'EducationField_Life Sciences': 1 if education_field == 'Life Sciences' else 0,
        'EducationField_Marketing': 1 if education_field == 'Marketing' else 0,
        'EducationField_Medical': 1 if education_field == 'Medical' else 0,
        'EducationField_Other': 1 if education_field == 'Other' else 0,
        'EducationField_Technical Degree': 1 if education_field == 'Technical Degree' else 0,
        'Gender_Male': 1 if gender == 'Male' else 0,
        'JobRole_Human Resources': 1 if job_role == 'Human Resources' else 0,
        'JobRole_Laboratory Technician': 1 if job_role == 'Laboratory Technician' else 0,
        'JobRole_Manager': 1 if job_role == 'Manager' else 0,
        'JobRole_Manufacturing Director': 1 if job_role == 'Manufacturing Director' else 0,
        'JobRole_Research Director': 1 if job_role == 'Research Director' else 0,
        'JobRole_Research Scientist': 1 if job_role == 'Research Scientist' else 0,
        'JobRole_Sales Executive': 1 if job_role == 'Sales Executive' else 0,
        'JobRole_Sales Representative': 1 if job_role == 'Sales Representative' else 0,
        'MaritalStatus_Married': 1 if marital_status == 'Married' else 0,
        'MaritalStatus_Single': 1 if marital_status == 'Single' else 0,
        'OverTime_Yes': 1 if overtime == 'Yes' else 0,
    }
    input_df = pd.DataFrame(data, index=[0])
    
    if st.button("✨ PREDICT SALARY"):
        with st.spinner('Analyzing data...'):
            prediction = predict_salary(input_df)
            
            st.markdown('<div class="glass-container">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("💵 Monthly Income", f"${prediction[0]:,.2f}")
            with col2:
                st.metric("📅 Annual Income", f"${prediction[0]*12:,.2f}")
            with col3:
                st.metric("⏱️ Hourly Rate", f"${prediction[0]/160:,.2f}")
            
            st.markdown('</div>', unsafe_allow_html=True)

# ==================== TAB 2: BULK PREDICTION ====================
with tab2:
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📤 Upload CSV file with employee data",
        type=["csv"],
        help="Upload your employee dataset for batch predictions"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if uploaded_file is not None:
        df_original = pd.read_csv(uploaded_file)
        
        st.markdown('<div class="glass-container">', unsafe_allow_html=True)
        st.markdown('<p class="section-header">📊 Dataset Overview</p>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Rows", f"{len(df_original):,}")
        with col2:
            st.metric("Columns", len(df_original.columns))
        with col3:
            st.metric("Employees", len(df_original))
        with col4:
            st.metric("Features", len(df_original.columns))
        
        st.dataframe(df_original.head(10), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Visualizations
        if 'MonthlyIncome' in df_original.columns:
            st.markdown('<div class="glass-container">', unsafe_allow_html=True)
            st.markdown('<p class="section-header">📈 Data Insights</p>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig, ax = plt.subplots(figsize=(10, 5))
                fig.patch.set_alpha(0)
                ax.set_facecolor('none')
                sns.histplot(df_original['MonthlyIncome'], kde=True, color='#A29BFE', ax=ax, alpha=0.7)
                ax.set_title("Income Distribution", fontsize=14, color='white', fontweight='bold')
                ax.set_xlabel("Monthly Income ($)", color='white')
                ax.set_ylabel("Frequency", color='white')
                ax.tick_params(colors='white')
                for spine in ax.spines.values():
                    spine.set_color('rgba(255,255,255,0.3)')
                st.pyplot(fig)
            
            with col2:
                if 'JobLevel' in df_original.columns:
                    fig, ax = plt.subplots(figsize=(10, 5))
                    fig.patch.set_alpha(0)
                    ax.set_facecolor('none')
                    sns.boxplot(x='JobLevel', y='MonthlyIncome', data=df_original, 
                               palette='Blues', ax=ax)
                    ax.set_title("Income by Job Level", fontsize=14, color='white', fontweight='bold')
                    ax.set_xlabel("Job Level", color='white')
                    ax.set_ylabel("Monthly Income ($)", color='white')
                    ax.tick_params(colors='white')
                    for spine in ax.spines.values():
                        spine.set_color('rgba(255,255,255,0.3)')
                    st.pyplot(fig)
            st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("🚀 GENERATE PREDICTIONS"):
            with st.spinner('Processing predictions...'):
                predictions = predict_salary(df_original)
                df_original['Predicted_Monthly_Income'] = predictions
                df_original['Predicted_Annual_Income'] = predictions * 12
                
                st.markdown('<div class="glass-container">', unsafe_allow_html=True)
                st.success("✅ Predictions completed!")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("💵 Avg Salary", f"${predictions.mean():,.2f}")
                with col2:
                    st.metric("📈 Max Salary", f"${predictions.max():,.2f}")
                with col3:
                    st.metric("📉 Min Salary", f"${predictions.min():,.2f}")
                
                st.dataframe(df_original.head(20), use_container_width=True)
                
                csv = df_original.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="⬇️ DOWNLOAD RESULTS",
                    data=csv,
                    file_name="predicted_salaries.csv",
                    mime="text/csv",
                    use_container_width=True
                )
                st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; color: rgba(255,255,255,0.5); padding: 3rem; margin-top: 3rem;'>
        <p style='font-size: 0.9rem;'>✨ Premium Glassmorphic UI • Powered by AI</p>
    </div>
""", unsafe_allow_html=True)