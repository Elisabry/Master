import numpy as np
import pandas as pd
from pathlib import Path


# ==================== CONSTANTS ====================
t_irr = 3600.0  # irradiation time [s]
# If you have two alternative irradiation times, you can call the function twice with different t_irr values

# ==================== NUCLEAR DATA ====================
# σ, Δσ [cm^2] (IAEA monitor data or literature values) kan jeg bare skrive de inn får hånd?
cross_sections = {
    "62ZNg": (120e-27, 6e-27), # husk enheter 40,2 
    "63ZNg": (85e-27, 4e-27),
    "65ZNg": (40e-27, 2e-27),
    "56COg": (15e-27, 1e-27),
    "58COg": (22e-27, 1.5e-27),
    "57Nig": (10e-27, 0.5e-27),
    # Add Ni, Ta isotopes here
} 

# decay constants [1/s] (IAEA monitor data or literature values) må jeg lage egen kode for dette?
decay_constants = {
    "62ZNg": np.log(2) / (9.186 * 3600),
    "63ZNg": np.log(2) / (38.47 * 60),
    "65ZNg": np.log(2) / (244 * 24 * 3600),
    "56COg": np.log(2) / (77.27 * 24 * 3600),
    "58COg": np.log(2) / (70.86 * 24 * 3600),
    "57Nig": np.log(2) / (35.60 * 24 * 3600),
    # Add Ni, Ta isotopes here
}

# ==================== CREATE OUTPUT FOLDER ====================
output_folder = Path("Beam_Current")
output_folder.mkdir(exist_ok=True)  # create folder if it doesn't exist

# ==================== FUNCTION TO PROCESS FOILS ====================
def process_foils(material, foil_props_csv, foil_data_path, file_pattern, nt_col, nt_unc_col, output_filename):
    print(f"\n=== Processing {material} foils ===")

    foil_props = pd.read_csv(foil_props_csv)
    csv_files = sorted(Path(foil_data_path).glob(file_pattern))
    results = []

    for csv_path in csv_files:
        print(f"Processing {csv_path.name} ({material})")

        # Extract foil index from filename (e.g., Cu01 -> 0)
        foil_index = int(csv_path.stem[2:4]) - 1
        NT = foil_props.loc[foil_index, nt_col]
        NT_unc = foil_props.loc[foil_index, nt_unc_col]

        df = pd.read_csv(csv_path)
        df["isotope"] = df["isotope"].astype(str).str.strip()
        df["A0"] = pd.to_numeric(df["A0"], errors="coerce")
        df["sigma_A0"] = pd.to_numeric(df["sigma_A0"], errors="coerce")

        for _, row in df.iterrows():
            isotope = row["isotope"]
            A0 = row["A0"]
            A0_unc = row["sigma_A0"]

            if pd.isna(A0) or A0 <= 0:
                continue

            if isotope not in cross_sections or isotope not in decay_constants:
                continue

            sigma, sigma_unc = cross_sections[isotope]
            lam = decay_constants[isotope]

            decay_factor = 1.0 - np.exp(-lam * t_irr)
            if decay_factor <= 0:
                continue

            Phi = A0 / (NT * sigma * decay_factor)
            rel_unc_sq = (
                (0.0 if pd.isna(A0_unc) or A0_unc == 0 else (A0_unc / A0) ** 2)
                + (NT_unc / NT) ** 2
                + (sigma_unc / sigma) ** 2
            )
            Phi_unc = Phi * np.sqrt(rel_unc_sq)

            results.append({
                "file": csv_path.name,
                "foil_index": foil_index + 1,
                "isotope": isotope,
                "Phi": Phi,
                "Phi_unc": Phi_unc
            })

    results_df = pd.DataFrame(results)
    # Save CSV inside Beam_Current folder
    results_df.to_csv(output_folder / output_filename, index=False)
    print(f"Saved {material} results to '{output_folder / output_filename}'")


# ==================== RUN FOR CU, NI, TA ====================
process_foils(
    material="Cu",
    foil_props_csv="Activity/Cu_areal_density_NT.csv",
    foil_data_path="Activity/Activity_data",
    file_pattern="Cu*_A0.csv",
    nt_col="Cu_NT_atoms_per_cm2",
    nt_unc_col="Cu_NT_unc_atoms_per_cm2",
    output_filename="beam_currents_all_Cu_foils.csv"
)

process_foils(
    material="Ni",
    foil_props_csv="Activity/Ni_areal_density_NT.csv",
    foil_data_path="Activity/Activity_data",
    file_pattern="Ni*_A0.csv",
    nt_col="Ni_NT_atoms_per_cm2",
    nt_unc_col="Ni_NT_unc_atoms_per_cm2",
    output_filename="beam_currents_all_Ni_foils.csv"
)



