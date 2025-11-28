import curie as ci
import pandas as pd 





def calibration_IDM_30cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/AB20250922_IDM_Ba133_30cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/CD20251018_IDM_Eu152_30cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/AK20250923_IDM_Cs137_30cm.Spe')
    sp_Cs137.isotopes = ['137CS'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'137CS', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Eu152, sp_Cs137], sources=sources) #Tok vekk de to andre, 137Cs og 56Co
    #cb.plot()
    cb.saveas("Calibration/calibration_IDM_30cm.json")
calibration_IDM_30cm()





def calibration_IDM_10cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/AI20251016_IDM_Ba133_10cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/AE20251016_IDM_Eu152_10cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/AD20251016_IDM_Cs137_10cm.Spe')
    sp_Cs137.isotopes = ['137CS'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'137CS', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Eu152, sp_Cs137], sources=sources) #Tok vekk de to andre, 137Cs og 56Co
    #cb.plot()
    cb.saveas("Calibration/calibration_IDM_10cm.json")
calibration_IDM_10cm()





def calibration_IDM_40cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/BO20251017_IDM_Ba133_40cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/CF20251018_IDM_Eu152_40cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/AI20250923_IDM_Cs137_40cm.Spe')
    sp_Cs137.isotopes = ['137CS'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'137CS', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Eu152, sp_Cs137], sources=sources) #Tok vekk de to andre, 137Cs og 56Co
    #cb.plot()
    cb.saveas("Calibration/calibration_IDM_40cm.json")
calibration_IDM_40cm()





def calibration_IDM_52cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/BK20251017_IDM_Ba133_52cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/CH20251020_IDM_Eu152_52cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BT20251017_IDM_Cs137_52cm.Spe')
    sp_Cs137.isotopes = ['137CS'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'137CS', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Eu152, sp_Cs137], sources=sources) #Tok vekk de to andre, 137Cs og 56Co
    #cb.plot()
    cb.saveas("Calibration/calibration_IDM_52cm.json")
calibration_IDM_52cm()





def calibration_IDM_15cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/BB20251017_IDM_Ba133_15cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/BW20251017_IDM_Eu152_15cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BP20251017_IDM_Cs137_15cm.Spe')
    sp_Cs137.isotopes = ['137CS'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'137CS', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Eu152, sp_Cs137], sources=sources) #Tok vekk de to andre, 137Cs og 56Co
    #cb.plot()
    cb.saveas("Calibration/calibration_IDM_15cm.json")
calibration_IDM_15cm()





def calibration_IDM_20cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/BE20251017_IDM_Ba133_20cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/BY20251017_IDM_Eu152_20cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BQ20251017_IDM_Cs137_20cm.Spe')
    sp_Cs137.isotopes = ['137CS'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'137CS', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Eu152, sp_Cs137], sources=sources) #Tok vekk de to andre, 137Cs og 56Co
    #cb.plot()
    cb.saveas("Calibration/calibration_IDM_20cm.json")
calibration_IDM_20cm()




def calibration_IDM_25cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/BH20251017_IDM_Ba133_25cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/CB20251018_IDM_Eu152_25cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BR20251017_IDM_Cs137_25cm.Spe')
    sp_Cs137.isotopes = ['137CS'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'137CS', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Eu152, sp_Cs137], sources=sources) #Tok vekk de to andre, 137Cs og 56Co
    #cb.plot()
    cb.saveas("Calibration/calibration_IDM_25cm.json")
calibration_IDM_25cm()


# Mangler 45cm Eu!

def calibration_IDM_45cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/BN20251017_IDM_Ba133_45cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/CO20251028_IDM_Eu152_45cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BS20251017_IDM_Cs137_45cm.Spe')
    sp_Cs137.isotopes = ['137CS'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'137CS', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Cs137, sp_Eu152], sources=sources) #Tok vekk de to andre, 137Cs og 56Co
    #cb.plot()
    cb.saveas("Calibration/calibration_IDM_45cm.json")
calibration_IDM_45cm()