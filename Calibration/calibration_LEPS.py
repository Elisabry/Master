import curie as ci
import pandas as pd 


# Mangler Eu og Cs

def calibration_LEPS_30cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/AM20250923_LEPS_Ba133_30cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    #sp_Eu152 = ci.Spectrum("Calibration/CL20251020_Det2_Eu152_10cm.Spe")
    #sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    #sp_Cs137 = ci.Spectrum('Calibration/BA20251017_Det2_Cs137_10cm.Spe')
    #sp_Cs137.isotopes = ['137CS'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'137CS', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133], sources=sources) #Tok vekk de to andre, 137Cs og 56Co
    #cb.plot()
    cb.saveas("Calibration/calibration_LEPS_30cm.json")
calibration_LEPS_30cm()