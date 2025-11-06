import curie as ci
import numpy as np


cb = ci.Calibration("Calibration/calibration_IDM_30cm.json")  
#cb.plot()

sp = ci.Spectrum('Data/IDM/BL09242025_Cu10_30cm_IDM.Spe')
sp.cb = cb
sp.isotopes = [
    "60ZN", "62ZN", "63ZN", "64ZN", "65ZN",
    "59CU", "61CU", "62CU", "64CU", 
    "56NI", "57NI",
    "56CO", "58CO", 
    "40K"
]
sp.plot()
#sp.saveas('filnavn!.png') 
sp.saveas("Spectroscopy/peak_summary/BL09242025_Cu10_30cm_IDM_peak_summary.csv")