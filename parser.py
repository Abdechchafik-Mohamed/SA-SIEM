import pandas as pd

# =========================
# YOUR EXISTING LOGIC
# =========================
def parse_line(line):
    line = line.strip()

    # COMMAND EVENT
    if "command(360)" in line:
        return {
            "timestamp": line[:19],
            "event_type": "command",
            "command": line.split("command(360):")[-1].strip(),
            "file": None,
            "pid": None
        }

    # FILE ANALYSIS EVENT
    elif "Analyzing file:" in line:
        return {
            "timestamp": line[:19],
            "event_type": "analysis",
            "command": None,
            "file": line.split("Analyzing file:")[-1].strip(),
            "pid": None
        }

    # START EVENT
    elif "Started (pid:" in line:
        pid = line.split("pid:")[-1].replace(")", "").strip()
        return {
            "timestamp": line[:19],
            "event_type": "start",
            "command": None,
            "file": None,
            "pid": pid
        }

    return None


def parse_file(file_path):
    parsed = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            result = parse_line(line)
            if result:
                parsed.append(result)

    return parsed


# =========================
# MAIN EXECUTION
# =========================
if __name__ == "__main__":

    log_file = "wazuh_test_logs.log"

    print("🚀 Parsing Wazuh logs...")

    data = parse_file(log_file)

    # =========================
    # CONVERT TO DATAFRAME
    # =========================
    df = pd.DataFrame(data)

    # =========================
    # CLEANING
    # =========================
    if df.empty:
        print("❌ No logs parsed. Check format.")
    else:
        df.fillna("null", inplace=True)

        # =========================
        # SAVE OUTPUT FOR FEATURE ENGINEERING
        # =========================
        df.to_csv("parsed_logs.csv", index=False)

        print("✅ parsed_logs.csv created successfully!")
        print(f"📊 Total events parsed: {len(df)}")
        print(df.head())