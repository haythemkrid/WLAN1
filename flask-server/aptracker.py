import subprocess
import re
import json  # Import the JSON module


class APTracker():
    def __init__(self):
        self.APs = []
        self.JSONval= {}

    def fetch_APs(self):
        result = subprocess.run("nmcli dev wifi", shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        out = result.stdout.decode("utf-8", errors="ignore")
        l1 = out.split("\n")

        if len(l1) > 1:
            propslength = dict()
            props = l1[0]
            m = re.findall("(IN-USE *)(BSSID *)(SSID *)(MODE *)(CHAN *)(RATE *)(SIGNAL *)(BARS *)(SECURITY *)", props, re.DOTALL)
            for prop in m[0]:
                propslength[prop.strip()] = len(prop)
            for ap in l1[1:]:
                if ap:
                    AP = dict()
                    for prop, length in propslength.items():
                        AP[prop] = ap[:length].strip()
                        ap = ap[length:]
                    self.APs.append(AP)







