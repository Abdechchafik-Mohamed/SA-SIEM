import pandas as pd

# =========================
# LOAD PARSED DATA
# =========================
df = pd.read_csv("parsed_logs.csv")

# =========================
# CLEAN
# =========================
# Separate handling by type

# numeric columns → fill with 0
num_cols = df.select_dtypes(include=["number"]).columns
df[num_cols] = df[num_cols].fillna(0)

# categorical columns → fill with "unknown"
cat_cols = df.select_dtypes(include=["object"]).columns
df[cat_cols] = df[cat_cols].fillna("unknown")

# =========================
# FEATURE 1: EVENT FREQUENCY
# =========================
df["event_count"] = df.groupby("event_type")["event_type"].transform("count")

# =========================
# FEATURE 2: PID ACTIVITY (PROCESS BEHAVIOR)
# =========================
df["pid_count"] = df.groupby("pid")["pid"].transform("count")

# =========================
# FEATURE 3: COMMAND USAGE FREQUENCY
# =========================
df["command_used"] = df["command"].apply(lambda x: 1 if x != "null" else 0)

df["command_count"] = df.groupby("command")["command"].transform("count")

# =========================
# FEATURE 4: FILE ACCESS FREQUENCY
# =========================
df["file_used"] = df["file"].apply(lambda x: 1 if x != "null" else 0)

df["file_count"] = df.groupby("file")["file"].transform("count")

# =========================
# FEATURE 5: EVENT TYPE ENCODING
# =========================
df["event_type_encoded"] = df["event_type"].astype("category").cat.codes

# =========================
# FINAL DATASET FOR ML
# =========================
features = df[[
    "event_count",
    "pid_count",
    "command_used",
    "command_count",
    "file_used",
    "file_count",
    "event_type_encoded"
]]

# =========================
# SAVE OUTPUT
# =========================
features.to_csv("features.csv", index=False)

print("✅ Feature extraction completed (PROCESS-BASED SIEM)")
print("📁 Saved: features.csv")