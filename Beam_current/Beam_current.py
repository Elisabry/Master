# ...existing code...
import numpy as np 
import pandas as pd 

# Attempt to read CSV with clear error if missing
csv_path = "Activity/Activity_data/Cu01_A0.csv"
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Input CSV not found at: {csv_path}")
except Exception as e:
    raise RuntimeError(f"Failed to read CSV '{csv_path}': {e}")

# Constants
NA = 6.02214076e23  # Avogadro [1/mol]

# Experiment-specific values
areal_density = 21      # g/cm^2  (example!)
areal_density_unc = 0.02   # g/cm^2

molar_mass = 63.546     # g/mol for natural Cu (fixed)
t_irr = 3600.0                 # seconds
 
cross_sections = {
    "62ZNg": (120e-27, 6e-27),   # σ, Δσ [cm^2]
    "63ZNg": (85e-27, 4e-27),
    "65ZNg": (40e-27, 2e-27),
    "56COg": (15e-27, 1e-27),
    "58COg": (22e-27, 1.5e-27),
}

decay_constants = {
    "62ZNg": np.log(2) / (9.186 * 3600),   # half-life in seconds
    "63ZNg": np.log(2) / (38.47 * 60),
    "65ZNg": np.log(2) / (244 * 24 * 3600),
    "56COg": np.log(2) / (77.27 * 24 * 3600),
    "58COg": np.log(2) / (70.86 * 24 * 3600),
}

# Derived quantities (check for zero to avoid division)
NT = areal_density * NA / molar_mass
NT_unc = areal_density_unc * NA / molar_mass
if NT == 0:
    raise ValueError("Computed NT is zero — check areal_density and molar_mass values")

beam_currents = []

# Validate required columns and locate possible uncertainty column
required_cols = {"isotope", "A0"}
if not required_cols.issubset(df.columns):
    raise ValueError(f"Input CSV must contain columns: {required_cols}")

# support a few common uncertainty column names
possible_unc_cols = ["sigma_A0", "A0_unc", "A0_err"]
unc_col = next((c for c in possible_unc_cols if c in df.columns), None)

# Ensure numeric types for A0 and uncertainty column if present
df["A0"] = pd.to_numeric(df["A0"], errors="coerce")
if unc_col:
    df[unc_col] = pd.to_numeric(df[unc_col], errors="coerce")

# --- Added diagnostics and cleaning: place here (before processing loop) ---
# Normalize isotope strings and report file contents to diagnose skips
if "isotope" in df.columns:
    df["isotope"] = df["isotope"].astype(str).str.strip()

print("Input CSV columns:", list(df.columns))
print("Unique isotopes in file:", sorted(df["isotope"].unique()))
print("Rows with NaN A0:", int(df["A0"].isna().sum()))
print("Rows with A0 == 0:", int((df["A0"] == 0).sum()))

missing_isotopes = set(df["isotope"].unique()) - set(cross_sections.keys())
if missing_isotopes:
    print("Isotopes missing cross section entries:", sorted(missing_isotopes))

missing_decay = set(df["isotope"].unique()) - set(decay_constants.keys())
if missing_decay:
    print("Isotopes missing decay-constant entries:", sorted(missing_decay))
# --- end diagnostics ---

processed = 0
skipped = 0

for _, row in df.iterrows():
    isotope = row.get("isotope")
    A0 = row.get("A0")
    A0_unc = row.get(unc_col, np.nan) if unc_col else np.nan

    # Skip invalid or zero activities
    if pd.isna(A0) or A0 == 0:
        print(f"Warning: skipping isotope '{isotope}' due to invalid or zero A0")
        skipped += 1
        continue

    # Get nuclear data
    if isotope not in cross_sections:
        print(f"Warning: cross section for isotope '{isotope}' not found — skipping")
        skipped += 1
        continue
    sigma, sigma_unc = cross_sections[isotope]
    if sigma == 0:
        print(f"Warning: σ=0 for isotope '{isotope}' — skipping")
        skipped += 1
        continue

    lam = decay_constants.get(isotope)
    if lam is None or lam <= 0:
        print(f"Warning: decay constant for isotope '{isotope}' not found or invalid — skipping")
        skipped += 1
        continue

    # Decay correction factor (irradiation build-up)
    decay_factor = 1.0 - np.exp(-lam * t_irr)
    if decay_factor == 0:
        print(f"Warning: decay factor zero for isotope '{isotope}' — skipping")
        skipped += 1
        continue

    # Beam current (flux)
    Phi = float(A0) / (NT * sigma * decay_factor)

    # Relative uncertainty (handle missing A0_unc)
    rel_unc_sq = (
        (0.0 if pd.isna(A0_unc) or A0_unc == 0 else (float(A0_unc) / float(A0)) ** 2) +
        (NT_unc / NT) ** 2 +
        (sigma_unc / sigma) ** 2
    )

    Phi_unc = Phi * np.sqrt(rel_unc_sq)

    beam_currents.append((isotope, Phi, Phi_unc))
    processed += 1

print(f"Processed: {processed}, Skipped: {skipped}")

for iso, Phi, Phi_unc in beam_currents:
    print(f"{iso:6s}  Φ = {Phi:.3e} ± {Phi_unc:.3e}")
# ...existing code...