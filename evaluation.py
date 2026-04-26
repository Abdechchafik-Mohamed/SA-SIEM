import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix, classification_report

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("features.csv")

X = df.select_dtypes(include=["number"])

# =========================
# CREATE PSEUDO LABELS
# (based on simple rule)
# =========================
df["true_label"] = (df["event_count"] > 40).astype(int)

# =========================
# TRAIN MODEL
# =========================
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

y_pred = model.predict(X)
y_pred = [0 if x == 1 else 1 for x in y_pred]
# =========================
# CONFUSION MATRIX
# =========================
cm = confusion_matrix(df["true_label"], y_pred)

print(" Confusion Matrix:")
print(cm)
