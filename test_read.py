with open("wazuh_raw_logs.log", "r") as f:
    for i in range(5):
        print(f.readline().strip())