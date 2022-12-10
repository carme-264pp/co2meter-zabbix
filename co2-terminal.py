#!/bin/env python
import time
import json
from datetime import datetime

from CO2Meter import *

WAITTIME=5
count = 5

Meter = None

try:
    Meter = CO2Meter("/dev/hidraw0")
    print("Wake up time...")
    time.sleep(3)
except Exception as e:
    print("Error: cannot read CO2 Meter.")
    print(e)
    exit(1)

try:
    while True:
        co2data = Meter.get_data()
        if 'temperature' not in co2data or 'co2' not in co2data:
            if count <= 0:
                break
            print("Wake up time...")
            time.sleep(1)
            count = count - 1
            continue
        co2data.update({'timestamp': datetime.now().isoformat()})
        print(json.dumps(co2data))
        time.sleep(WAITTIME)
except KeyboardInterrupt:
    exit(0)

exit(1)

