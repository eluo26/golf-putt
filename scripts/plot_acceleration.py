import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/putt_ble_001.csv")
plt.plot(df["time"], df["az"], label="Z Acceleration")
plt.title("Z-axis Acceleration from Putt Stroke")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.grid()
plt.legend()
plt.show()
