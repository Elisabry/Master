import matplotlib.pyplot as plt
from Cross_Section import calculate_cross_section, load_file_with_uncertainty
from Exfor import Exfor
from Talys import Talys
from Tendl import Tendl
import os
from collections import OrderedDict


exfor = Exfor(os.getcwd() + '/../exfor/')
talys = Talys(os.getcwd() + '/../talys_analysis/')
tendl_ta = Tendl({"Ta181": 0.9998799, "Ta180m": 0.0001201}, 'proton')


path_to_cross_section_figures = os.getcwd()+'/../Figures/cross_section_figures/'

def set_title(element, isotope, independent=False):
    if independent:
        str = element + '(p,x)' + isotope + ' - independent'
    else:
        str = element + '(p,x)' + isotope + ' - cumulative'
    plt.title(str)
    plt.xlabel('Energy (MeV)')
    plt.ylabel('Cross section (mb)')

def set_legend(fontsize='small', loc='best'):
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), fontsize=fontsize, loc=loc)














# ------------ Monitor isotopes ------------

def cu_62ZN_monitor():
    element='Cu'; isotope='62ZN';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Cu_62Zn_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

# cu_62ZN_monitor()

def cu_63ZN_monitor():
    element='Cu'; isotope='63ZN';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Cu_63Zn_ind.txt')  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#cu_63ZN_monitor()


def cu_65ZN_monitor():
    element='Cu'; isotope='65ZN';
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Cu_65Zn_ind.txt')  # plotting the EXFOR data for comparison.
    maxE = 60
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    set_legend(fontsize='5')    
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show() 

#cu_65ZN_monitor()

def cu_56CO_monitor():
    element='Cu'; isotope='56CO';
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Cu_56Co_cumu.txt')  # plotting the EXFOR data for comparison.
    maxE = 60
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    set_legend(fontsize='5')    
    name = element+'_'+isotope+'_cumu.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#cu_56CO_monitor()

def cu_58CO_monitor():
    element='Cu'; isotope='58CO';
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Cu_58Co_cumu.txt')  # plotting the EXFOR data for comparison.
    maxE = 60
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    set_legend(fontsize='5')    
    name = element+'_'+isotope+'_cumu.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#cu_58CO_monitor()

def ni_57NI_monitor():
    element='Ni'; isotope='57NI';
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Ni_57Ni_cumu.txt')  # plotting the EXFOR data for comparison.
    maxE = 60
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    set_legend(fontsize='5')    
    name = element+'_'+isotope+'_cumu.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ni_57NI_monitor()























# ------------ Ta isotopes ------------

def ta_177W_independet():             # noen av this work sporer av, falske peaker?
    element='Ta'; isotope='177W'; 
    Z = '74'; A = '177'
    maxE = 60; maxXs = 800
    exfor.plotExforDataFromFilename('Ta_177W_ind.txt')  # plotting the EXFOR data for comparison.
    calculate_cross_section(element, isotope)
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')    
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ta_177W_independet()

    
def ta_178W_independent():                 # denne har kun x-ray. det er noen av this work som sporer av falske peaker?
    element='Ta'; isotope='178W';
    Z = '74'; A = '178'
    maxE = 60; maxXs = 850
    exfor.plotExforDataFromFilename('Ta_178W_ind.txt')  # plotting the EXFOR data for comparison.
    calculate_cross_section(element, isotope)
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')                           
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()
    plt.show()

#ta_178W_independent()  



def ta_179Wg_independent():                # denne kjører ikke
    element='Ta'; isotope='179Wg';
    Z = '74'; A = '179'
    maxE = 60; maxXs = 850
    #exfor.plotExforDataFromFilename('Ta_179Wg_ind.txt')  #  INGEN EXFOR DATA TLGJENGELIG!
    calculate_cross_section(element, isotope)
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')                           
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()
    plt.show()

#ta_179Wg_independent()  


def ta_179Wm1_independent():                      # Denne kjører, men this work er off
    element='Ta'; isotope='179Wm1';
    Z = '74'; A = '179'
    maxE = 60; maxXs = 5000
    # exfor.plotExforDataFromFilename('Ta_179Wm1_ind.txt')  # INGEN EXFOR DATA TLGJENGELIG!
    calculate_cross_section(element, isotope)
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')                           
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ta_179Wm1_independent()
 


