import curie as ci
import numpy as np


cb = ci.Calibration("Calibration/calibration_IDM_10cm.json")  
#cb.plot()

sp = ci.Spectrum('Data/IDM/EJ09262025_Cu03_10cm_IDM.Spe')
sp.cb = cb
sp.isotopes = [
    '59CUg','60CUg','61CUg','62CUg','64CUg',
    '60ZNg','61ZNg','62ZNg','63ZNg','65ZNg',
    '55COg','56COg','57COg','58COg','58COm1','60COg','60COm1','61COg','62COg','62COm1',
    '53FEg','55FEg','59FEg','61FEg',
    '54MNg','56MNg',
    '56NIg','57NIg']
sp.plot()
#sp.saveas('filnavn!.png') 
sp.saveas("Spectroscopy/Cu_peak_summary/EJ09262025_Cu03_10cm_IDM_peak_summary.csv")
#sp.summarize()