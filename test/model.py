import pandas as pd
from sklearn.ensemble import IsolationForest

# =========================
# LOAD FEATURES
# =========================
df = pd.read_csv("features.csv")

print("Training Isolation Forest model...")

# =========================
# SELECT FEATURES (NO LABEL USED)
# =========================
# Use only numeric feature columns
X = df.select_dtypes(include=["number"])

# =========================
# TRAIN MODEL
# =========================
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,  # expected % of anomalies
    random_state=42
)

model.fit(X)

# =========================
# PREDICTION
# =========================
df["anomaly"] = model.predict(X)

# Convert:
# -1 = anomaly
#  1 = normal
df["anomaly"] = df["anomaly"].map({1: 0, -1: 1})

# =========================
# SCORE (OPTIONAL)
# =========================
df["anomaly_score"] = model.decision_function(X)

# =========================
# SAVE RESULTS
# =========================
df.to_csv("output/detections.csv", index=False)

print("Model training completed!")
print("Anomalies detected:", df["anomaly"].sum())
print("Saved: output/detections.csv")