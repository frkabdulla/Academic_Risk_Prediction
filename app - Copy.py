import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 Academic Risk Prediction System")

st.write("Enter student details")

attendance = st.slider("Attendance (%)", 0, 100, 70)
assignment = st.slider("Assignment Score", 0, 100, 60)
lms = st.slider("LMS Activity", 0, 100, 50)
exam = st.slider("Exam Score", 0, 100, 65)

if st.button("Predict Risk"):
    input_data = pd.DataFrame([[attendance, assignment, lms, exam]],
                              columns=["attendance", "assignment_score", "lms_activity", "exam_score"])

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("✅ Low Risk Student")
    else:
        st.error("⚠️ High Risk Student")

st.subheader("Upload CSV File")

uploaded_file = st.file_uploader("Upload student data", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    preds = model.predict(df)
    df["Risk"] = preds
    st.write(df)