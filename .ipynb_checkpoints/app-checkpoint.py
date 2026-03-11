import streamlit as st
import pandas as pd
import joblib
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LendShield AI | Credit Scoring",
    page_icon="💳",
    layout="wide"
)

# Custom CSS for a modern "FinTech" look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #2e7d32; color: white; font-weight: bold; }
    .stNumberInput, .stSelectbox { border-radius: 8px; }
    h1 { color: #1b5e20; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOAD THE TRAINED MODEL ---
@st.cache_resource
def load_model():
    # This matches the filename from your Jupyter Notebook
    return joblib.load('best_loan_model.joblib')

model = load_model()

# --- 3. HEADER SECTION ---
st.title("💳 LendShield: AI Credit Risk Assessment")
st.markdown("### Decision Support System for Loan Approval")
st.info("Fill in the applicant details below to evaluate the credit risk in real-time.")

# --- 4. USER INPUT FORM ---
# We split the screen into 3 columns for a better UI
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("👤 Applicant Profile")
    age = st.number_input("Age", 18, 95, 30)
    gender = st.selectbox("Gender", ["male", "female"])
    education = st.selectbox("Education Level", ["High School", "Bachelor", "Master", "Associate", "Doctorate"])
    home_ownership = st.selectbox("Home Ownership", ["RENT", "OWN", "MORTGAGE", "OTHER"])

with col2:
    st.subheader("💰 Financial Status")
    income = st.number_input("Annual Income ($)", 0, 10000000, 55000)
    emp_exp = st.number_input("Work Experience (Years)", 0, 50, 5)
    credit_score = st.slider("Credit Score (CIBIL/FICO Equivalent)", 300, 850, 650)
    history_length = st.number_input("Credit History Length (Years)", 0, 40, 4)

with col3:
    st.subheader("🏥 Loan Details")
    loan_amnt = st.number_input("Requested Loan Amount ($)", 500, 100000, 10000)
    intent = st.selectbox("Loan Purpose", ["EDUCATION", "MEDICAL", "VENTURE", "PERSONAL", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"])
    interest_rate = st.slider("Interest Rate (%)", 5.0, 25.0, 11.5)
    defaults = st.selectbox("Previous Defaults on Record?", ["No", "Yes"])

# Feature Calculation (Matches what we did in training)
loan_percent_income = loan_amnt / income if income > 0 else 0

# --- 5. PREDICTION LOGIC ---
st.markdown("---")
if st.button("RUN AI RISK ANALYSIS"):
    # Prepare data for model
    data = pd.DataFrame([{
        'person_age': age, 'person_gender': gender, 'person_education': education,
        'person_income': income, 'person_emp_exp': emp_exp, 'person_home_ownership': home_ownership,
        'loan_amnt': loan_amnt, 'loan_intent': intent, 'loan_int_rate': interest_rate,
        'loan_percent_income': loan_percent_income, 'cb_person_cred_hist_length': history_length,
        'credit_score': credit_score, 'previous_loan_defaults_on_file': defaults
    }])

    # Animated processing
    with st.spinner('Accessing risk parameters and model weights...'):
        time.sleep(1.5)
        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)[0]

    # --- 6. DISPLAY RESULTS ---
    res_col1, res_col2 = st.columns([1, 2])
    
    with res_col1:
        if prediction == 0:
            st.success("### ✅ LOAN APPROVED")
            st.balloons()
        else:
            st.error("### ❌ LOAN REJECTED")
            st.warning("Risk level exceeds internal threshold.")

    with res_col2:
        # Show Probability Gauge/Score
        approval_prob = round(probability[0] * 100, 2)
        st.metric(label="Repayment Probability Score", value=f"{approval_prob}%")
        st.progress(approval_prob / 100)
        st.caption("A probability score above 75% is typically required for standard approval.")