import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("E-log/2025-09-23 17_34_39.179.csv", usecols=[0,1,2,3])
df2 = pd.read_csv("E-log/2025-09-24 14_43_43.101.csv", usecols=[0,1,2,3])

# Rename columns
df.columns = ["Time", "Current_nA", "IntegratedCharge_C", "BeamOnTime_s"]
df2.columns = ["Time", "Current_nA", "IntegratedCharge_C", "BeamOnTime_s"]

# Convert time column
df["Time"] = pd.to_datetime(df["Time"])
df2["Time"] = pd.to_datetime(df2["Time"])

# Print end of beam time 
end_beam_1 = df.loc[df["BeamOnTime_s"].idxmax(), "Time"]
end_beam_2 = df2.loc[df2["BeamOnTime_s"].idxmax(), "Time"]

print("End of beam time file 1:", end_beam_1)
print("End of beam time file 2:", end_beam_2)

# Plot 1:
plt.figure()
plt.plot(df["Time"], df["Current_nA"])
plt.xlabel("Time")
plt.ylabel("Current (nA)")
plt.title("Beam Current vs Time (2025-09-23)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: 
plt.figure()
plt.plot(df2["Time"], df2["Current_nA"], color="orange")
plt.xlabel("Time")
plt.ylabel("Current (nA)")
plt.title("Beam Current vs Time (2025-09-24)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
