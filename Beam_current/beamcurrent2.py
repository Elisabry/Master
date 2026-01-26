import numpy as np 
import matplotlib.pyplot as plt 
import curie as ci 
import pandas as pd 
# from scipy.interpolate import splev, splrep
from scipy.interpolate import interp1d
from scipy.interpolate import PchipInterpolator

# ...existing code...
def calculate_beam_currents_w_unc(self):
    """
    Compute beam currents (nA) and their uncertainties from lists stored on `self`.
    Expects self to have:
      - areal_dens (mg/cm^2)
      - areal_dens_unc_percent
      - molar_mass (g/mol)
      - molar_mass_unc (g/mol)
      - reaction_list, A0_list, A0_unc_list, xs_mon_list, xs_mon_unc_list,
        decay_const_list, decay_const_unc_list
    Results appended to:
      - self.beam_current_list
      - self.beam_current_unc_list
    """
    N_A = 6.0221408e+23
    t_irr = 1200.0  # [s]
    t_irr_unc = 3.0  # [s]

    # convert areal density (assumed given in mg/cm^2) -> g/cm^2
    areal_dens = float(self.areal_dens) / 1000.0  # g/cm^2
    molar_dens = areal_dens / self.molar_mass  # mol/cm^2
    N_T_per_cm2 = N_A * molar_dens  # nuclei / cm^2
    N_T = N_T_per_cm2 * 1.0e4  # nuclei / m^2

    # initialize output lists if not present
    if not hasattr(self, "beam_current_list"):
        self.beam_current_list = []
    if not hasattr(self, "beam_current_unc_list"):
        self.beam_current_unc_list = []

    # prepare N_T uncertainty from areal density and molar mass uncertainties
    areal_dens_unc = areal_dens * (self.areal_dens_unc_percent / 100.0)
    N_T_unc = N_T * np.sqrt((areal_dens_unc / areal_dens) ** 2 + (self.molar_mass_unc / self.molar_mass) ** 2)

    # helper: beam current in decay/s for given parameters
    def beam_dps(A0, N_Tp, xs, decay, tirr):
        return A0 / (N_Tp * xs * (1.0 - np.exp(-decay * tirr)))

    eps = 1e-8
    for i in range(len(self.reaction_list)):
        A0 = float(self.A0_list[i])
        xs = float(self.xs_mon_list[i])
        decay = float(self.decay_const_list[i])

        # baseline beam current [decays/s]
        try:
            baseline = beam_dps(A0, N_T, xs, decay, t_irr)
        except ZeroDivisionError:
            baseline = np.nan

        # convert to A then nA (1 elementary charge = 1.60217634e-19 C)
        baseline_A = baseline * 1.60217634e-19
        baseline_nA = baseline_A * 1.0e9

        # numerical partial derivatives (central differences)
        dA0 = (beam_dps(A0 + eps, N_T, xs, decay, t_irr) - beam_dps(A0 - eps, N_T, xs, decay, t_irr)) / (2 * eps)
        dN_T = (beam_dps(A0, N_T + eps, xs, decay, t_irr) - beam_dps(A0, N_T - eps, xs, decay, t_irr)) / (2 * eps)
        dxs = (beam_dps(A0, N_T, xs + eps, decay, t_irr) - beam_dps(A0, N_T, xs - eps, decay, t_irr)) / (2 * eps)
        ddecay = (beam_dps(A0, N_T, xs, decay + eps, t_irr) - beam_dps(A0, N_T, xs, decay - eps, t_irr)) / (2 * eps)
        dtirr = (beam_dps(A0, N_T, xs, decay, t_irr + eps) - beam_dps(A0, N_T, xs, decay, t_irr - eps)) / (2 * eps)

        derivs = np.array([dA0, dN_T, dxs, ddecay, dtirr])
        unc_inputs = np.array([
            float(self.A0_unc_list[i]),
            float(N_T_unc),
            float(self.xs_mon_unc_list[i]),
            float(self.decay_const_unc_list[i]),
            float(t_irr_unc),
        ])

        # combined uncertainty in decay/s, then convert to nA
        bc_unc_dps = np.sqrt(np.sum((derivs * unc_inputs) ** 2))
        bc_unc_nA = bc_unc_dps * 1.60217634e-19 * 1.0e9

        self.beam_current_list.append(baseline_nA)
        self.beam_current_unc_list.append(bc_unc_nA)
