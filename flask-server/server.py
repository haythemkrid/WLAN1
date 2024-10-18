from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import re
import threading
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for the Flask app

class APTracker():
    def __init__(self):
        self.APs = []

    def fetch_APs(self):
        while True:
            try:
                # Run the nmcli command to fetch Wi-Fi access points
                result = subprocess.run("nmcli dev wifi", shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)
                # Decode the output
                out = result.stdout.decode("utf-8", errors="ignore")
                l1 = out.split("\n")

                if len(l1) > 1:
                    propslength = dict()
                    props = l1[0]
                    m = re.findall("(IN-USE *)(BSSID *)(SSID *)(MODE *)(CHAN *)(RATE *)(SIGNAL *)(BARS *)(SECURITY *)",
                                   props, re.DOTALL)

                    if m:
                        for prop in m[0]:
                            propslength[prop.strip()] = len(prop)

                        self.APs = []  # Clear previous results
                        for ap in l1[1:]:
                            if ap:
                                AP = dict()
                                for prop, length in propslength.items():
                                    AP[prop] = ap[:length].strip()
                                    ap = ap[length:]
                                self.APs.append(AP)

                    else:
                        print("No matches found in the properties header.")  # Debug info

                else:
                    print("No access points found.")  # Debug info

            except Exception as e:
                print(f"Error fetching APs: {e}")  # Handle and log exceptions
            time.sleep(1)  # Wait for 1 second before fetching again

apt = APTracker()
def background_fetch():
    apt.fetch_APs()

threading.Thread(target=background_fetch, daemon=True).start()

@app.route("/PickYourWifi")
def PickYourWifi():
    return jsonify(apt.APs)

if __name__ == "__main__":
    app.run(debug=True)  # Corrected line
