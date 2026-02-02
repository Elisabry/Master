import numpy as np
import pandas as pd
from pathlib import Path

# ==================== CONSTANTS ====================
t_irr = 3600.0  # irradiation time [s]

# ==================== CREATE OUTPUT FOLDER ====================
output_folder = Path("Beam_Current")
output_folder.mkdir(exist_ok=True)  # create folder if it doesn't exist

# ==================== NUCLEAR DATA ====================
# Decay constants [1/s]
decay_constants = {
    "62ZNg": np.log(2) / (9.186 * 3600),
    "63ZNg": np.log(2) / (38.47 * 60),
    "65ZNg": np.log(2) / (244 * 24 * 3600),
    "56COg": np.log(2) / (77.27 * 24 * 3600),
    "58COg": np.log(2) / (70.86 * 24 * 3600),
    "57Nig": np.log(2) / (35.60 * 24 * 3600),
}

# ==================== FUNCTION ====================
def process_foils(material, foil_props_csv, weighted_csv_path, file_pattern, nt_col, nt_unc_col, output_filename):
    """
    Calculate beam current for foils using flux-weighted cross sections.
    """
    print(f"\n=== Processing {material} foils ===")

    # Load foil properties
    foil_props = pd.read_csv(foil_props_csv)
    weighted_csv_files = sorted(Path(weighted_csv_path).glob(file_pattern))
    results = []

    for weighted_csv_file in weighted_csv_files:
        print(f"Processing {weighted_csv_file.name}")
        weighted_csv = pd.read_csv(weighted_csv_file)

        for idx, foil_row in weighted_csv.iterrows():
            foil = foil_row["Foil"]
            foil_index = int(''.join(filter(str.isdigit, foil))) - 1  # e.g., Cu08 -> 7

            NT = foil_props.loc[foil_index, nt_col]
            NT_unc = foil_props.loc[foil_index, nt_unc_col]

            for iso in decay_constants.keys():
                lam = decay_constants[iso]

                # Column names in weighted CSV
                sigma_col = f"FluxWeightedCrossSection_{iso.lower()}_mb"
                sigma_unc_col = f"FluxWeightedCrossSection_{iso.lower()}_unc_mb"

                if sigma_col not in weighted_csv.columns:
                    continue  # isotope not present for this foil

                # Get weighted cross section (mb → cm^2)
                sigma = foil_row[sigma_col] * 1e-27
                sigma_unc = foil_row[sigma_unc_col] * 1e-27

                if sigma <= 0:
                    continue

                # Retrieve activity from a separate CSV if needed
                # Here we assume activity is in the same weighted CSV for simplicity
                if "A0" in foil_row:
                    A0 = foil_row["A0"]
                    A0_unc = foil_row.get("sigma_A0", 0.0)
                else:
                    # If not present, skip
                    continue

                decay_factor = 1.0 - np.exp(-lam * t_irr)
                if decay_factor <= 0:
                    continue

                # Beam current Φ(E_d) = A0 / (N_T * (1 - exp(-λ t_irr))) / σ_weighted
                Phi = A0 / (NT * decay_factor * sigma)

                # Uncertainty propagation
                rel_unc_sq = (
                    (0.0 if A0_unc == 0 else (A0_unc / A0) ** 2)
                    + (NT_unc / NT) ** 2
                    + (sigma_unc / sigma) ** 2
                )
                Phi_unc = Phi * np.sqrt(rel_unc_sq)

                results.append({
                    "Foil": foil,
                    "Isotope": iso,
                    "Phi": Phi,
                    "Phi_unc": Phi_unc,
                    "WeightedEnergy_MeV": foil_row.get("FluxWeightedEnergy_MeV", np.nan),
                    "Material": foil_row.get("Material", "")
                })

    # Save results
    out_path = output_folder / output_filename
    pd.DataFrame(results).to_csv(out_path, index=False)
    print(f"Saved beam current results → {out_path}")


# ==================== RUN ====================
process_foils(
    material="Cu",
    foil_props_csv="Activity/Cu_areal_density_NT.csv",
    weighted_csv_path="FluxWeighted",
    file_pattern="*_flux_weighted.csv",
    nt_col="Cu_NT_atoms_per_cm2",
    nt_unc_col="Cu_NT_unc_atoms_per_cm2",
    output_filename="beam_currents_all_Cu_foils.csv"
)

process_foils(
    material="Ni",
    foil_props_csv="Activity/Ni_areal_density_NT.csv",
    weighted_csv_path="FluxWeighted",
    file_pattern="*_flux_weighted.csv",
    nt_col="Ni_NT_atoms_per_cm2",
    nt_unc_col="Ni_NT_unc_atoms_per_cm2",
    output_filename="beam_currents_all_Ni_foils.csv"
)
