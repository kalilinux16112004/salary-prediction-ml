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

# --- Apple Glass UI CSS ---
st.markdown("""
    <style>
    /* Hide sidebar completely */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Remove sidebar space */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    /* Force main content to full width */
    .main .block-container {
        max-width: 100% !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
    }
    
    /* Hide any sidebar toggle button */
    button[kind="header"] {
        display: none !important;
    }
    
    /* Main background with gradient */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-attachment: fixed;
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 95%;
    }
    
    /* Glass card effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
    }
    
    /* Header glass card */
    .glass-header {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        padding: 3rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
        text-align: center;
    }
    
    .glass-header h1 {
        color: white;
        font-size: 3.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        letter-spacing: -1px;
    }
    
    .glass-header p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 0.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: white;
        border-radius: 10px;
        padding: 1rem 2rem;
        font-weight: 600;
        border: none;
    }
    
    .stTabs [aria-selected="true"] {
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
    }
    
    /* Input fields */
    .stSelectbox, .stSlider, .stRadio {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 0.5rem;
    }
    
    .stSelectbox label, .stSlider label, .stRadio label {
        color: white !important;
        font-weight: 600;
        font-size: 0.95rem;
    }
    
    /* Input backgrounds */
    input, select, [data-baseweb="select"] {
        background: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 10px !important;
        color: white !important;
    }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(20px);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.4);
        padding: 1rem 2rem;
        font-size: 1.2rem;
        font-weight: 700;
        border-radius: 15px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.35);
        transform: translateY(-3px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.3);
    }
    
    /* Metrics */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    div[data-testid="metric-container"] label {
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 600;
    }
    
    div[data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: white !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
    }
    
    /* File uploader */
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        padding: 3rem;
        border-radius: 20px;
        border: 2px dashed rgba(255, 255, 255, 0.5);
    }
    
    [data-testid="stFileUploader"] label {
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }
    
    /* Success/Info boxes */
    .stSuccess, .stInfo, .stWarning {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: white;
    }
    
    /* Dataframe */
    [data-testid="stDataFrame"] {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
        font-weight: 700 !important;
    }
    
    p, span, div {
        color: rgba(255, 255, 255, 0.95);
    }
    
    /* Download button */
    .stDownloadButton>button {
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(20px);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 15px;
        font-weight: 700;
        padding: 1rem 2rem;
    }
    
    .stDownloadButton>button:hover {
        background: rgba(255, 255, 255, 0.4);
        transform: translateY(-2px);
    }
    
    /* Model selector */
    .model-selector {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(20px);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: white !important;
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

# --- Header ---
st.markdown("""
    <div class="glass-header">
        <h1>💎 Salary Predictor</h1>
        <p>AI-Powered Income Prediction with Glassmorphic Design</p>
    </div>
""", unsafe_allow_html=True)

# --- Model Selector ---
st.markdown('<div class="model-selector">', unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])
with col1:
    model_choice = st.selectbox(
        '🤖 Select Prediction Model',
        ('Linear Regression', 'Lasso Regression', 'Ridge Regression', 'Elastic Net'),
        label_visibility="visible"
    )
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"**Active Model**")
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
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 👤 Personal")
        age = st.slider('Age', 18, 60, 30)
        gender = st.radio('Gender', ('Male', 'Female'), horizontal=True)
        marital_status = st.selectbox('Marital Status', ('Single', 'Married', 'Divorced'))
        distance_from_home = st.slider('Distance From Home (km)', 1, 29, 10)
        
        st.markdown("#### 💼 Position")
        department = st.selectbox('Department', ('Sales', 'Research & Development', 'Human Resources'))
        job_role = st.selectbox('Job Role', ('Sales Executive', 'Research Scientist', 'Laboratory Technician', 
                                              'Manufacturing Director', 'Healthcare Representative', 'Manager', 
                                              'Sales Representative', 'Research Director', 'Human Resources'))
        job_level = st.selectbox('Job Level', (1, 2, 3, 4, 5), index=1)
        overtime = st.radio('OverTime', ('No', 'Yes'), horizontal=True)
    
    with col2:
        st.markdown("#### 🎓 Education")
        education_field = st.selectbox('Field', ('Life Sciences', 'Medical', 'Marketing', 
                                                   'Technical Degree', 'Human Resources', 'Other'))
        education = st.selectbox('Level (1-5)', (1, 2, 3, 4, 5), index=2)
        
        st.markdown("#### 📅 Experience")
        total_working_years = st.slider('Total Working Years', 0, 40, 10)
        years_at_company = st.slider('Years at Company', 0, 40, 5)
        num_companies_worked = st.slider('Companies Worked', 0, 9, 2)
        business_travel = st.selectbox('Business Travel', ('Travel_Rarely', 'Travel_Frequently', 'Non-Travel'))
    
    with col3:
        st.markdown("#### 📈 Performance")
        performance_rating = st.selectbox('Performance Rating (1-4)', (1, 2, 3, 4), index=2)
        percent_salary_hike = st.slider('Salary Hike %', 11, 25, 15)
        job_involvement = st.selectbox('Job Involvement (1-4)', (1, 2, 3, 4), index=2)
        
        st.markdown("#### 😊 Satisfaction")
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
    
    if st.button("✨ PREDICT SALARY", use_container_width=True):
        with st.spinner('Analyzing data...'):
            prediction = predict_salary(input_df)
            
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("💵 Monthly Income", f"${prediction[0]:,.2f}")
            with col2:
                st.metric("📅 Annual Income", f"${prediction[0]*12:,.2f}")
            with col3:
                st.metric("📊 Hourly Rate", f"${prediction[0]/160:,.2f}")
            
            st.markdown('</div>', unsafe_allow_html=True)

# ==================== TAB 2: BULK PREDICTION ====================
with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📤 Upload CSV file with employee data",
        type=["csv"],
        help="Upload your employee dataset for batch predictions"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if uploaded_file is not None:
        df_original = pd.read_csv(uploaded_file)
        
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Dataset Overview")
        
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
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("### 📈 Data Insights")
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig, ax = plt.subplots(figsize=(10, 5), facecolor='none')
                ax.set_facecolor('none')
                sns.histplot(df_original['MonthlyIncome'], kde=True, color='white', ax=ax, alpha=0.7)
                ax.set_title("Income Distribution", fontsize=14, color='white', fontweight='bold')
                ax.set_xlabel("Monthly Income ($)", color='white')
                ax.set_ylabel("Frequency", color='white')
                ax.tick_params(colors='white')
                ax.spines['bottom'].set_color('white')
                ax.spines['left'].set_color('white')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                st.pyplot(fig)
            
            with col2:
                if 'JobLevel' in df_original.columns:
                    fig, ax = plt.subplots(figsize=(10, 5), facecolor='none')
                    ax.set_facecolor('none')
                    sns.boxplot(x='JobLevel', y='MonthlyIncome', data=df_original, 
                               palette='Pastel1', ax=ax)
                    ax.set_title("Income by Job Level", fontsize=14, color='white', fontweight='bold')
                    ax.set_xlabel("Job Level", color='white')
                    ax.set_ylabel("Monthly Income ($)", color='white')
                    ax.tick_params(colors='white')
                    ax.spines['bottom'].set_color('white')
                    ax.spines['left'].set_color('white')
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)
                    st.pyplot(fig)
            st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("🚀 GENERATE PREDICTIONS", use_container_width=True):
            with st.spinner('Processing predictions...'):
                predictions = predict_salary(df_original)
                df_original['Predicted_Monthly_Income'] = predictions
                df_original['Predicted_Annual_Income'] = predictions * 12
                
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
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
    <div style='text-align: center; color: rgba(255,255,255,0.8); padding: 3rem; margin-top: 2rem;'>
        <p style='font-size: 0.9rem;'>✨ Designed with Apple's Glassmorphic UI | Powered by AI</p>
    </div>
""", unsafe_allow_html=True)