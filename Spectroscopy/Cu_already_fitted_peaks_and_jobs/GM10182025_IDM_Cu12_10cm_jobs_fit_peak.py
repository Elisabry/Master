import curie as ci
import numpy as np


cb = ci.Calibration("Calibration/calibration_IDM_10cm.json")  
#cb.plot()
list_of_jobs = ['Data/IDM/GM10182025_IDM_Cu12_10cm_000.Spe',
                'Data/IDM/GM10182025_IDM_Cu12_10cm_001.Spe',
                'Data/IDM/GM10182025_IDM_Cu12_10cm_002.Spe',
                'Data/IDM/GM10182025_IDM_Cu12_10cm_003.Spe',
                'Data/IDM/GM10182025_IDM_Cu12_10cm_004.Spe',
                'Data/IDM/GM10182025_IDM_Cu12_10cm_005.Spe',
                'Data/IDM/GM10182025_IDM_Cu12_10cm_006.Spe',
                'Data/IDM/GM10182025_IDM_Cu12_10cm_007.Spe',
                'Data/IDM/GM10182025_IDM_Cu12_10cm_008.Spe',
                'Data/IDM/GM10182025_IDM_Cu12_10cm_009.Spe',
                'Data/IDM/GM10182025_IDM_Cu12_10cm_010.Spe',
                'Data/IDM/GM10182025_IDM_Cu12_10cm_011.Spe',
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

#print(type(sp))
print(type(summed_spectra))

summed_spectra.plot()
# sp.plot()
#sp.saveas('filnavn!.png') 
summed_spectra.saveas("Spectroscopy/Cu_peak_summary/GM10182025_IDM_Cu12_10cm_jobs_peak_summary.csv")
#sp.summarize()
summed_spectra.summarize()