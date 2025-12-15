import curie as ci
import numpy as np

# KOMPLETT ISOTOPLISTE! Selv om mange topper er falske:(

cb = ci.Calibration("Calibration/calibration_IDM_30cm.json")  
#cb.plot()

sp = ci.Spectrum('Data/IDM/DG09252025_Cu07_30cm_IDM.Spe')
sp.cb = cb
sp.isotopes = [
    "60ZN", "62ZN", "63ZN", "65ZN", "69ZN", "71ZN", "72ZN",
    "60CU", "61CU", "62CU", "64CU", "66CU", "67CU",
    "56NI", "57NI", "65NI", "66NI",
    "55CO", "56CO", "57CO", "58CO", "60CO", "61CO",
    "40K", "41K", "42K", "43K", "44K",
    "52FE", "53FE", "55FE", "59FE", "61FE",
    "48CR", "49CR", "51CR", "55CR", "56CR",
    "45CA", "47CA", "49CA",
    "44SC", "46SC", "47SC", "48SC", 
    "51MN", "52MN", "54MN", "56MN",
    "64GA", "65GA", "66GA", "67GA", "68GA", "70GA",
    "68GE", "69GE", "71GE",
    "69AS","70AS", "71AS", 
    "41AR", "42AR", "43AR", 
    "38CL", "39CL", "40CL",
    "37S", "38S"
]
sp.plot()

sp.saveas("Spectroscopy/peak_summary/DG09252025_Cu07_30cm_IDM_peak_summary.csv")
#sp.saveas('filnavn!.png') 
#sp.summarize()