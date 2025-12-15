import pandas as pd
import curie as ci
import numpy as np
import matplotlib.pyplot as plt
import os

# --- User input: list of CSV spectra and isotope names ---
spectra_files = [
    'Spectroscopy/Cu_peak_summary/BW09242025_Cu06_52cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/CD09242025_Cu06_45cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/CR09252025_Cu06_40cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/DF09252025_Cu06_30cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/EG09262025_Cu06_10cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/FB09272025_Cu06_10cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/GX10222025_Det2_Cu06_10cm_jobs_peak_summary.csv',
]

isotopes_list = ['62ZN', '63ZN', '65ZN', '56CO', '58CO']

foil_name = 'Cu06'
EoB_time = '09/24/2025 15:43:00'  # End of beam

# --- Read and combine CSV files ---
df_list = [pd.read_csv(f) for f in spectra_files]
df_concat = pd.concat(df_list, axis=0)

# --- Ensure output folder exists ---
output_path = "Activity/Combined_peak_summary"
os.makedirs(output_path, exist_ok=True)

# --- Save combined CSV ---
combined_csv_path = os.path.join(output_path, f"{foil_name}_combined.csv")
df_concat.to_csv(combined_csv_path, index=False)
print(f"Combined CSV saved to: {combined_csv_path}")

# --- Loop through isotopes ---
data = []
for isotope in isotopes_list:
    if not df_concat[df_concat['isotope'] == isotope].empty:
        #dc = ci.DecayChain(isotope, R=[[1e4, 1]], units='h')
        dc = ci.DecayChain(isotope, A0=1e6, units='h')
        dc.get_counts(spectra='', EoB=EoB_time, peak_data=df_concat)
        #isotopes, R, cov_R = dc.fit_R()
        isotopes, A0, cov_A0 = dc.fit_A0()

        # Plot
        dc.plot(title=f'Decay Plot for {foil_name} – {isotope}')
        # plt.show()
        
        # Print decay constants
        print(f"Decay constants (R) for {isotope}:")
        print(dc.R)
        # df_R = pd.DataFrame({'isotopes': [isotopes[0]], 'R': [R[0]], 'cov_R': [cov_R[0]]})
        # df_A0 = pd.DataFrame({'isotopes': [isotopes[0]], 'A0': [A0[0]], 'cov_A': [cov_A0[0]]})
        if len(isotopes) > 1:
            for i in range(len(isotopes)):
                sigma_A0 = np.sqrt(cov_A0[i])
                data.append([isotopes[i], A0[i], cov_A0[i], sigma_A0])
        else: 
            sigma_A0 = np.sqrt(cov_A0[0])
            data.append([isotopes, A0, cov_A0, sigma_A0])
    else:
        print(f"No data for {isotope} in this foil.")
df = pd.DataFrame(data, columns=['isotope', 'A0', 'cov A0', 'sigma_A0'])
df.to_csv('Activity/Activity_data/Cu06_A0.csv')