def ta_181W_independent():         # this work er off
    element='Ta'; isotope='181W';
    Z = '74'; A = '181'
    maxE = 60; maxXs = 200
    #exfor.plotExforDataFromFilename('Ta_177W_ind.txt')  # Det finnes ingen EXFOR data for Ta-181W.
    calculate_cross_section(element, isotope)
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')    
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ta_181W_independent()  


def ta_175TA_independent():
    element='Ta'; isotope='175TA';
    Z = '73'; A = '175'
    maxE = 100; maxXs = 80
    exfor.plotExforDataFromFilename('Ta_175TA_ind.txt')  # det står at den er cumulative i EXFOR
    calculate_cross_section(element, isotope)
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')    
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

ta_175TA_independent()  


def ta_176TA_independent():           # maybe this is cumulative?
    element='Ta'; isotope='176TA';
    Z = '73'; A = '176'
    maxE = 200; maxXs = 500
    exfor.plotExforDataFromFilename('Ta_176TA_ind.txt')  # plotting the EXFOR data for comparison.
    calculate_cross_section(element, isotope)
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')    
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ta_176TA_independent() 


def ta_177TA_cumulative():

    element='Ta'; isotope='177TA';
    Z = '73'; A = '177'
    maxE = 60; maxXs = 800
    betaplus_decay_chain = {'isotope': ['74', 1.0, None]} 
    # {isotope: [productZ, branchingRatio isomerLevel]} #beta+/beta- for tendl feedomg
    # {isotope: [branchingRatio isomerLevel]} #isomer for tendl feedomg
    #exfor.plotExforDataFromFilename('Ta_177TA_cumu.txt')  # plotting the EXFOR data for comparison.
    calculate_cross_section(element, isotope) 
    exfor.plotExforDataFromFilename('Ta_177TA_cumu.txt', setLegend=False, maxE=maxE)
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element, 
                    isomerLevel = None,
                    betaFeeding = 'beta+', # only beta+ beta-
                    branchingRatio = 1.0,
                    parentIsomerLevel = None)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    tendl_ta.plotTendl23Unique_feeding(productZ=Z, productA=A, isomerLevel = None,  
                                  betaPlusDecayChain = betaplus_decay_chain, betaMinusDecayChain = None, isomerDecayChain = None, 
                                  color=None, lineStyle=None)
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')    
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_cumu.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ta_177TA_cumulative() 


def ta_178TA_cumulative():     # maybe this is independent? since there is no 178w.
    element='Ta'; isotope='178TA';
    Z = '73'; A = '178'
    maxE = 60; maxXs = 1000      # Hvorfor er usikkerheten så sykt høy??!
    betaplus_decay_chain = {'isotope': ['74', 1.0, None]} 
    # {isotope: [productZ, branchingRatio isomerLevel]} #beta+/beta- for tendl feedomg
    # {isotope: [branchingRatio isomerLevel]} #isomer for tendl feedomg
    #exfor.plotExforDataFromFilename('Ta_178TA_cumu.txt')  # plotting the EXFOR data for comparison.
    calculate_cross_section(element, isotope) 
    exfor.plotExforDataFromFilename('Ta_178TA_cumu.txt', setLegend=False, maxE=maxE)
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element, 
                    isomerLevel = None,
                    betaFeeding = 'beta+', # only beta+ beta-
                    branchingRatio = 1.0,
                    parentIsomerLevel = None)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    tendl_ta.plotTendl23Unique_feeding(productZ=Z, productA=A, isomerLevel = None,  
                                  betaPlusDecayChain = betaplus_decay_chain, betaMinusDecayChain = None, isomerDecayChain = None, 
                                  color=None, lineStyle=None)
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')    
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_cumu.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ta_178TA_cumulative() 



def ta_180TA_independent():
    element='Ta'; isotope='180TA';
    Z = '73'; A = '180'
    maxE = 60; maxXs = 400
    exfor.plotExforDataFromFilename('Ta_180TA_ind.txt')  # plotting the EXFOR data for comparison.
    calculate_cross_section(element, isotope)
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')    
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ta_180TA_independent() 



