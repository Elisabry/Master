import curie as ci
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.constants import elementary_charge
import os
from scipy.interpolate import PchipInterpolator
from Exfor import Exfor


exfor = Exfor(os.getcwd() + '/../exfor/')

def get_energy(element): # going trough the stack files to get the weighted average beam energy for the chosen element.
    if element == 'Cu':
        stack_30 = os.getcwd() + '/stack_30_MeV_Cu_weighted_average_beam_energy.csv'
        stack_55 = os.getcwd() + '/stack_55_MeV_Cu_weighted_average_beam_energy.csv'
    elif element == 'Ni':
        stack_30 = os.getcwd() + '/stack_30_MeV_Ni_weighted_average_beam_energy.csv'
        stack_55 = os.getcwd() + '/stack_55_MeV_Ni_weighted_average_beam_energy.csv'
    elif element == 'Ta':
        stack_30 = os.getcwd() + '/stack_30_MeV_Ta_weighted_average_beam_energy.csv'
        stack_55 = os.getcwd() + '/stack_55_MeV_Ta_weighted_average_beam_energy.csv'
    else:
        raise ValueError('Element not recognized. Please use Cu, Ni, or Ta.')
    df_30 = pd.read_csv(stack_30)
    df_55 = pd.read_csv(stack_55)

    df = pd.concat([df_55, df_30])  # concatenate the two dataframes to get all the energies in one dataframe. This is necessary because we want to use all of them to get a better estimate of the energy.

    energy = df['wabe'].values              # wabe = weighted average beam energy, to get the energy for each element in the stack, then use this energy to get the cross section for each element.
    unc_left = df['unc wabe left'].values        # in the kinda normal curve (not symetric), the left and right uncertainties are not the same 
    unc_right = df['unc wabe right'].values
    return energy, unc_left, unc_right           # returns the energy and the uncertainties and putting it in a dataframe.

def get_beam_current():
    stack_30 = os.getcwd () + '/beam_current_stack_30_MeV.csv'
    stack_55 = os.getcwd () + '/beam_current_stack_55_MeV.csv'

    df_30 = pd.read_csv(stack_30)
    df_55 = pd.read_csv(stack_55)

    df = pd.concat([df_55, df_30]) 
    
    beam_current = df['beam current (nA)'].values              
    unc_beam_current = df['unc beam current (nA)'].values
    beam_current *= 1e-9 / elementary_charge 
    unc_beam_current *= 1e-9 / elementary_charge 
    return np.array(beam_current), np.array(unc_beam_current)

def get_NT(element):
    if element == 'Cu':
        NT_file = os.getcwd() + '/../Activity/Cu_areal_density_NT.csv'
        header_NT = 'Cu_NT_atoms_per_cm2'
        header_unc_NT = 'Cu_NT_unc_atoms_per_cm2'
    elif element == 'Ni':
        NT_file = os.getcwd() + '/../Activity/Ni_areal_density_NT.csv'
        header_NT = 'Ni_NT_atoms_per_cm2'
        header_unc_NT = 'Ni_NT_unc_atoms_per_cm2'
    elif element == 'Ta':
        NT_file = os.getcwd() + '/../Activity/Ta_areal_density_NT.csv'
        header_NT = 'Ta_NT_atoms_per_cm2'
        header_unc_NT = 'Ta_NT_unc_atoms_per_cm2'
    else:
        raise ValueError('Element not recognized. Please use Cu, Ni, or Ta.')
    
    df = pd.read_csv(NT_file)
    NT = df[header_NT].values
    unc_NT = df[header_unc_NT].values
    return np.array(NT), np.array(unc_NT)

def get_A0(element, isotope):
    A0_files = get_A0_files(element)
    A0_total = np.zeros(14); unc_A0_total = np.zeros(14)
    for i,file in enumerate(A0_files):
        path = os.getcwd() + '/../'
        df = pd.read_csv(path + file)
        df_isotope = df[df['isotope'].isin([isotope, isotope + 'g'])]
        if df_isotope.empty:
            A0_total[i] = 0
            unc_A0_total[i] = 0
        else:
            A0_total[i] = df_isotope['A0'].values              
            unc_A0_total[i] = df_isotope['sigma_A0'].values           
    return np.array(A0_total), np.array(unc_A0_total)

