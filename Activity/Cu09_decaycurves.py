import pandas as pd
import curie as ci
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# --- Read individual CSV files ---
df_AB = pd.read_csv('Spectroscopy/peak_summary/AB09232025_Cu09_52cm_IDM_peak_summary.csv')
df_AI = pd.read_csv('Spectroscopy/peak_summary/AI09232025_Cu09_45cm_IDM_peak_summary.csv')
df_BK = pd.read_csv('Spectroscopy/peak_summary/BK09242025_Cu09_30cm_IDM_peak_summary.csv')
df_EY = pd.read_csv('Spectroscopy/peak_summary/EY09272025_Cu09_10cm_IDM_peak_summary.csv')
df_DV = pd.read_csv('Spectroscopy/peak_summary/DV09252025_Cu09_10cm_IDM_peak_summary.csv')

# --- Combine all DataFrames ---
df_concat_Cu09 = pd.concat((df_AB, df_AI, df_BK, df_EY, df_DV), axis=0)

# --- Ensure output folder exists ---
output_path = "Spectroscopy/combined"
os.makedirs(output_path, exist_ok=True)

# --- Save combined data ---
combined_csv_path = os.path.join(output_path, "Cu09_IDM_combined.csv")
df_concat_Cu09.to_csv(combined_csv_path, index=False)
print(f"Combined data saved to: {combined_csv_path}")

# --- Initialize decay chain ---
dc = ci.DecayChain('62ZN', R=[[1e4, 1]], units='h')

# --- Run decay analysis ---
# Assuming get_counts() expects a file path for `peak_data`, not a DataFrame.
# The first argument (foil_name) can be a string identifier.
dc.get_counts('Cu09', EoB='09/23/2025 18:35:00', peak_data=combined_csv_path)

# --- Fit and plot decay results ---
isotopes, R, cov_R = dc.fit_R()
dc.plot(title='Decay Plot for Cu09')
plt.show()

# --- Print results ---
print("Decay constants (R):")
print(dc.R)
