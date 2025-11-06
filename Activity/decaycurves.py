import pandas as pd
import curie as ci
import numpy as np
import matplotlib.pyplot as plt
import csv

df_AB = pd.read_csv('Spectroscopy/peak_summary/AB09232025_Cu09_52cm_IDM_peak_summary.csv')
df_AI = pd.read_csv('Spectroscopy/peak_summary/AI09232025_Cu09_45cm_IDM_peak_summary.csv')
df_BK = pd.read_csv('Spectroscopy/peak_summary/BK09242025_Cu09_30cm_IDM_peak_summary.csv')
df_EY = pd.read_csv('Spectroscopy/peak_summary/EY09272025_Cu09_10cm_IDM_peak_summary.csv')
df_DV = pd.read_csv('Spectroscopy/peak_summary/DV09252025_Cu09_10cm_IDM_peak_summary.csv')

df_concat_Cu09 = pd.concat((df_AB, df_AI, df_BK, df_EY, df_DV), axis = 0)
#df_concat_Cu09.to_csv('Cu09_IDM.csv')
df_concat_Cu09.saveas("Spectroscopy/combined/Cu09_IDM_combined.csv")

dc = ci.DecayChain('62ZN', R=[[1e4, 1]], units='h')
dc.get_counts(Cu09, EoB='09/23/2025 18:35:00', peak_data= 'Spectroscopy/combined/Cu09_IDM_combined.csv')

isotopes, R, cov_R = dc.fit_R()
dc.plot(title=f'Decay Plot for {df_concat_Cu09}')
plt.show()
print(dc.R)




# for csv_file, foil_name in zip(csv_files, foil_names):
    
#     df = pd.read_csv(csv_file)

#     dc = ci.DecayChain('62ZN', R=[[1e4, 1]], units='h')
#     dc.get_counts(foil_name, EoB='09/23/2025 18:35:00', peak_data=csv_file)

#     isotopes, R, cov_R = dc.fit_R()
#     dc.plot(title=f'Decay Plot for {foil_name}')
#     plt.show()
#     print(dc.R)





# dc = ci.DecayChain("48V", R = [[1E4,0.33]], units = "h")    # For 48V
# dc = ci.DecayChain("46SC", R = [[1E4,0.33]], units = "h")    # For 46SC
# dc.get_counts("Ti10", EoB = "02/13/2017 14:21:00", peak_data = "CG240217_Ti10_18cm_50MeV.csv")
# isotopes, R, cov_R = dc.fit_R()
# dc.plot()


# for R må man bare velge en random R så finner curie resten (curie regner den ut) bruk 3E5, 
# men det går an å bruke A0 for monitorreaksjonene, A0 er end of beam activity. fit A0 funksjonen

# viktig å endre til riktig tidspunkt! decay_curves_Zr_foils_curie.py i Elises koder.

# DET2 har blitt målt uten hull, men det kan være det går fint. Eller det kan være at vi må ta hensyn til det.

# her fra hannah: 
# dfs = [pd.read_csv(f) for f in csv_files]
# combined = pd.concat(dfs, ignore_index=True)
# combined.to_csv("combined.csv", index=False)


# i master training på decaycurve.py

# Det er monitor vi er interssert i nå! på Cu og Ni foliene.

# foil_class.py og foil_class_ for_ xs_calc.py i Elises git hub