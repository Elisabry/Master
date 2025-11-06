import curie as ci
import numpy as np


cb = ci.Calibration("Calibration/calibration_IDM_30cm.json")  
#cb.plot()

sp = ci.Spectrum('Data/IDM/FW09302025_Ni02_10cm_IDM.Spe')
sp.cb = cb
sp.isotopes = ["56CO","56NI","57CO", "58CO", "55CO", "57NI"] 
sp.plot()
#sp.saveas('filnavn!.png') 
#sp.saveas("CC220217_Ti06_18cm_50MeV.csv")
sp.summarize()

