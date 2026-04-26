import random
from datetime import datetime, timedelta

# =========================
# CONFIG
# =========================
event_types = [
    "command(360): ls -la",
    "command(360): cat /etc/passwd",
    "command(360): sudo rm -rf /tmp/test",
    "Analyzing file: /var/log/auth.log",
    "Analyzing file: /etc/shadow",
]

pid_values = ["3150", "3536", "4120", "5011", "6233"]

base_time = datetime.now()

# =========================
# GENERATE LOGS
# =========================
logs = []

for i in range(10):
    time = (base_time + timedelta(seconds=i * 5)).strftime("%Y/%m/%d %H:%M:%S")

    choice = random.choice(event_types)

    if "command" in choice:
        log = f"{time} wazuh-agent: {choice}"
    else:
        log = f"{time} wazuh-agent: {choice} Started (pid: {random.choice(pid_values)})"

    logs.append(log)

# =========================
# SAVE FILE
# =========================
with open("wazuh_test_logs.log", "w") as f:
    for log in logs:
        f.write(log + "\n")

print("✅ 10 Wazuh-like logs generated!")
print("📁 File: wazuh_test_logs.log")