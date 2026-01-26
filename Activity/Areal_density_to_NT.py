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

Cu_areal_density = [21.906, 22.235, 22.253, 22.289, 22.311, 22.233, 22.258, 22.197, 22.091, 22.259, 22.211, 22.177, 22.168, 22.125]  # mg/cm2
Cu_ad_uncertainty = [0.086, 0.041, 0.067, 0.029, 0.022, 0.057, 0.037, 0.023, 0.039, 0.032, 0.105, 0.062, 0.058, 0.112]

Ni_areal_density = [23.079, 23.091, 22.966, 22.982, 22.942, 22.631, 22.529, 23.145, 22.662, 23.107, 22.941, 23.155, 23.153, 23.067] # mg/cm2
Ni_ad_uncertainty = [0.034, 0.016, 0.071, 0.048, 0.028, 0.038, 0.032, 0.096, 0.015, 0.024, 0.030, 0.016, 0.038, 0.026] 

Ta_areal_density = [27.334, 27.396, 27.702, 27.518, 27.197, 27.374, 27.539, 27.227, 27.377, 27.165, 27.200, 27.702, 27.337, 27.361]  
Ta_ad_uncertainty = [0.090, 0.138, 0.080, 0.066, 0.141, 0.157, 0.073, 0.129, 0.074, 0.151, 0.136, 0.136, 0.041, 0.104]

Sn_areal_density = [37.475, 37.211, 37.130, 36.990, 8.004, 7.816, 7.917, 8.047, 7.829, 8.232, 7.982, 8.021, 7.354, 7.620]  
Sn_ad_uncertainty = [0.436, 0.166, 0.141, 0.298, 0.019, 0.026, 0.017, 0.018, 0.010, 0.012, 0.019, 0.023, 0.026, 0.013]

Cu_df = compute_areal_density('Cu', Cu_areal_density, Cu_ad_uncertainty)
Ni_df = compute_areal_density('Ni', Ni_areal_density, Ni_ad_uncertainty)
Ta_df = compute_areal_density('Ta', Ta_areal_density, Ta_ad_uncertainty)    
Sn_df = compute_areal_density('Sn', Sn_areal_density, Sn_ad_uncertainty)    

print(Cu_df)
print(Ni_df)
print(Ta_df)    
print(Sn_df)    

# Save CSVs to the same folder as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
cu_path = os.path.join(script_dir, 'Cu_areal_density_NT.csv')
ni_path = os.path.join(script_dir, 'Ni_areal_density_NT.csv')
ta_path = os.path.join(script_dir, 'Ta_areal_density_NT.csv')
sn_path = os.path.join(script_dir, 'Sn_areal_density_NT.csv')

Cu_df.to_csv(cu_path, index=False)
Ni_df.to_csv(ni_path, index=False)
Ta_df.to_csv(ta_path, index=False)  
Sn_df.to_csv(sn_path, index=False)  

print(f'Wrote {cu_path}')
print(f'Wrote {ni_path}')
print(f'Wrote {ta_path}')
print(f'Wrote {sn_path}')   