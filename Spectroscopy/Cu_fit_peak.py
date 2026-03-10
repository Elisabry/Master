import curie as ci
import numpy as np

cu_isotopes = [
    '59CUg','60CUg','61CUg','62CUg','64CUg',
    '60ZNg','61ZNg','62ZNg','63ZNg','65ZNg',
    '55COg','56COg','57COg','58COg','58COm1','60COg','60COm1','61COg','62COg','62COm1',
    '53FEg','55FEg','59FEg','61FEg',
    '54MNg','56MNg',
    '56NIg','57NIg']



# [
#         "62ZN", "63ZN", "65ZN",
#         "59CU", "61CU", "62CU", "64CU", 
#         "56NI", "57NI",
#         "56CO", "58CO"]

def fit_peak(calibration_file, spectrum_file, peak_data_filename, isotopes):
    cb = ci.Calibration(calibration_file)  
    sp = ci.Spectrum(spectrum_file)
    sp.cb = cb
    sp.isotopes = isotopes
    sp.fit_config = {'xrays': True, 'E_min':20}
    #sp.plot()
    sp.saveas(peak_data_filename)


fit_peak("Calibration/calibration_IDM_45cm.json", 'Data/IDM/CE09242025_Cu07_45cm_IDM.Spe', "Spectroscopy/Cu_peak_summary/CE09242025_Cu07_45cm_IDM_peak_summary.csv", cu_isotopes)   # ['63ZN']
fit_peak("Calibration/calibration_DET2_50cm.json", 'Data/DET2/AN09232025_Cu08_50cm_DET2.Spe', "Spectroscopy/Cu_peak_summary/AN09232025_Cu08_50cm_DET2_peak_summary.csv", cu_isotopes)  
fit_peak("Calibration/calibration_DET2_50cm.json", 'Data/DET2/BD09242025_Cu10_50cm_DET2.Spe', "Spectroscopy/Cu_peak_summary/BD09242025_Cu10_50cm_DET2_peak_summary.csv", cu_isotopes)  
fit_peak("Calibration/calibration_LEPS_10cm.json", 'Data/LEPS/AU09242025_Cu09_10cm_LEPS.Spe', "Spectroscopy/Cu_peak_summary/AU09242025_Cu09_10cm_LEPS_peak_summary.csv", cu_isotopes)  
fit_peak("Calibration/calibration_LEPS_10cm.json", 'Data/LEPS/BP09242025_Cu11_10cm_LEPS.Spe', "Spectroscopy/Cu_peak_summary/BP09242025_Cu11_10cm_LEPS_peak_summary.csv", cu_isotopes)  


