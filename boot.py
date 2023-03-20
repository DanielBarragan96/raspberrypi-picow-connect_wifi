import network
import urequests
import os
import sys

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    wlan.connect(os.environ['SSID'], os.environ['PASSWORD'])
    print("wlan is connected" if wlan.isconnected() else "wlan error")

astronauts = urequests.get("http://api.open-notify.org/astros.json").json()
number = astronauts['number']
for i in range(number):
    print(astronauts['people'][i]['name'])

