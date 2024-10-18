import subprocess
import re


class APTracker():
    def __init__(self):
        self.APs = []

    def fetch_APs(self):
        result = subprocess.run("nmcli dev wifi", shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        out = result.stdout.decode("utf-8", errors="ignore")
        l1 = out.split("\n")
        if len(l1)  > 1:
            propslength=dict()
            props=l1[0]
            m = re.findall("(IN-USE *)(BSSID *)(SSID *)(MODE *)(CHAN *)(RATE *)(SIGNAL *)(BARS *)(SECURITY *)",props,re.DOTALL)
            for prop in m[0]:
                propslength[prop.strip()]=len(prop)
            for ap in l1[1:]:
                if ap:
                    AP=dict()
                    for prop, length in propslength.items():
                        AP[prop]=ap[:length].strip()
                        ap=ap[length:]
                    self.APs.append(AP)

    def format_AP(self,ap):
        ch=f"SSID: {ap['SSID']}\n"+"\n".join(["   "+i+": "+j for i,j in ap.items() if i!="SSID"])
        ch=ch+'\n____________________'
        return ch
    def show_APs(self):
        for AP in self.APs:
            print(self.format_AP(AP))

apt = APTracker()
apt.fetch_APs()
apt.show_APs()