import pandas as pd
import numpy as np


def to_float(x):
    if isinstance(x, str):
        return float(x.strip("[]").split()[0])
    return float(x)


def beam_current_from_csv(csv_file, NT, sigma, lambda_, t_irr):
    df = pd.read_csv(csv_file)
    results = []

    decay_factor = 1.0 - np.exp(-lambda_ * t_irr)

    for _, row in df.iterrows():
        isotope = row["isotope"]
        A0 = to_float(row["A0"])
        dA0 = to_float(row["sigma_A0"])

        # Skip zero activity
        if A0 == 0:
            continue

        Phi = A0 / (NT * sigma * decay_factor)
        Phi_unc = Phi * (dA0 / A0)

        results.append((isotope, Phi, Phi_unc))

    return results




if __name__ == "__main__":

    NT = 3.2e20          # number of target atoms
    sigma = 100e-27      # cm^2
    lambda_ = 1.2e-4     # 1/s
    t_irr = 3600         # s

    csv_file = "Activity/Activity_data/Cu01_A0.csv"
    beam_currents = beam_current_from_csv(csv_file, NT, sigma, lambda_, t_irr)

    for isotope, I, dI in beam_currents:
        print(f"{isotope:8s}  I = {I:.3e} ± {dI:.3e}")
