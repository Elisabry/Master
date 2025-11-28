import curie as ci
import pandas as pd 




def calibration_LEPS_09cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/DP20251103_LEPS_Ba133_9cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Co57 = ci.Spectrum("Calibration/DO20251103_LEPS_Co57_9cm.Spe")
    sp_Co57.isotopes = ["57CO"]
    #sp_Eu152.plot()

    sp_Am241 = ci.Spectrum('Calibration/DC20251030_LEPS_Am241_9cm.Spe')
    sp_Am241.isotopes = ['241AM'] 
    #sp_Cs137.plot()

    sp_Cd109 = ci.Spectrum('Calibration/DV20251105_LEPS_Cd109_09cm.Spe')
    sp_Cd109.isotopes = ['109CD'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'109CD', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},      # Er dette riktig dato og A0?
               {'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'241AM', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}       # Her og må vi fikse tall
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Cd109, sp_Co57, sp_Am241], sources=sources) 
    #cb.plot()
    cb.saveas("Calibration/calibration_LEPS_09cm.json")
calibration_LEPS_09cm()





def calibration_LEPS_10cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/DA20251030_LEPS_Ba133_10cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Co57 = ci.Spectrum("Calibration/DI20251030_LEPS_Co57_10cm.Spe")
    sp_Co57.isotopes = ["57CO"]
    #sp_Eu152.plot()

    sp_Am241 = ci.Spectrum('Calibration/DB20251030_LEPS_Am241_10cm.Spe')
    sp_Am241.isotopes = ['241AM'] 
    #sp_Cs137.plot()

    sp_Cd109 = ci.Spectrum('Calibration/DQ20251103_LEPS_Cd109_10cm.Spe')
    sp_Cd109.isotopes = ['109CD'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'109CD', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},      # Er dette riktig dato og A0?
               {'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'241AM', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}       # Her og må vi fikse tall
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Cd109, sp_Am241, sp_Co57], sources=sources) 
    #cb.plot()
    cb.saveas("Calibration/calibration_LEPS_10cm.json")
calibration_LEPS_10cm()





def calibration_LEPS_15cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/CX20251029_LEPS_Ba133_15cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Co57 = ci.Spectrum("Calibration/DN20251103_LEPS_Co57_15cm.Spe")
    sp_Co57.isotopes = ["57CO"]
    #sp_Eu152.plot()

    sp_Am241 = ci.Spectrum('Calibration/DD20251030_LEPS_Am241_15cm.Spe')
    sp_Am241.isotopes = ['241AM'] 
    #sp_Cs137.plot()

    sp_Cd109 = ci.Spectrum('Calibration/DU20251105_LEPS_Cd109_15cm.Spe')
    sp_Cd109.isotopes = ['109CD'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'109CD', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},      # Er dette riktig dato og A0?
               {'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'241AM', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}       # Her og må vi fikse tall
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Cd109, sp_Am241, sp_Cd109], sources=sources) 
    #cb.plot()
    cb.saveas("Calibration/calibration_LEPS_15cm.json")
calibration_LEPS_15cm()





def calibration_LEPS_20cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/CV20251029_LEPS_Ba133_20cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Co57 = ci.Spectrum("Calibration/DL20251031_LEPS_Co57_20cm.Spe")
    sp_Co57.isotopes = ["57CO"]
    #sp_Eu152.plot()

    sp_Am241 = ci.Spectrum('Calibration/DE20251030_LEPS_Am241_20cm.Spe')
    sp_Am241.isotopes = ['241AM'] 
    #sp_Cs137.plot()

    sp_Cd109 = ci.Spectrum('Calibration/DS20251104_LEPS_Cd109_20cm.Spe')
    sp_Cd109.isotopes = ['109CD'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'109CD', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},      # Er dette riktig dato og A0?
               {'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'241AM', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}       # Her og må vi fikse tall
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Cd109, sp_Co57, sp_Am241], sources=sources) 
    #cb.plot()
    cb.saveas("Calibration/calibration_LEPS_20cm.json")
calibration_LEPS_20cm()






def calibration_LEPS_30cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/CZ20251030_LEPS_Ba133_30cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Co57 = ci.Spectrum("Calibration/DK20251031_LEPS_Co57_30cm.Spe")
    sp_Co57.isotopes = ["57CO"]
    #sp_Eu152.plot()

    sp_Am241 = ci.Spectrum('Calibration/DF20251030_LEPS_Am241_30cm.Spe')
    sp_Am241.isotopes = ['241AM'] 
    #sp_Cs137.plot()

    sp_Cd109 = ci.Spectrum('Calibration/DT20251105_LEPS_Cd109_30cm.Spe')
    sp_Cd109.isotopes = ['109CD'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'109CD', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},      # Er dette riktig dato og A0?
               {'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'241AM', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}       # Her og må vi fikse tall
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Cd109, sp_Am241, sp_Co57], sources=sources) 
    #cb.plot()
    cb.saveas("Calibration/calibration_LEPS_30cm.json")
calibration_LEPS_30cm()





def calibration_LEPS_40cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/CT20251029_LEPS_Ba133_40cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Co57 = ci.Spectrum("Calibration/DM20251103_LEPS_Co57_40cm.Spe")
    sp_Co57.isotopes = ["57CO"]
    #sp_Eu152.plot()

    sp_Am241 = ci.Spectrum('Calibration/DH20251030_LEPS_Am241_40cm.Spe')
    sp_Am241.isotopes = ['241AM'] 
    #sp_Cs137.plot()

    sp_Cd109 = ci.Spectrum('Calibration/DR20251104_LEPS_Cd109_40cm.Spe')
    sp_Cd109.isotopes = ['109CD'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               {'isotope':'109CD', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},      # Er dette riktig dato og A0?
               {'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'241AM', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}       # Her og må vi fikse tall
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Cd109, sp_Am241, sp_Co57], sources=sources) 
    #cb.plot()
    cb.saveas("Calibration/calibration_LEPS_40cm.json")
calibration_LEPS_40cm()





def calibration_LEPS_60cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("Calibration/CP20251028_LEPS_Ba133_60cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()
 
    sp_Co57 = ci.Spectrum("Calibration/DJ20251031_LEPS_Co57_60cm.Spe")
    sp_Co57.isotopes = ["57CO"]
    #sp_Eu152.plot()

    sp_Am241 = ci.Spectrum('Calibration/DG20251030_LEPS_Am241_60cm.Spe')
    sp_Am241.isotopes = ['241AM'] 
    #sp_Cs137.plot()

    #sp_Cd109 = ci.Spectrum('Calibration/DR20251104_LEPS_Cd109_40cm.Spe')         # Denne mangler
    #sp_Cd109.isotopes = ['109CD'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.859E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'152EU', 'A0':3.822E4, 'ref_date':'03/01/2019 12:00:00'},
               #{'isotope':'109CD', 'A0':3.670E4, 'ref_date':'03/01/2019 12:00:00'},      # Er dette riktig dato og A0?
               {'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'241AM', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}       # Her og må vi fikse tall
               ]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Am241, sp_Co57], sources=sources) 
    #cb.plot()
    cb.saveas("Calibration/calibration_LEPS_40cm.json")
calibration_LEPS_60cm()




