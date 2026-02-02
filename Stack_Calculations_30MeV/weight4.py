import os
import numpy as np
from scipy.interpolate import PchipInterpolator

# Load IAEA monitor cross section files
def load_file(path):
    data = [tuple(map(float, line.split()[:2]))
            for line in open(path).readlines()[6:]
            if line.strip()]
    if len(data) < 2:
        return None
    E, xs = map(np.array, zip(*data))
    return PchipInterpolator(E, xs, extrapolate=False)

# Path to your data folder
data_dir = "/Users/elisabethbrynildsen/Master/Monitor_Cross_Sections/IAEA_Monitor_Data"

# Create interpolators
curves = {
    f.replace(".txt", ""): load_file(os.path.join(data_dir, f))
    for f in os.listdir(data_dir)
    if f.endswith(".txt")
}

# Flux-weighted mean energy ⟨E⟩ = ∫E*phi / ∫phi
def flux_weighted_energy(E, phi):
    phi = np.asarray(phi)
    E = np.asarray(E)
    if np.all(phi == 0):
        return np.nan
    return np.trapz(E * phi, E) / np.trapz(phi, E)

# Flux-weighted mean cross section ⟨σ⟩ = ∫σ*phi / ∫phi
def flux_weighted_cross_section(E, phi, sigma):
    phi = np.asarray(phi)
    sigma = np.asarray(sigma)
    E = np.asarray(E)
    if np.all(phi == 0):
        return np.nan
    return np.trapz(sigma * phi, E) / np.trapz(phi, E)

# ---------------- Example usage ----------------
if __name__ == "__main__":
    
    # Define a sample energy grid
    E_mon = np.linspace(0, 50, 1000)  # MeV

    # Define a simple test flux (for example purposes)
    phi = np.exp(-((E_mon - 20)/5)**2)  # Gaussian-shaped flux centered at 20 MeV

    # Pick a sample cross section curve from your loaded files
    # We'll just pick the first one that successfully loaded
    for label, interp in curves.items():
        if interp is not None:
            sigma = interp(E_mon)  # Interpolate cross section
            print(f"Using curve: {label}")
            break
    else:
        raise RuntimeError("No valid cross section files found!")

    # Compute flux-weighted energy and cross section
    avg_E = flux_weighted_energy(E_mon, phi)
    avg_sigma = flux_weighted_cross_section(E_mon, phi, sigma)

    print(f"Flux-weighted mean energy ⟨E⟩ = {avg_E:.2f} MeV")
    print(f"Flux-weighted mean cross section ⟨σ⟩ = {avg_sigma:.2f} mb")
