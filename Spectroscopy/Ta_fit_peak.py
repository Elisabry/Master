import curie as ci
import numpy as np

cu_isotopes = [
        "62ZN", "63ZN", "65ZN",
        "59CU", "61CU", "62CU", "64CU", 
        "56NI", "57NI",
        "56CO", "58CO"]

def fit_peak(calibration_file, spectrum_file, peak_data_filename, isotopes):
    cb = ci.Calibration(calibration_file)  
    sp = ci.Spectrum(spectrum_file)
    sp.cb = cb
    sp.isotopes = isotopes
    sp.plot()
    sp.saveas(peak_data_filename)


fit_peak("Calibration/calibration_IDM_52cm.json", 'Data/IDM/AB09232025_Cu09_52cm_IDM.Spe', "Spectroscopy/Cu_peak_summary/AB09232025_Cu09_52cm_IDM_peak_summary.csv", cu_isotopes)   # ['63ZN']
fit_peak("Calibration/calibration_IDM_52cm.json", 'Data/IDM/BU09242025_Cu04_52cm_IDM.Spe', "Spectroscopy/Cu_peak_summary/BU09242025_Cu04_52cm_IDM_peak_summary.csv", cu_isotopes)

