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
    '59CUg','60CUg','61CUg','62CUg','64CUg',
    '60ZNg','61ZNg','62ZNg','63ZNg','65ZNg',
    '55COg','56COg','57COg','58COg','58COm1','60COg','60COm1','61COg','62COg','62COm1',
    '53FEg','55FEg','59FEg','61FEg',
    '54MNg','56MNg',
    '56NIg','57NIg']

summed_spectra.isotopes = [
    '59CUg','60CUg','61CUg','62CUg','64CUg',
    '60ZNg','61ZNg','62ZNg','63ZNg','65ZNg',
    '55COg','56COg','57COg','58COg','58COm1','60COg','60COm1','61COg','62COg','62COm1',
    '53FEg','55FEg','59FEg','61FEg',
    '54MNg','56MNg',
    '56NIg','57NIg']

#print(type(sp))
print(type(summed_spectra))

summed_spectra.plot()
# sp.plot()
#sp.saveas('filnavn!.png') 
summed_spectra.saveas("Spectroscopy/Cu_peak_summary/GK10152025_IDM_Cu13_10cm_jobs_peak_summary.csv")
#sp.summarize()
summed_spectra.summarize()