#!/bin/env python
import time
from datetime import datetime

from CO2Meter import *
from zabbix_utils import Sender, ItemValue

HOSTNAME = 'CO2 Meter'
ZABBIX_SERVER = '127.0.0.1'
count = 5

Meter = None

# Get Co2 meter instance and wait data stability
try:
    Meter = CO2Meter("/dev/hidraw0")
    time.sleep(3)
except Exception as e:
    print("Error: cannot read CO2 Meter.")
    print(e)
    exit(1)

while count > 0:
    # Get co2data and check data
    co2data = Meter.get_data()
    if 'temperature' not in co2data or 'co2' not in co2data:
        time.sleep(1)
        count = count - 1
        continue

    # Send data to zabbix
    items = [
        ItemValue(HOSTNAME, 'co2mini.temperature', co2data['temperature']),
        ItemValue(HOSTNAME, 'co2mini.co2', co2data['co2'])
    ]
    sender = Sender(server=ZABBIX_SERVER, port=10051)
    result = sender.send(items)
    #print(getTime, end=' ')
    print(result)
    exit(0)

print(getTime, end=' ')
print("Failed to get co2meter")
exit(1)

