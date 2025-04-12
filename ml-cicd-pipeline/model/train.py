import pandas as pd
import pickle
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

# Load sample data
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
X = data.drop("species", axis=1)
y = data["species"]

# Encode target
y = y.astype('category').cat.codes

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved")