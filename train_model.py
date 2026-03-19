import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

print("🔹 Starting model training...")

# Check file exists
if not os.path.exists("data.csv"):
    print("❌ ERROR: data.csv not found")
    exit()

# Load dataset
try:
    data = pd.read_csv("data.csv")
    print("✅ Data loaded successfully")
    print(data.head())
except Exception as e:
    print("❌ Error loading data:", e)
    exit()

# Check columns
if "risk" not in data.columns:
    print("❌ ERROR: 'risk' column missing")
    exit()

# Prepare data
X = data.drop("risk", axis=1)
y = data["risk"]

print("✅ Features and target prepared")

# Train model
try:
    model = RandomForestClassifier()
    model.fit(X, y)
    print("✅ Model trained")
except Exception as e:
    print("❌ Error during training:", e)
    exit()

# Save model
try:
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("✅ Model saved as model.pkl")
except Exception as e:
    print("❌ Error saving model:", e)