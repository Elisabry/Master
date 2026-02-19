import curie as ci
import numpy as np
import os


cb = ci.Calibration("Calibration/calibration_IDM_10cm.json")  
#cb.plot()
list_of_jobs = ['Data/IDM/GE10072025_IDM_Ta09_10cm_000.Spe',
                'Data/IDM/GE10072025_IDM_Ta09_10cm_001.Spe',
                'Data/IDM/GE10072025_IDM_Ta09_10cm_002.Spe',
                'Data/IDM/GE10072025_IDM_Ta09_10cm_003.Spe',
                'Data/IDM/GE10072025_IDM_Ta09_10cm_004.Spe',
                'Data/IDM/GE10072025_IDM_Ta09_10cm_005.Spe',
                ]

list_of_spectra = []
for job in list_of_jobs: 
    sp = ci.Spectrum(job)
    sp.cb = cb
    list_of_spectra.append(sp)

print(list_of_spectra)

summed_spectra = list_of_spectra[0]
for i, spec in enumerate(list_of_spectra[1:], start=1):
    summed_spectra += spec

sp.isotopes = [
        "40K",
        "177W", "178W", "181W", 
        "175TA", "176TA", "177TA", "178TA", "180TA", 
        "173HF", "175HF"]

summed_spectra.isotopes = [
        "40K",
        "177W", "178W", "181W", 
        "175TA", "176TA", "177TA", "178TA", "180TA", 
        "173HF", "175HF"]



print(type(sp))
print(type(summed_spectra))

summed_spectra.plot()
# sp.plot()
#sp.saveas('filnavn!.png') 
summed_spectra.saveas("Spectroscopy/Ta_peak_summary/GE10072025_IDM_Ta09_10cm_jobs_peak_summary.csv")
sp.summarize()
summed_spectra.summarize()