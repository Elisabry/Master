import scipy.constants as const
import curie as ci
import pandas as pd
import numpy as np
import os


# Return a DataFrame with areal density and atom density (NT) for a given element:
def compute_areal_density(element_symbol, ad_mg_per_cm2, ad_unc_mg_per_cm2):
    
    molar_mass = ci.Element(element_symbol.upper()).mass  # g/mol
    ad_g_per_cm2 = np.array(ad_mg_per_cm2) * 1e-3
    ad_unc_g_per_cm2 = np.array(ad_unc_mg_per_cm2) * 1e-3
    NT = ad_g_per_cm2 * const.N_A / molar_mass
    NT_unc = ad_unc_g_per_cm2 * const.N_A / molar_mass
    return pd.DataFrame({
        f'{element_symbol}_ad_mg_per_cm2': ad_mg_per_cm2,
        f'{element_symbol}_ad_unc_mg_per_cm2': ad_unc_mg_per_cm2,
        f'{element_symbol}_NT_atoms_per_cm2': NT,
        f'{element_symbol}_NT_unc_atoms_per_cm2': NT_unc
    })

Cu_areal_density = [21.91, 22.24, 22.25, 22.29, 22.31, 22.23, 22.26, 22.20, 22.09, 22.26, 22.21, 22.18, 22.17, 22.12]  # mg/cm2
Cu_ad_uncertainty = [0.086, 0.04, 0.07, 0.03, 0.02, 0.06, 0.04, 0.02, 0.04, 0.03, 0.11, 0.06, 0.06, 0.11]

Ni_areal_density = [23.08, 23.09, 22.97, 22.98, 22.94, 22.63, 22.53, 23.15, 22.66, 23.11, 22.94, 23.16, 23.15, 23.07] # mg/cm2
Ni_ad_uncertainty = [0.03, 0.02, 0.07, 0.05, 0.03, 0.04, 0.03, 0.10, 0.01, 0.02, 0.03, 0.02, 0.04, 0.03] 

Cu_df = compute_areal_density('Cu', Cu_areal_density, Cu_ad_uncertainty)
Ni_df = compute_areal_density('Ni', Ni_areal_density, Ni_ad_uncertainty)

print(Cu_df)
print(Ni_df)

# Save CSVs to the same folder as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
cu_path = os.path.join(script_dir, 'Cu_areal_density_NT.csv')
ni_path = os.path.join(script_dir, 'Ni_areal_density_NT.csv')

Cu_df.to_csv(cu_path, index=False)
Ni_df.to_csv(ni_path, index=False)

print(f'Wrote {cu_path}')
print(f'Wrote {ni_path}')
