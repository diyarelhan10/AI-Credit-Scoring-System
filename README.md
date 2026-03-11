# 🛡️ LendShield: AI-Driven Credit Risk Intelligence

LendShield is a professional-grade Credit Scoring System built to demonstrate the application of **Machine Learning** in financial risk assessment. Using a **Random Forest Classifier**, the system analyzes applicant data to provide instant loan approval decisions with a **92.4% accuracy rate**.

## 🌐 Live Deployment
**Access the production app here:** 👉 **[LendShield Web Dashboard](https://ai-credit-scoring-system-erlppk4ny6jutxsfttwjka.streamlit.app/)**

---

## 🚀 Interactive Demo (Development Mode)
To run this project in a development environment:

1. **GitHub Codespaces:** * Click the green **"<> Code"** button.
   * Select the **Codespaces** tab and click **"Create codespace"**.
   * Once the terminal opens, run: `streamlit run app.py`

2. **Local Machine:**
   * Clone the repo: `git clone <your-repo-url>`
   * Install dependencies: `pip install -r requirements.txt`
   * Run the app: `streamlit run app.py`

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
* **Deployment:** Streamlit Cloud / GitHub Codespaces 

---

## 🧠 The Machine Learning Logic
The model evaluates creditworthiness based on several high-impact features:
1. **Loan-to-Income Ratio:** The most critical factor in determining default risk.
2. **Credit Score (FICO/CIBIL):** Historical financial reliability.
3. **Employment Stability:** Years of work experience to gauge income consistency.
4. **Previous Defaults:** A strong indicator of future repayment behavior.



[Image of random forest classifier diagram]


The **Random Forest** algorithm was chosen for its ability to handle non-linear relationships and provide **Feature Importance** rankings, which are crucial for explainable AI in banking.

---

## 📂 Project Structure
```text
├── app.py                # Main Streamlit UI and Logic
├── best_loan_model.joblib # Serialized Random Forest Model
├── loan_data.csv         # Processed dataset for benchmarks
├── requirements.txt      # Library dependencies
└── README.md             # Project documentation
