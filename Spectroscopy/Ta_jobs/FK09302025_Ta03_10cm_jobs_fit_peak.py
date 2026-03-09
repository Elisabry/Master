import curie as ci
import numpy as np
import os


cb = ci.Calibration("Calibration/calibration_LEPS_10cm.json")  
#cb.plot()
list_of_jobs = ['Data/LEPS/FK09302025_Ta03_10cm_000.Spe',
                'Data/LEPS/FK09302025_Ta03_10cm_001.Spe',
                'Data/LEPS/FK09302025_Ta03_10cm_002.Spe',
                'Data/LEPS/FK09302025_Ta03_10cm_003.Spe',
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
    '177Wg','178W','179Wg','179Wm','181Wg',
    '173TAg','174TAg','175TAg','176TAg','177TAg','178TAg','180TAg',
    '172HFg','173HFg','175HFg','180HFm','172LUm','176LUm','178LUg','179LUg'
    ]


summed_spectra.isotopes = [
    '177Wg','178W','179Wg','179Wm','181Wg',
    '173TAg','174TAg','175TAg','176TAg','177TAg','178TAg','180TAg',
    '172HFg','173HFg','175HFg','180HFm','172LUm','176LUm','178LUg','179LUg'
    ]



print(type(sp))
print(type(summed_spectra))

summed_spectra.plot()
# sp.plot()
#sp.saveas('filnavn!.png') 
summed_spectra.saveas("Spectroscopy/Ta_peak_summary/FK09302025_Ta03_10cm_LEPS_jobs_peak_summary.csv")
sp.summarize()
summed_spectra.summarize()