def ta_172HFg_cumulative():
    element='Ta'; isotope='172HFg';
    Z = '72'; A = '172'
    maxE = 200; maxXs = 500    
    betaplus_decay_chain = {'isotope': ['73', 1.0, None]} 
    # {isotope: [productZ, branchingRatio isomerLevel]} #beta+/beta- for tendl feedomg
    # {isotope: [branchingRatio isomerLevel]} #isomer for tendl feedomg
    #exfor.plotExforDataFromFilename('Ta_178TA_cumu.txt')  # plotting the EXFOR data for comparison.
    calculate_cross_section(element, isotope) 
    #exfor.plotExforDataFromFilename('Ta_172HFg_cumu.txt')
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element, 
                    isomerLevel = None,
                    betaFeeding = 'beta+', # only beta+ beta-
                    branchingRatio = 1.0,
                    parentIsomerLevel = None)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    tendl_ta.plotTendl23Unique_feeding(productZ=Z, productA=A, isomerLevel = None,  
                                  betaPlusDecayChain = betaplus_decay_chain, betaMinusDecayChain = None, isomerDecayChain = None, 
                                  color=None, lineStyle=None)
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')    
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_cumu.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ta_172HFg_cumulative() 



def ta_173HF_cumulative():
    element='Ta'; isotope='173HF';
    Z = '72'; A = '173'
    maxE = 60; maxXs = 50     # Hvorfor er usikkerheten så sykt høy??!
    betaplus_decay_chain = {'isotope': ['73', 1.0, None]} 
    # {isotope: [productZ, branchingRatio isomerLevel]} #beta+/beta- for tendl feedomg
    # {isotope: [branchingRatio isomerLevel]} #isomer for tendl feedomg
    #exfor.plotExforDataFromFilename('Ta_178TA_cumu.txt')  # plotting the EXFOR data for comparison.
    calculate_cross_section(element, isotope) 
    exfor.plotExforDataFromFilename('Ta_173HF_cumu.txt')
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element, 
                    isomerLevel = None,
                    betaFeeding = 'beta+', # only beta+ beta-
                    branchingRatio = 1.0,
                    parentIsomerLevel = None)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    tendl_ta.plotTendl23Unique_feeding(productZ=Z, productA=A, isomerLevel = None,  
                                  betaPlusDecayChain = betaplus_decay_chain, betaMinusDecayChain = None, isomerDecayChain = None, 
                                  color=None, lineStyle=None)
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')    
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_cumu.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ta_173HF_cumulative() 


def ta_175HF_cumulative():
    element='Ta'; isotope='175HF';
    Z = '72'; A = '175'
    maxE = 60; maxXs = 40     # Hvorfor er usikkerheten så sykt høy??!
    betaplus_decay_chain = {'isotope': ['73', 1.0, None]} 
    # {isotope: [productZ, branchingRatio isomerLevel]} #beta+/beta- for tendl feedomg
    # {isotope: [branchingRatio isomerLevel]} #isomer for tendl feedomg
    #exfor.plotExforDataFromFilename('Ta_178TA_cumu.txt')  # plotting the EXFOR data for comparison.
    calculate_cross_section(element, isotope) 
    exfor.plotExforDataFromFilename('Ta_175HF_cumu.txt')
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element, 
                    isomerLevel = None,
                    betaFeeding = 'beta+', # only beta+ beta-
                    branchingRatio = 1.0,
                    parentIsomerLevel = None)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    tendl_ta.plotTendl23Unique_feeding(productZ=Z, productA=A, isomerLevel = None,  
                                  betaPlusDecayChain = betaplus_decay_chain, betaMinusDecayChain = None, isomerDecayChain = None, 
                                  color=None, lineStyle=None)
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')    
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_cumu.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ta_175HF_cumulative() 


def ta_180HFm1_cumulative():
    element='Ta'; isotope='180HFm1';
    Z = '72'; A = '180'
    maxE = 60; maxXs = 40     # Hvorfor er usikkerheten så sykt høy??!
    betaplus_decay_chain = {'isotope': ['73', 1.0, None]} 
    # {isotope: [productZ, branchingRatio isomerLevel]} #beta+/beta- for tendl feedomg
    # {isotope: [branchingRatio isomerLevel]} #isomer for tendl feedomg
    #exfor.plotExforDataFromFilename('Ta_178TA_cumu.txt')  # plotting the EXFOR data for comparison.
    calculate_cross_section(element, isotope) 
    #exfor.plotExforDataFromFilename('Ta_180HFm_cumu.txt')
    talys.plotTalys(productZ=Z, productA=A, targetFoil=element, 
                    isomerLevel = None,
                    betaFeeding = 'beta+', # only beta+ beta-
                    branchingRatio = 1.0,
                    parentIsomerLevel = None)
    tendl_ta.plotTendl23Unique(productZ=Z, productA=A, color='hotpink')
    tendl_ta.plotTendl23Unique_feeding(productZ=Z, productA=A, isomerLevel = None,  
                                  betaPlusDecayChain = betaplus_decay_chain, betaMinusDecayChain = None, isomerDecayChain = None, 
                                  color=None, lineStyle=None)
    plt.xlim(0,maxE) 
    plt.ylim(0, maxXs)
    set_title(element, isotope, independent=True)
    # plt.legend(fontsize='5')    
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_cumu.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ta_180HFm1_cumulative() 



