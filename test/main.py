import os

print("🚀 SA-SIEM Pipeline Starting...\n")

# =========================
# STEP 1: PARSING
# =========================
print("[1] Running parser...")
exit_code = os.system("python3 parser.py")

if exit_code != 0:
    print("❌ Parser failed. Stopping pipeline.")
    exit()

print("✅ Parsing completed.\n")

# =========================
# STEP 2: FEATURE ENGINEERING
# =========================
print("[2] Running feature extraction...")
exit_code = os.system("python3 feature_engineering.py")

if exit_code != 0:
    print("❌ Feature engineering failed. Stopping pipeline.")
    exit()

print("✅ Feature extraction completed.\n")

# =========================
# STEP 3: MODEL TRAINING + DETECTION
# =========================
print("[3] Running anomaly detection model...")
exit_code = os.system("python3 model.py")

if exit_code != 0:
    print("❌ Model execution failed. Stopping pipeline.")
    exit()

print("Model executed successfully.\n")