# ...existing code...

if __name__ == "__main__":
    import ast, re, os
    # set this to the CSV you want to use
    csv_path = "Activity/Activity_data/Cu01_A0.csv"  # <- update if your file is in a subfolder
    if not os.path.exists(csv_path):
        raise SystemExit(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path, dtype=str).fillna("")

    def try_literal(cell):
        s = str(cell).strip()
        if s.startswith("[") or s.startswith("("):
            try:
                return ast.literal_eval(s)
            except Exception:
                pass
        return s

    def parse_label(cell):
        v = try_literal(cell)
        if isinstance(v, (list, tuple)) and v:
            v = v[0]
        s = str(v)
        m = re.findall(r"[A-Za-z0-9]+", s)
        return m[0] if m else s

    def parse_first_number_or_list(cell, pick_last=False):
        v = try_literal(cell)
        if isinstance(v, (list, tuple)):
            nums = []
            for item in v:
                try:
                    nums.append(float(item))
                except Exception:
                    # try to extract numbers from string elements
                    found = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", str(item))
                    for f in found:
                        try:
                            nums.append(float(f))
                        except Exception:
                            pass
            if not nums:
                return 0.0
            return float(nums[-1] if pick_last else nums[0])
        # fallback: extract first numeric token from string
        s = str(v)
        nums = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", s)
        return float(nums[-1] if (pick_last and nums) else (nums[0] if nums else 0.0))

    reactions = [parse_label(x) for x in df.get("isotope", [])]
    A0_list = [parse_first_number_or_list(x, pick_last=False) for x in df.get("A0", [])]

    # prefer sigma_A0 (one-value uncertainty). If not present, try 'cov A0' and pick a suitable element.
    if "sigma_A0" in df.columns:
        A0_unc_list = [parse_first_number_or_list(x, pick_last=False) for x in df["sigma_A0"]]
    elif "cov A0" in df.columns:
        # cov A0 may be a matrix; pick last or diag element depending on formatting
        A0_unc_list = [parse_first_number_or_list(x, pick_last=True) for x in df["cov A0"]]
    else:
        A0_unc_list = [0.0] * len(A0_list)

    n = max(len(reactions), len(A0_list))
    def pad(l, length, fill):
        return (l + [fill] * length)[:length]

    reactions = pad(reactions, n, "")
    A0_list = pad(A0_list, n, 0.0)
    A0_unc_list = pad(A0_unc_list, n, 0.0)

    from types import SimpleNamespace
    s = SimpleNamespace()

    s.areal_dens = 2.0
    s.areal_dens_unc_percent = 1.0
    s.molar_mass = 63.546
    s.molar_mass_unc = 0.0

    s.reaction_list = reactions
    s.A0_list = A0_list
    s.A0_unc_list = A0_unc_list

    s.xs_mon_list = [1.0] * n
    s.xs_mon_unc_list = [0.0] * n
    s.decay_const_list = [1e-6] * n
    s.decay_const_unc_list = [0.0] * n

    s.beam_current_list = []
    s.beam_current_unc_list = []

    calculate_beam_currents_w_unc(s)

    out = pd.DataFrame({
        "reaction": s.reaction_list,
        "beam_current_nA": s.beam_current_list,
        "beam_current_unc_nA": s.beam_current_unc_list,
    })
    out.to_csv("beam_currents_output.csv", index=False)
    print("Wrote beam_currents_output.csv with", len(out), "rows.")
# ...existing code...