def get_A0_files(element):
    if element == 'Cu':
        files = ['Activity/Activity_data/Cu01_A0.csv', './Activity/Activity_data/Cu02_A0.csv', './Activity/Activity_data/Cu03_A0.csv', './Activity/Activity_data/Cu04_A0.csv', './Activity/Activity_data/Cu05_A0.csv', './Activity/Activity_data/Cu06_A0.csv', './Activity/Activity_data/Cu07_A0.csv', './Activity/Activity_data/Cu08_A0.csv', './Activity/Activity_data/Cu09_A0.csv', './Activity/Activity_data/Cu10_A0.csv', './Activity/Activity_data/Cu11_A0.csv', './Activity/Activity_data/Cu12_A0.csv', './Activity/Activity_data/Cu13_A0.csv', './Activity/Activity_data/Cu14_A0.csv']
    elif element == 'Ni':
        files = ['./Activity/Activity_data/Ni01_A0.csv', './Activity/Activity_data/Ni02_A0.csv', './Activity/Activity_data/Ni03_A0.csv', './Activity/Activity_data/Ni04_A0.csv', './Activity/Activity_data/Ni05_A0.csv', './Activity/Activity_data/Ni06_A0.csv', './Activity/Activity_data/Ni07_A0.csv', './Activity/Activity_data/Ni08_A0.csv', './Activity/Activity_data/Ni09_A0.csv', './Activity/Activity_data/Ni10_A0.csv', './Activity/Activity_data/Ni11_A0.csv', './Activity/Activity_data/Ni12_A0.csv', './Activity/Activity_data/Ni13_A0.csv', './Activity/Activity_data/Ni14_A0.csv']
    elif element == 'Ta':
        files = ['./Activity/Activity_data/Ta01_A0.csv', './Activity/Activity_data/Ta02_A0.csv', './Activity/Activity_data/Ta03_A0.csv', './Activity/Activity_data/Ta04_A0.csv']
    else:
        raise ValueError('Element not recognized. Please use Cu, Ni, or Ta.')
    return files

def load_file_with_uncertainty(element, isotope):
    """Load cross section data with uncertainties and return PCHIP interpolators."""
    path = os.getcwd() +'/../Monitor_Cross_Sections/IAEA_Monitor_Data/'
    if element == 'Cu' and isotope =='56CO':
        file = 'cup56cot'
    elif element == 'Cu' and isotope =='58CO':
        file = 'cup58cot'
    elif element == 'Cu' and isotope =='62ZN':
        file = 'cup62znt'
    elif element == 'Cu' and isotope =='63ZN':
        file = 'cup63znt'
    elif element == 'Cu' and isotope =='65ZN': 
        file = 'cup65znt'
    elif element == 'Ni' and isotope =='57NI':
        file = 'nip57nit'
    else:
        raise ValueError('Element or isotope not recognized. Please use Cu with 56CO, 58CO, 62ZN, 63ZN, or 65ZN; or Ni with 57NI.')
    data = []
    for line in open(path+file+'.txt').readlines()[6:]:
        if line.strip():
            try:
                e, xs, unc = map(float, line.split()[:3])
                data.append((e, xs, unc))
            except ValueError:
                continue
    if len(data) < 2:
        return None, None
    E, xs, unc = map(np.array, zip(*data))
    interp_xs = PchipInterpolator(E, xs, extrapolate=True)
    interp_unc = PchipInterpolator(E, unc, extrapolate=True)
    plt.plot(E, interp_xs(E), label='IAEA data')  # plotting the IAEA data for comparison.
    return E, interp_xs, interp_unc

def calculate_cross_section(element, isotope):
    A0, unc_A0 = get_A0(element, isotope)                            
    beam_current, unc_beam_current  = get_beam_current()              # getting the beam current and its uncertainty, this will be used to calculate the cross section and its uncertainty.
    t_irr = 3600; unc_t_irr = 1  # seconds                            # t_irr won't have a large effect if not super precise, but A0 will so this need to be correct.
    decay_constant, unc_decay_const = ci.Isotope(isotope).decay_const(units='s', unc=True)
    NT, unc_NT = get_NT(element)                                                # getting the areal density and its uncertainty, this will be used to calculate the cross section and its uncertainty.
    xs = A0/(beam_current.T * (1 - np.exp(-decay_constant * t_irr)) * NT.T)     # calulating the cross section by using the xs-equation.
    unc_xs = xs * np.sqrt(
        (unc_A0/A0)**2 + (unc_beam_current/beam_current)**2 + (unc_decay_const/decay_constant)**2 + (unc_NT/NT)**2 + ( unc_t_irr/t_irr)**2      # caluculating the uncertainty of the cross section by using error propagation. 
     )
    xs *= 1e27          # converting the cross section from cm^2 to mb.
    unc_xs *= 1e27      # converting the uncertainty of the cross section from
    energy, unc_left, unc_right = get_energy(element) # getting the energy for the element, this will be used to plot the cross section as a function of energy. The uncertainties will be used to plot error bars.    
    plt.errorbar(energy, xs, xerr=[unc_left,unc_right], yerr=unc_xs, marker='o', label='This work', ls='none')  # plotting the cross section with error bars.