import pandas as pd
import pickle
import shutil
import os
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

print("📂 Current working directory:", os.getcwd())

# Load sample data
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
X = data.drop("species", axis=1)
y = data["species"].astype("category").cat.codes

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
model.fit(X_train, y_train)

# Save model
# model_path = "/app/model.pkl"  # Save to top-level app folder
model_path = "model.pkl"  # Save to top-level app folder/
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Model trained and saved to: {model_path}")
