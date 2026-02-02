import curie as ci
import numpy as np

ta_isotopes = [
        "175TA", "176TA", "177TA", "178TA", "180TA", 
        "173HF", "175HF"]

def fit_peak(calibration_file, spectrum_file, peak_data_filename, isotopes):
    cb = ci.Calibration(calibration_file)  
    sp = ci.Spectrum(spectrum_file)
    sp.cb = cb
    sp.isotopes = isotopes
    sp.plot()
    sp.saveas(peak_data_filename)


fit_peak("Calibration/calibration_DET2_80cm.json", 'Data/DET2/AB09232025_Ta09_80cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/AB09232025_Ta09_80cm_DET2_peak_summary.csv", ta_isotopes)   # ['63ZN']
fit_peak("Calibration/calibration_DET2_60cm.json", 'Data/DET2/AD09232025_Ta11_60cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/AD09232025_Ta11_60cm_DET2_peak_summary.csv", ta_isotopes)
fit_peak("Calibration/calibration_DET2_18cm.json", 'Data/DET2/AF09232025_Ta13_18cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/AF09232025_Ta13_18cm_DET2_peak_summary.csv", ta_isotopes)
fit_peak("Calibration/calibration_DET2_50cm.json", 'Data/DET2/AJ09232025_Ta10_50cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/AJ09232025_Ta10_50cm_DET2_peak_summary.csv", ta_isotopes)
fit_peak("Calibration/calibration_DET2_18cm.json", 'Data/DET2/AL09232025_Ta12_18cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/AL09232025_Ta12_18cm_DET2_peak_summary.csv", ta_isotopes)
fit_peak("Calibration/calibration_DET2_18cm.json", 'Data/DET2/AP09242025_Ta09_18cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/AP09242025_Ta09_18cm_DET2_peak_summary.csv", ta_isotopes)
fit_peak("Calibration/calibration_DET2_18cm.json", 'Data/DET2/AR09242025_Ta11_18cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/AR09242025_Ta11_18cm_DET2_peak_summary.csv", ta_isotopes)
fit_peak("Calibration/calibration_DET2_18cm.json", 'Data/DET2/AT09242025_Ta13_18cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/AT09242025_Ta13_18cm_DET2_peak_summary.csv", ta_isotopes)
fit_peak("Calibration/calibration_DET2_18cm.json", 'Data/DET2/AV09242025_Ta08_18cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/AV09242025_Ta08_18cm_DET2_peak_summary.csv", ta_isotopes)
fit_peak("Calibration/calibration_DET2_18cm.json", 'Data/DET2/AX09242025_Ta10_18cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/AX09242025_Ta10_18cm_DET2_peak_summary.csv", ta_isotopes)
fit_peak("Calibration/calibration_DET2_10cm.json", 'Data/DET2/AZ09242025_Ta12_10cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/AZ09242025_Ta12_10cm_DET2_peak_summary.csv", ta_isotopes)
fit_peak("Calibration/calibration_DET2_18cm.json", 'Data/DET2/BB09242025_Ta08_18cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/BB09242025_Ta08_18cm_DET2_peak_summary.csv", ta_isotopes)
fit_peak("Calibration/calibration_DET2_10cm.json", 'Data/DET2/BF09242025_Ta12_10cm_DET2.Spe', "Spectroscopy/Ta_peak_summary/BF09242025_Ta12_10cm_DET2_peak_summary.csv", ta_isotopes)

