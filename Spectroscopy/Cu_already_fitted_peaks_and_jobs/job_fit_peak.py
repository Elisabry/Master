import curie as ci
import numpy as np


cb = ci.Calibration("Calibration/calibration_IDM_10cm.json")  
#cb.plot()
list_of_jobs = ["Data/IDM/GK10152025_IDM_Cu13_10cm_000.Spe",
                "Data/IDM/GK10152025_IDM_Cu13_10cm_001.Spe", 
                "Data/IDM/GK10152025_IDM_Cu13_10cm_002.Spe",
                "Data/IDM/GK10152025_IDM_Cu13_10cm_003.Spe",
                "Data/IDM/GK10152025_IDM_Cu13_10cm_004.Spe",
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
    "60ZN", "62ZN", "63ZN", "64ZN", "65ZN",
    "59CU", "61CU", "62CU", "64CU", 
    "56NI", "57NI",
    "56CO", "58CO", 
]

summed_spectra.isotopes = [
    "60ZN", "62ZN", "63ZN", "64ZN", "65ZN",
    "59CU", "61CU", "62CU", "64CU", 
    "56NI", "57NI",
    "56CO", "58CO", 
]

print(type(sp))
print(type(summed_spectra))

summed_spectra.plot()
# sp.plot()
#sp.saveas('filnavn!.png') 
#sp.saveas("CC220217_Ti06_18cm_50MeV.csv")
sp.summarize()
summed_spectra.summarize()