import curie as ci
import numpy as np
import os


cb = ci.Calibration("Calibration/calibration_IDM_10cm.json")  
#cb.plot()
list_of_jobs = ['Data/IDM/GH10102025_IDM_Ta12_10cm_000.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_001.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_002.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_003.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_004.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_005.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_006.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_007.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_008.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_009.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_010.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_011.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_012.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_013.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_014.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_015.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_016.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_017.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_018.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_019.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_020.Spe',
                'Data/IDM/GH10102025_IDM_Ta12_10cm_021.Spe',
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
summed_spectra.saveas("Spectroscopy/Ta_peak_summary/GH10102025_IDM_Ta12_10cm_jobs_peak_summary.csv")
sp.summarize()
summed_spectra.summarize()