import subprocess
import re

def read_current_signal():
    wifi = {}  # Dictionary to store Wi-Fi info

    # Run the iwconfig command to get Wi-Fi details
    result1 = subprocess.run("iwconfig", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out1 = result1.stdout.decode("utf-8", errors="ignore")

    # Extract ESSID, Frequency, and Signal Level
    m1 = re.findall(r'ESSID:"(.*?)".*?Frequency:([0-9.]+).*?Signal level=(-?\d+) dBm', out1, re.DOTALL)

    if not m1:
        print("No Wi-Fi network found in iwconfig output.")
        return

    wifi_name, frequency, signal_level = m1[0]

    # Run nmcli to get more detailed Wi-Fi info
    result2 = subprocess.run("nmcli dev wifi | grep '*'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out2 = result2.stdout.decode("utf-8", errors="ignore")

    # Extract BSSID, Mode, Channel, Rate, Signal, and Security
    m2 = re.findall(r'\* *(\S+) *{} *(\S+) *(\d+) *([\d.]+ [a-zA-Z/]+) *(\d+) *[^ ]* *(.*)'.format(re.escape(wifi_name)), out2)

    if not m2:
        print(f"No matching Wi-Fi network found for {wifi_name} in nmcli output.")
        return

    bssid, mode, channel, rate, signal_power, security = m2[0]
    security = security.strip()

    # Store values in the dictionary
    wifi["SSID"] = wifi_name
    wifi["Frequency"] = frequency
    wifi["Signal Level (dBm)"] = signal_level
    wifi["BSSID"] = bssid
    wifi["Mode"] = mode
    wifi["Channel"] = channel
    wifi["Rate"] = rate
    wifi["Signal Power"] = signal_power
    wifi["Security"] = security

    # Print the extracted data
    for key, value in wifi.items():
        print(f"{key}: {value}")

# Run the function
read_current_signal()
