import curie as ci
import numpy as np

# KOMPLETT ISOTOPLISTE!

cb = ci.Calibration("Calibration/calibration_IDM_45cm.json")  
#cb.plot()

sp = ci.Spectrum('Data/IDM/CA09242025_Cu03_45cm_IDM.Spe')
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
sp.saveas("Spectroscopy/peak_summary/CA09242025_Cu03_45cm_IDM_peak_summary.csv")