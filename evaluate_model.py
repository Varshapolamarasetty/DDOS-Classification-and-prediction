import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from xgboost import XGBClassifier

# Load dataset
df = pd.read_csv("new_traffic.csv")

# Drop unnecessary columns
drop_cols = ['Unnamed: 0', 'Flow ID', 'Source', 'Source Port', 'Destination', 'Destination Port', 'Timestamp']
df = df.drop(columns=drop_cols, errors='ignore')

# Drop null values
df = df.dropna()

# Encode labels if necessary
le = LabelEncoder()
if df['Label'].dtype == 'object':
    df['Label'] = le.fit_transform(df['Label'])  # e.g., 'Syn' -> 1, 'Normal' -> 0

# Split into features and target
X = df.drop('Label', axis=1)
y = df['Label']

# Handle inf and NaNs in features
X.replace([np.inf, -np.inf], np.nan, inplace=True)
X.dropna(inplace=True)
y = y[X.index]  # Keep alignment

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Print unique classes to debug
print("Classes in y_train:", np.unique(y_train))

# Final XGBoost model setup
model = XGBClassifier(
    objective='binary:logistic',
    base_score=0.5,  # safe default
    use_label_encoder=False,
    eval_metric='logloss'
)

# Fit the model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# If you used label encoding
if 'le' in locals():
    print("\n📄 Classification Report:\n", classification_report(y_test, y_pred, target_names=le.classes_))
else:
    print("\n📄 Classification Report:\n", classification_report(y_test, y_pred))
