# 🛡️ LendShield: AI-Driven Credit Risk Intelligence

LendShield is a professional-grade Credit Scoring System built to demonstrate the application of **Machine Learning** in financial risk assessment. Using a **Random Forest Classifier**, the system analyzes applicant data to provide instant loan approval decisions with a **92.4% accuracy rate**.

## 🚀 Interactive Demo
> **Live on GitHub Codespaces:** > 1. Click the green **"<> Code"** button.
> 2. Select the **Codespaces** tab and click **"Create codespace"**.
> 3. Once the terminal opens, run: `streamlit run app.py`

---

## 📊 Key Features
* **Predictive Underwriting:** Real-time probability scoring for loan repayment.
* **Interactive Radar Charts:** Visualizes applicant strengths (Income vs. Credit Score vs. Stability).
* **Market Benchmarking:** Compares individual applicants against 45,000+ historical records.
* **Responsive UI:** Built with Streamlit and Plotly for a modern, "Glassmorphism" FinTech experience.

---

## 🛠️ Tech Stack & Concepts
* **Language:** Python 3.14
* **Frontend:** Streamlit, Plotly (Interactive Charts)
* **Machine Learning:** Scikit-Learn (Random Forest, Pipelines, Standard Scaler)
* **Data Handling:** Pandas, NumPy
* **Deployment:** GitHub Codespaces / Streamlit Cloud



---

## 🧠 The Machine Learning Logic
The model evaluates creditworthiness based on several high-impact features:
1.  **Loan-to-Income Ratio:** The most critical factor in determining default risk.
2.  **Credit Score (FICO/CIBIL):** Historical financial reliability.
3.  **Employment Stability:** Years of work experience to gauge income consistency.
4.  **Previous Defaults:** A strong indicator of future repayment behavior.

The Random Forest algorithm was chosen for its ability to handle non-linear relationships and provide **Feature Importance** rankings, which are crucial for explainable AI in banking.

---

## 📂 Project Structure
```text
├── app.py                # Main Streamlit UI and Logic
├── best_loan_model.joblib # Serialized Random Forest Model
├── loan_data.csv         # Processed dataset for benchmarks
├── requirements.txt      # Library dependencies
└── README.md             # Project documentation



