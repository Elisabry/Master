import curie as ci
import numpy as np
import os


cb = ci.Calibration("Calibration/calibration_DET2_10cm.json")  
#cb.plot()
list_of_jobs = ['Data/DET2/GM10142025_Det2_Ni08_10cm_000.Spe',
                'Data/DET2/GM10142025_Det2_Ni08_10cm_001.Spe',
                'Data/DET2/GM10142025_Det2_Ni08_10cm_002.Spe',
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

Ni_isotopes = [
    '59CUg','60CUg','61CUg','62CUg','64CUg',
    '54COm1','55COg','56COg','57COg','58COg','58COm','58COm1','60COg','60COm','60COm1','61COg','62COg','62COm1',
    '53FEg','53FEm1','55FEg','59FEg','61FEg',
    '50MNm1','51MNg','52MNg','52MNm','52MNm1','54MNg','56MNg',
    '49CRg','51CRg','55CRg',
    '47Vg',
    '56NIg','57NIg']

summed_spectra.isotopes = [
    '59CUg','60CUg','61CUg','62CUg','64CUg',
    '54COm1','55COg','56COg','57COg','58COg','58COm','58COm1','60COg','60COm','60COm1','61COg','62COg','62COm1',
    '53FEg','53FEm1','55FEg','59FEg','61FEg',
    '50MNm1','51MNg','52MNg','52MNm','52MNm1','54MNg','56MNg',
    '49CRg','51CRg','55CRg',
    '47Vg',
    '56NIg','57NIg']

print(type(sp))
print(type(summed_spectra))

summed_spectra.plot()
# sp.plot()
#sp.saveas('filnavn!.png') 
summed_spectra.saveas("Spectroscopy/Ni_peak_summary/GM10142025_Det2_Ni08_10cm_jobs_peak_summary.csv")
sp.summarize()
summed_spectra.summarize()