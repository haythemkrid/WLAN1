import subprocess
import re
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.animation import FuncAnimation

def current_wifi_signal():
    # Run the iwconfig command to get Wi-Fi details
    result1 = subprocess.run("iwconfig", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out1 = result1.stdout.decode("utf-8", errors="ignore")

    # Extract ESSID from iwconfig output
    m1 = re.findall(r'ESSID:"(.*?)"', out1, re.DOTALL)
    if len(m1) == 1:
        ESSID = m1[0]

        # Run nmcli to get signal strength of the connected Wi-Fi
        result2 = subprocess.run("nmcli dev wifi | grep '*'", shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        out2 = result2.stdout.decode("utf-8", errors="ignore")

        # Extract BSSID, Mode, Channel, Rate, Signal, and Security
        m2 = re.findall(
            r'\* *(\S+) *{} *(\S+) *(\d+) *([\d.]+ [a-zA-Z/]+) *(\d+) *[^ ]* *(.*)'.format(re.escape(ESSID)), out2)

        if m2:
            bssid, mode, channel, rate, signal_power, security = m2[0]
            security = security.strip()
            return int(signal_power), ESSID

    # If not connected to any Wi-Fi network
    return 0, 'Not connected to any access point'


plt.style.use("fivethirtyeight")
x_vals = []
y_vals = []



fig=plt.figure()

def animate(frame):
    signal, ESSID = current_wifi_signal()
    x_vals.append(datetime.now())
    y_vals.append(signal)
    plt.cla()
    plt.plot(x_vals[-20:], y_vals[-20:])
    plt.autoscale(enable=True, axis='y', tight=True)
    plt.title(ESSID)

animation = FuncAnimation(fig, animate, interval=500)
plt.tight_layout()
plt.show()