#     '173TAg','174TAg'
#     '172HFg'
#     '172LUm','176LUm','178LUg','179LUg'





















# ------------ Ni isotopes ------------

def ni_62ZN_independent():
    element='Ni'; isotope='62ZN';
    maxE = 60
    calculate_cross_section(element, isotope)
    #exfor.plotExforDataFromFilename('Ni_62ZN_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ni_62ZN_independent() 


def ni_63ZN_independent():
    element='Ni'; isotope='63ZN';
    maxE = 60
    calculate_cross_section(element, isotope)
    #exfor.plotExforDataFromFilename('Ni_63ZN_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ni_63ZN_independent() 


def ni_65ZN_independent():
    element='Ni'; isotope='65ZN';
    maxE = 60
    calculate_cross_section(element, isotope)
    #exfor.plotExforDataFromFilename('Ni_65ZN_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ni_65ZN_independent() 


def ni_59CU_independent():
    element='Ni'; isotope='59CU';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Ni_59CU_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ni_59CU_independent() 


def ni_61CU_independent():
    element='Ni'; isotope='61CU';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Ni_61CU_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ni_61CU_independent() 


def ni_62CU_independent():
    element='Ni'; isotope='62CU';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Ni_62CU_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ni_62CU_independent() 


def ni_64CU_independent():
    element='Ni'; isotope='64CU';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Ni_64CU_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ni_64CU_independent() 


def ni_56NI_independent():
    element='Ni'; isotope='56NI';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Ni_56NI_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ni_56NI_independent() 


def ni_56CO_independent():
    element='Ni'; isotope='56CO';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Ni_56CO_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ni_56CO_independent() 


def ni_58CO_independent():
    element='Ni'; isotope='58CO';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Ni_58CO_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#ni_58CO_independent() 



# isotopes_list = [
#     '59CUg','60CUg','61CUg','62CUg','64CUg',
#     '54COm1','55COg','56COg','57COg','58COg','58COm','58COm1','60COg','60COm','60COm1','61COg','62COg','62COm1',
#     '53FEg','53FEm1','55FEg','59FEg','61FEg',
#     '50MNm1','51MNg','52MNg','52MNm','52MNm1','54MNg','56MNg',
#     '49CRg','51CRg','55CRg',
#     '47Vg',
#     '56NIg','57NIg']













       
# ------------ Cu isotopes ------------


def cu_59CU_independent():
    element='Cu'; isotope='59CU';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Cu_59CU_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#cu_59CU_independent() 


def cu_61CU_independent():
    element='Cu'; isotope='61CU';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Cu_61CU_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#cu_61CU_independent() 


def cu_62CU_independent():
    element='Cu'; isotope='62CU';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Cu_62CU_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#cu_62CU_independent() 


def cu_64CU_independent():
    element='Cu'; isotope='64CU';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Cu_64CU_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#cu_64CU_independent() 


def cu_56NI_independent():
    element='Cu'; isotope='56NI';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Cu_56NI_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#cu_56NI_independent() 


def cu_57NI_independent():
    element='Cu'; isotope='57NI';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Cu_57NI_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

#cu_57NI_independent() 




# isotopes_list = [
#     '59CUg','60CUg','61CUg','62CUg','64CUg',
#     '60ZNg','61ZNg','62ZNg','63ZNg','65ZNg',
#     '55COg','56COg','57COg','58COg','58COm1','60COg','60COm1','61COg','62COg','62COm1',
#     '53FEg','55FEg','59FEg','61FEg',
#     '54MNg','56MNg',
#     '56NIg','57NIg']