import subprocess
import pandas as pd
import time
import os

LOG_FILE = "../data/wifi_log.csv"

def scan_wifi():
    result = subprocess.check_output(["iwlist", "wlan0", "scan"]).decode("utf-8")
    cells = result.split("Cell")
    wifi_data = []

    for cell in cells[1:]:
        ssid_line = next((line for line in cell.split("\n") if "ESSID" in line), None)
        if ssid_line:
            ssid = ssid_line.split(":")[1].replace('"','')
            signal_line = next((line for line in cell.split("\n") if "Signal level" in line), None)
            bssid_line = next((line for line in cell.split("\n") if "Address" in line), None)
            if signal_line and bssid_line:
                signal = int(signal_line.split("=")[2].split(" ")[0])
                bssid = bssid_line.split("Address: ")[1]
                wifi_data.append({"SSID": ssid, "BSSID": bssid, "RSSI": signal, "Timestamp": time.time()})
    return wifi_data

def log_data():
    if not os.path.exists(LOG_FILE):
        pd.DataFrame(columns=["SSID", "BSSID", "RSSI", "Timestamp"]).to_csv(LOG_FILE, index=False)

    try:
        while True:
            scan = scan_wifi()
            df = pd.DataFrame(scan)
            df.to_csv(LOG_FILE, mode='a', header=False, index=False)
            print(f"{len(scan)} redes registadas.")
            time.sleep(10)
    except KeyboardInterrupt:
        print("Paragem manual do scan.")

if __name__ == "__main__":
    log_data()

