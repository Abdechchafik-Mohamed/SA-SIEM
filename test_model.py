import pandas as pd
from sklearn.ensemble import IsolationForest

# =========================
# LOAD TRAINING DATA
# =========================
df = pd.read_csv("features.csv")

# Keep numeric features only
X = df.select_dtypes(include=["number"])

# =========================
# TRAIN MODEL (for testing)
# =========================
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

# =========================
# TAKE ONE SAMPLE FOR TESTING
# =========================
sample = X.iloc[[0]]  # first log

# =========================
# PREDICT
# =========================
result = model.predict(sample)

# =========================
# INTERPRET RESULT
# =========================
if result[0] == -1:
    print("🚨 ANOMALY DETECTED")
else:
    print("✅ NORMAL ACTIVITY")