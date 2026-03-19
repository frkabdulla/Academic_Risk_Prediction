# 🎓 AI-Powered Academic Risk Prediction System

## 📌 Overview

This project presents an AI-based real-time academic risk prediction system designed to identify at-risk students and support timely faculty intervention. The system analyzes student performance indicators such as attendance, assignment scores, LMS activity, and examination results to predict academic risk levels.

---

## 🚀 Features

* Real-time academic risk prediction
* Machine learning-based classification
* Interactive Streamlit dashboard
* Student data upload (CSV support)
* Visual analytics (graphs and charts)
* Faculty decision-support system

---

## 🧠 Problem Statement

Academic risk is often identified only after examination results, which delays intervention and reduces opportunities for improvement. This system provides an early warning mechanism using AI to enhance student success outcomes.

---

## ⚙️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Matplotlib

---

## 📂 Project Structure

```
Academic_Risk_Prediction/
│
├── app.py
├── train_model.py
├── data.csv
├── model.pkl
├── students_test.csv
└── README.md
```

---

## 📊 Dataset Description

| Feature          | Description                                   |
| ---------------- | --------------------------------------------- |
| attendance       | Percentage of classes attended                |
| assignment_score | Average assignment performance                |
| lms_activity     | LMS engagement level                          |
| exam_score       | Examination performance                       |
| risk             | Target variable (0 = Low Risk, 1 = High Risk) |

---

## 🧪 How to Run the Project

### Step 1: Clone the Repository

```
git clone https://github.com/your-username/Academic_Risk_Prediction.git
cd Academic_Risk_Prediction
```

---

### Step 2: Install Dependencies

```
python -m pip install streamlit pandas scikit-learn matplotlib
```

---

### Step 3: Train the Model

```
python train_model.py
```

This will generate:

```
model.pkl
```

---

### Step 4: Run the Application

```
python -m streamlit run app.py
```

---

### Step 5: Open in Browser

```
http://localhost:8501
```

---

## 📂 CSV Upload Format

The CSV file must contain the following columns:

```
attendance,assignment_score,lms_activity,exam_score
```

### Example:

```
85,78,60,80
40,30,20,35
```

---

## 🎯 Output

* Predicts student academic risk
* Risk levels:

  * 0 → Low Risk
  * 1 → High Risk
* Provides visual dashboard for analysis

---

## 📌 Future Enhancements

* Medium risk classification (Low / Medium / High)
* Explainable AI (feature importance visualization)
* Integration with institutional LMS systems
* Cloud deployment for real-time access

---

## 👨‍🏫 Author

**Prof. Md Faruk Abdulla**
Assistant Professor, IT & CS
Parul University, Vadodara

---

## 📢 Contribution

Contributions, suggestions, and improvements are welcome.

---

## ⭐ Acknowledgment

This project is developed as part of research on AI-based student success systems and decision-support frameworks.
