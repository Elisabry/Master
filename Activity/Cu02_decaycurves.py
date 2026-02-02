import pandas as pd
import curie as ci
import numpy as np
import matplotlib.pyplot as plt
import os

# --- User input: list of CSV spectra and isotope names ---
spectra_files = [
    'Spectroscopy/Cu_peak_summary/BS09242025_Cu02_52cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/BZ09242025_Cu02_45cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/CN09242025_Cu02_40cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/DB09252025_Cu02_30cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/EK09262025_Cu02_10cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/FG09282025_Cu02_10cm_IDM_peak_summary.csv',
    'Spectroscopy/Cu_peak_summary/GQ10232025_IDM_Cu02_10cm_jobs_peak_summary.csv',
]

isotopes_list = ['62ZN', '63ZN', '65ZN', '56CO', '58CO']

foil_name = 'Cu02'
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

# ...existing code...
# --- Loop through isotopes ---
data = []
os.makedirs("Activity/Activity_data", exist_ok=True)

for isotope in isotopes_list:
    df_iso = df_concat[df_concat['isotope'] == isotope]
    if df_iso.empty:
        print(f"No data for {isotope} in this foil.")
        continue

    # Try to detect any count columns; if none found, we still attempt the fit
    count_cols = [c for c in df_iso.columns if "count" in c.lower()]
    has_counts = True
    if count_cols:
        vals = df_iso[count_cols].fillna(0).to_numpy(dtype=float)
        has_counts = vals.size and (vals.sum() > 0)

    if not has_counts:
        print(f"No valid counts for {isotope}, skipping fit.")
        continue

    dc = ci.DecayChain(isotope, A0=1e6, units='h')
    try:
        dc.get_counts(spectra='', EoB=EoB_time, peak_data=df_concat)
    except Exception as e:
        print(f"get_counts failed for {isotope}: {e}")
        continue

    try:
        isotopes_fit, A0, cov_A0 = dc.fit_A0()
    except ValueError as e:
        # handle the empty ydata case gracefully and continue with next isotope
        if "ydata" in str(e):
            print(f"{isotope}: no valid counts for fit (ydata empty), skipping fit.")
            continue
        else:
            raise

    # Plot
    dc.plot(title=f'Decay Plot for {foil_name} – {isotope}')

    # Normalize shapes and compute sigmas robustly
    cov_arr = np.array(cov_A0)
    A0_arr = np.atleast_1d(A0)
    isotopes_arr = isotopes_fit if isinstance(isotopes_fit, (list, tuple, np.ndarray)) else [isotopes_fit]

    if cov_arr.ndim == 2:
        sigmas = np.sqrt(np.diag(cov_arr))
    else:
        sigmas = np.sqrt(np.atleast_1d(cov_arr))

    for i, iso in enumerate(isotopes_arr):
        a0_val = float(A0_arr[i]) if i < A0_arr.size else float(A0_arr[0])
        cov_val = float(cov_arr[i, i]) if (cov_arr.ndim == 2 and i < cov_arr.shape[0]) else float(np.atleast_1d(cov_arr)[i])
        sigma = float(sigmas[i]) if i < len(sigmas) else float(sigmas[0])
        data.append([iso, a0_val, cov_val, sigma])

df_out = pd.DataFrame(data, columns=['isotope', 'A0', 'cov A0', 'sigma_A0'])
df_out.to_csv('Activity/Activity_data/Cu02_A0.csv', index=False)                    #ENDRE NAVNET HER!
print("Saved A0 results to: Activity/Activity_data/Cu02_A0.csv")                    #ENDRE NAVNET HER!
# ...existing code...


# isotope: the nuclide (the fitted component) returned by the fit.
# A0: the fitted initial activity for that isotope at End‑of‑Beam (EoB). Units are the activity units used by the curie.DecayChain/fit (check your curie settings; typically activity is in Bq or decays per time unit).
# cov A0: the covariance (or variance) of the fitted A0 parameters — a matrix when multiple fit components were returned, or a single variance if only one component.
# sigma_A0: the 1‑sigma uncertainty for A0 (square root of the relevant diagonal element of the covariance).

