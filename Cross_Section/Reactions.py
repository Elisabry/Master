import matplotlib.pyplot as plt
from Cross_Section import calculate_cross_section, load_file_with_uncertainty
from Exfor import Exfor
import os

exfor = Exfor(os.getcwd() + '/../exfor/')
path_to_cross_section_figures = os.getcwd()+'/../Figures/cross_section_figures/'

def set_title(element, isotope, independent=False):
    if independent:
        str = element + '(p,x)' + isotope + ' - independent'
    else:
        str = element + '(p,x)' + isotope + ' - cumulative'
    plt.title(str)
    plt.xlabel('Energy (MeV)')
    plt.ylabel('Cross section (mb)')

# def set_legend(fontsize='small', loc='best'):
#     handles, labels = plt.gca().get_legend_handles_labels()
#     by_label = OrderedDict(zip(labels, handles))
#     plt.legend(by_label.values(), by_label.keys(), fontsize=fontsize, loc=loc)

def cu_62ZN_monitor():
    element='Cu'; isotope='62ZN';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Cu_62Zn_ind.txt', setLegend=False, maxE=maxE)  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')
    # set_legend(fontsize='5')
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

cu_62ZN_monitor()

def cu_63ZN_monitor():
    element='Cu'; isotope='63ZN';
    maxE = 60
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Cu_63Zn_ind.txt')  # plotting the EXFOR data for comparison.
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')    
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

# cu_63ZN_monitor()

def cu_65ZN_monitor():
    element='Cu'; isotope='65ZN';
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Cu_65Zn_ind.txt')  # plotting the EXFOR data for comparison.
    maxE = 60
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')    
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

# cu_65ZN_monitor()

def cu_56CO_monitor():
    element='Cu'; isotope='56CO';
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Cu_56Co_cumu.txt')  # plotting the EXFOR data for comparison.
    maxE = 60
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')    
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

# cu_56CO_monitor()

def cu_58CO_monitor():
    element='Cu'; isotope='58CO';
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Cu_58Co_cumu.txt')  # plotting the EXFOR data for comparison.
    maxE = 60
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')    
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

# cu_58CO_monitor()

def ni_57NI_monitor():
    element='Ni'; isotope='57NI';
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    exfor.plotExforDataFromFilename('Ni_57Ni_cumu.txt')  # plotting the EXFOR data for comparison.
    maxE = 60
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')    
    name = element+'_'+isotope+'_ind.pdf'
    plt.savefig(path_to_cross_section_figures + name)
    plt.show()

# ni_57NI_monitor()

def ta_177W_independet():
    element='Ta'; isotope='177W';
    calculate_cross_section(element, isotope)
    load_file_with_uncertainty(element, isotope)
    #exfor.plotExforDataFromFilename('Ni_57Ni_cumu.txt')  # plotting the EXFOR data for comparison.
    maxE = 60
    plt.xlim(0,maxE) 
    set_title(element, isotope, independent=True)
    plt.legend(fontsize='5')    
    name = element+'_'+isotope+'_ind.pdf'
    #plt.savefig(path_to_cross_section_figures + name)
    plt.show()

ta_177W_independet()

    