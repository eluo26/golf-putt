# scripts/read_ble_sensor.py
import asyncio
from bleak import BleakClient
import pandas as pd
import time

ADDRESS = "C6:39:1A:09:2D:81"
CHAR_UUID = "0000ffe4-0000-1000-8000-00805f9b34fb" 
data = []

def notification_handler(sender, value):
    timestamp = time.time()
    try:
        line = value.decode(errors="ignore").strip()
        parts = line.split(',')
        if len(parts) >= 6:
            ax, ay, az, gx, gy, gz = map(float, parts[:6])
            data.append([timestamp, ax, ay, az, gx, gy, gz])
            print(f"az: {az:.2f}")
    except:
        pass

async def main():
    async with BleakClient(ADDRESS) as client:
        await client.start_notify(CHAR_UUID, notification_handler)
        print("Receiving data for 10 seconds...")
        await asyncio.sleep(10)
        await client.stop_notify(CHAR_UUID)

        df = pd.DataFrame(data, columns=["time", "ax", "ay", "az", "gx", "gy", "gz"])
        df.to_csv("data/putt_ble_001.csv", index=False)
        print("Saved data to data/putt_ble_001.csv")

asyncio.run(main())
