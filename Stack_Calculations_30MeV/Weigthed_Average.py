import os
import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator
from pathlib import Path
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# Def for load IAEA monitor cross section files and interpolating
# ---------------------------------------------------------------
def load_file_with_uncertainty(file):
    """Load cross section data with uncertainties and return PCHIP interpolators."""
    path = './Monitor_Cross_Sections/IAEA_Monitor_Data/'
    data = []
    for line in open(path+file+'.txt').readlines()[6:]:
        if line.strip():
            try:
                e, xs, unc = map(float, line.split()[:3])
                data.append((e, xs, unc))
            except ValueError:
                continue
    if len(data) < 2:
        return None, None
    E, xs, unc = map(np.array, zip(*data))
    interp_xs = PchipInterpolator(E, xs, extrapolate=True)
    interp_unc = PchipInterpolator(E, unc, extrapolate=True)
    return E, interp_xs, interp_unc


# ---------------------------------------------------------------
# Def for load flux files and saving energies and fluxes in arrays
# ---------------------------------------------------------------

def load_flux_file(dp, target, stack='30MeV'):
    path = f'./Stack_Calculations_{stack}/'
    file = f'stack_{stack}_dp_{dp}_fluxes.csv'

    flux_data = pd.read_csv(path + file)
    target_data = flux_data.loc[flux_data['name'] == target]
    energy_array = np.array(target_data['energy'].values)
    flux_array = np.array(target_data['flux'].values)
    return energy_array, flux_array


# -----------------------------------------------------------------------------
# Def for calcualting flux weighted average cross sections for monitor reactions
# -----------------------------------------------------------------------------

def flux_weighted_cross_section(dp, target, mon_reaction, stack='30MeV'):
    energy_array, flux_array = load_flux_file(dp, target, stack=stack)
    E, interp_xs, interp_unc = load_file_with_uncertainty(mon_reaction)

    #Calculating flux weighted avrg energy
    E_foil = np.sum(energy_array * flux_array) / np.sum(flux_array)
    
    #Calculating flux weighted avrg cross section
    xs_not_norm = np.trapz(np.multiply(interp_xs(energy_array), flux_array), energy_array)
    xs_norm = xs_not_norm / np.trapz(flux_array, energy_array)

    #Calculating flux weighted avrg unc for cross section
    xs_unc_not_norm = np.trapz(np.multiply(interp_unc(energy_array), flux_array), energy_array)
    xs_unc_norm = xs_unc_not_norm / np.trapz(flux_array, energy_array)
    print(target, E_foil)
   
    return E_foil, xs_norm, xs_unc_norm








E, xs, xs_unc = flux_weighted_cross_section(1.02, 'Cu08', 'cup63znt')
E, xs, xs_unc = flux_weighted_cross_section(0.94, 'Cu01', 'cup63znt', stack='55MeV')
print(f'xs = {xs} +- {xs_unc} mb')


# --------------------------------------------------
# Load monitor curves
# --------------------------------------------------

IAEA_monitor_files = ['cup56cot', 'cup58cot', 'cup62znt', 'cup63znt', 'cup65znt', 'nip57nit']
curves = {}
curves_unc = {}

for file in IAEA_monitor_files:
    energy_array, interp_xs, interp_unc = load_file_with_uncertainty(file)
    curves[file] = interp_xs
    curves_unc[file] = interp_unc
#     plt.plot(energy_array, interp_xs(energy_array), label=file)
# plt.xlabel("Proton Energy (MeV)")
# plt.ylabel("Cross Section (mb)")
# plt.xlim(0,100)
# plt.legend()
# plt.show()

foils = ['Cu08', 'Cu09', 'Cu10', 'Cu11', 'Cu12', 'Cu13', 'Cu14']

energy_array, interp_xs, interp_unc = load_file_with_uncertainty("cup63znt")
plt.plot(energy_array, interp_xs(energy_array), label="cup63znt")

for foil in foils:
    E, xs, xs_unc = flux_weighted_cross_section(1.01, foil, 'cup63znt')
    plt.plot(E, xs, 'o', color='black')

   
plt.xlabel("Proton Energy (MeV)")
plt.ylabel("Cross Section (mb)")
plt.xlim(0,100)
plt.legend()
plt.show()


