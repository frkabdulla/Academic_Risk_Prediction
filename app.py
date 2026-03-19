import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Academic Risk System", layout="wide")

st.title("🎓 Academic Risk Prediction Dashboard")

st.markdown("### Student Performance Input")

col1, col2 = st.columns(2)

with col1:
    attendance = st.slider("Attendance (%)", 0, 100, 70)
    assignment = st.slider("Assignment Score", 0, 100, 60)

with col2:
    lms = st.slider("LMS Activity", 0, 100, 50)
    exam = st.slider("Exam Score", 0, 100, 65)

# Predict
if st.button("🔍 Predict Risk"):
    input_data = pd.DataFrame([[attendance, assignment, lms, exam]],
                              columns=["attendance", "assignment_score", "lms_activity", "exam_score"])
    
    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("✅ Low Risk Student")
    else:
        st.error("⚠️ High Risk Student")

    # Visualization
    st.markdown("### 📊 Student Performance Analysis")

    features = ["Attendance", "Assignment", "LMS", "Exam"]
    values = [attendance, assignment, lms, exam]

    fig, ax = plt.subplots()
    ax.bar(features, values)
    ax.set_ylabel("Score")
    ax.set_title("Student Performance Overview")

    st.pyplot(fig)

# Upload dataset
st.markdown("### 📂 Upload Student Dataset")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview:", df.head())

    predictions = model.predict(df)
    df["Risk"] = predictions

    st.markdown("### 🔍 Prediction Results")
    st.write(df)

    # Risk count visualization
    st.markdown("### 📊 Risk Distribution")

    risk_counts = df["Risk"].value_counts()

    fig2, ax2 = plt.subplots()
    ax2.pie(risk_counts, labels=["Low Risk", "High Risk"], autopct="%1.1f%%")
    ax2.set_title("Risk Distribution")

    st.pyplot(fig2)