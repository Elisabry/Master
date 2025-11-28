import curie as ci
import pandas as pd 




def calibration_DET2_10cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/BV20251017_Det2_Ba133_10cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/CL20251020_Det2_Eu152_10cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BA20251017_Det2_Cs137_10cm.Spe')
    sp_Cs137.isotopes = ['137CS'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'137CS', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Eu152, sp_Cs137], sources=sources) 
    #cb.plot()
    cb.saveas("Calibration/calibration_DET2_10cm.json") # Saving in the Calibration folder.
calibration_DET2_10cm()




def calibration_DET2_18cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/BX20251017_Det2_Ba133_18cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/CK20251020_Det2_Eu152_18cm.Spe") # Det var flere av denne
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BC20251017_Det2_Cs137_18cm.Spe')
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
    cb.saveas("Calibration/calibration_DET2_18cm.json")
calibration_DET2_18cm()




def calibration_DET2_24cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/BZ20251017_Det2_Ba133_24cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/CM20251020_Det2_Eu152_24cm.Spe") 
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BD20251017_Det2_Cs137_24cm.Spe')
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
    cb.saveas("Calibration/calibration_DET2_24cm.json")
calibration_DET2_24cm()




# Mangler Eu

def calibration_DET2_30cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/CA20251018_Det2_Ba133_30cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/CR20251028_Det2_Eu152_30cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BF20251017_Det2_Cs137_30cm.Spe')
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
    cb.saveas("Calibration/calibration_DET2_30cm.json")
calibration_DET2_30cm()





def calibration_DET2_40cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/CC20251018_Det2_Ba133_40cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/CQ20251028_Det2_Eu152_40cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BG20251017_Det2_Cs137_40cm.Spe')
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
    cb.saveas("Calibration/calibration_DET2_40cm.json")
calibration_DET2_40cm()





def calibration_DET2_50cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/AD20250922_Det2_Ba133_50cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/AL20250923_Det2_Eu152_50cm.Spe") 
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BJ20251017_Det2_Cs137_50cm.Spe')
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
    cb.saveas("Calibration/calibration_DET2_50cm.json")
calibration_DET2_50cm()






def calibration_DET2_60cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/AF20250922_Det2_Ba133_60cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/AN20250923_Det2_Eu152_60cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BJ20251017_Det2_Cs137_50cm.Spe')
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
    cb.saveas("Calibration/calibration_DET2_60cm.json")
calibration_DET2_60cm()






def calibration_DET2_70cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/CG20251018_Det2_Ba133_70cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/CS20251028_Det2_Eu152_70cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BM20251017_Det2_Cs137_70cm.Spe')
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
    cb.saveas("Calibration/calibration_DET2_70cm.json")
calibration_DET2_70cm() 



def calibration_DET2_80cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/CI20251020_Det2_Ba133_80cm_000.Spe") # Hvordan slår jeg sammen filer?
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Eu152 = ci.Spectrum("Calibration/BU20251017_Det2_Eu152_80cm.Spe") # Det er flere av denne
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Cs137 = ci.Spectrum('Calibration/BI20251017_Det2_Cs137_80cm.Spe')
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
    cb.saveas("Calibration/calibration_DET2_80cm.json")
calibration_DET2_80cm()