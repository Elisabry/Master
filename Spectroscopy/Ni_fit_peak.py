import curie as ci
import numpy as np

Ni_isotopes = [
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


fit_peak("Calibration/calibration_IDM_45cm.json", 'Data/IDM/AO09232025_Ni08_45cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/AO09232025_Ni08_45cm_IDM_peak_summary.csv", Ni_isotopes)   # ['63ZN']
fit_peak("Calibration/calibration_IDM_45cm.json", 'Data/IDM/AP09242025_Ni09_45cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/AP09242025_Ni09_45cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_45cm.json", 'Data/IDM/AQ09242025_Ni10_45cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/AQ09242025_Ni10_45cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/AR09242025_Ni11_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/AR09242025_Ni11_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/AS09242025_Ni12_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/AS09242025_Ni12_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_25cm.json", 'Data/IDM/AT09242025_Ni13_25cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/AT09242025_Ni13_25cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_15cm.json", 'Data/IDM/AU09242025_Ni14_15cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/AU09242025_Ni14_15cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/BQ09242025_Ni08_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/BQ09242025_Ni08_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/CF09242025_Ni01_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CF09242025_Ni01_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/CG09242025_Ni02_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CG09242025_Ni02_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/CH09242025_Ni03_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CH09242025_Ni03_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/CI09242025_Ni04_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CI09242025_Ni04_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_25cm.json", 'Data/IDM/CJ09242025_Ni05_25cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CJ09242025_Ni05_25cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_25cm.json", 'Data/IDM/CK09242025_Ni06_25cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CK09242025_Ni06_25cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_25cm.json", 'Data/IDM/CL09242025_Ni07_25cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CL09242025_Ni07_25cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_25cm.json", 'Data/IDM/CT09252025_Ni08_25cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CT09252025_Ni08_25cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_25cm.json", 'Data/IDM/CU09252025_Ni09_25cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CU09252025_Ni09_25cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_25cm.json", 'Data/IDM/CV09252025_Ni10_25cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CV09252025_Ni10_25cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_25cm.json", 'Data/IDM/CW09252025_Ni11_25cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CW09252025_Ni11_25cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_25cm.json", 'Data/IDM/CX09252025_Ni12_25cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CX09252025_Ni12_25cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_15cm.json", 'Data/IDM/CY09252025_Ni13_15cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CY09252025_Ni13_15cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/CZ09252025_Ni14_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/CZ09252025_Ni14_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/DH09252025_Ni01_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DH09252025_Ni01_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/DI09252025_Ni02_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DI09252025_Ni02_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/DJ09252025_Ni03_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DJ09252025_Ni03_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/DK09252025_Ni04_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DK09252025_Ni04_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/DL09252025_Ni05_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DL09252025_Ni05_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/DM09252025_Ni06_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DM09252025_Ni06_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/DN09252025_Ni07_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DN09252025_Ni07_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/DO09252025_Ni08_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DO09252025_Ni08_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_30cm.json", 'Data/IDM/DP09252025_Ni09_30cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DP09252025_Ni09_30cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/DX09252025_Ni14_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DX09252025_Ni14_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/DY09262025_Ni13_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DY09262025_Ni13_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/DZ09262025_Ni12_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/DZ09262025_Ni12_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_15cm.json", 'Data/IDM/E09262025_Ni03_15cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/E09262025_Ni03_15cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/EA09262025_Ni14_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/EA09262025_Ni14_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_20cm.json", 'Data/IDM/EB09262025_Ni11_20cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/EB09262025_Ni11_20cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_20cm.json", 'Data/IDM/EC09262025_Ni10_20cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/EC09262025_Ni10_20cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_20cm.json", 'Data/IDM/ED09262025_Ni09_20cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/ED09262025_Ni09_20cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_20cm.json", 'Data/IDM/EE09262025_Ni08_20cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/EE09262025_Ni08_20cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_15cm.json", 'Data/IDM/EM09262025_Ni07_15cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/EM09262025_Ni07_15cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_15cm.json", 'Data/IDM/EN09262025_Ni06_15cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/EN09262025_Ni06_15cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_15cm.json", 'Data/IDM/EO09262025_Ni05_15cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/EO09262025_Ni05_15cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_15cm.json", 'Data/IDM/EP09262025_Ni04_15cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/EP09262025_Ni04_15cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_15cm.json", 'Data/IDM/EQ09262025_Ni03_15cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/EQ09262025_Ni03_15cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_15cm.json", 'Data/IDM/ER09262025_Ni02_15cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/ER09262025_Ni02_15cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_15cm.json", 'Data/IDM/ES09262025_Ni01_15cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/ES09262025_Ni01_15cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FI09282025_Ni14_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FI09282025_Ni14_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FJ09282025_Ni13_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FJ09282025_Ni13_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FK09282025_Ni12_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FK09282025_Ni12_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FL09282025_Ni11_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FL09282025_Ni11_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FN09292025_Ni10_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FN09292025_Ni10_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FO09292025_Ni09_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FO09292025_Ni09_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FP09292025_Ni08_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FP09292025_Ni08_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FQ09292025_Ni07_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FQ09292025_Ni07_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FR09292025_Ni06_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FR09292025_Ni06_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FT09302025_Ni05_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FT09302025_Ni05_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FU09302025_Ni04_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FU09302025_Ni04_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FV09302025_Ni03_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FV09302025_Ni03_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_IDM_10cm.json", 'Data/IDM/FW09302025_Ni02_10cm_IDM.Spe', "Spectroscopy/Ni_peak_summary/FW09302025_Ni02_10cm_IDM_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_DET2_10cm.json", 'Data/DET2/FS09302025_Ni01_10cm_DET2.Spe', "Spectroscopy/Ni_peak_summary/FS09302025_Ni01_10cm_DET2_peak_summary.csv", Ni_isotopes)
fit_peak("Calibration/calibration_DET2_10cm.json", 'Data/DET2/GN10142025_Det2_Ni07_10cm.Spe', "Spectroscopy/Ni_peak_summary/GN10142025_Det2_Ni07_10cm_peak_summary.csv", Ni_isotopes)



