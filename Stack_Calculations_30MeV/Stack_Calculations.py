# ...existing code...
import numpy as np
import curie as ci
import pandas as pd

x_kapton = 0.013
x_silicone = 0.013
ad_degrader_a = 599.0  # 2.24 mm
ad_degrader_b = 415.0  # 1.55 mm
ad_degrader_c = 261.5  # 0.97 mm
# ad_degrader_d = 599.0
ad_degrader_e = 68.3  # 0.256 mm
ad_degrader_h = 33.8
ad_be_backing = 4.425  # 23.9130435 microns


def stack_30(E_p, build=True):
    stack = [
        # compartment08
        {'compound': 'Ni', 'name': 'Ni08', 'ad': 23.145},
        {'compound': 'Sn', 'name': 'Sn08', 'ad': 8.047},
        {'compound': 'Ta', 'name': 'Ta08', 'ad': 27.227},
        {'compound': 'Cu', 'name': 'Cu08', 'ad': 22.197},
        {'compound': 'Al', 'name': 'Al_degrader_E2_E1', 'ad': 2 * ad_degrader_e},

        # compartment09
        {'compound': 'Ni', 'name': 'Ni09', 'ad': 22.662},
        {'compound': 'Sn', 'name': 'Sn09', 'ad': 7.829},
        {'compound': 'Ta', 'name': 'Ta09', 'ad': 27.377},
        {'compound': 'Cu', 'name': 'Cu09', 'ad': 22.091},
        {'compound': 'Al', 'name': 'Al_degrader_E4_E3', 'ad': 2 * ad_degrader_e},

        # compartment10
        {'compound': 'Ni', 'name': 'Ni10', 'ad': 23.107},
        {'compound': 'Sn', 'name': 'Sn10', 'ad': 8.232},
        {'compound': 'Ta', 'name': 'Ta10', 'ad': 27.165},
        {'compound': 'Cu', 'name': 'Cu10', 'ad': 22.259},
        {'compound': 'Al', 'name': 'Al_degrader_E6_E5', 'ad': 2 * ad_degrader_e},

        # compartment11
        {'compound': 'Ni', 'name': 'Ni11', 'ad': 22.941},
        {'compound': 'Sn', 'name': 'Sn11', 'ad': 7.982},
        {'compound': 'Ta', 'name': 'Ta11', 'ad': 27.200},
        {'compound': 'Cu', 'name': 'Cu11', 'ad': 22.211},
        {'compound': 'Al', 'name': 'Al_degrader_E8_E7', 'ad': 2 * ad_degrader_e},

        # compartment12
        {'compound': 'Ni', 'name': 'Ni12', 'ad': 23.155},
        {'compound': 'Sn', 'name': 'Sn12', 'ad': 8.021},
        {'compound': 'Ta', 'name': 'Ta12', 'ad': 27.702},
        {'compound': 'Cu', 'name': 'Cu12', 'ad': 22.177},
        {'compound': 'Al', 'name': 'Al_degrader_E9', 'ad': ad_degrader_e},

        # compartment13
        {'compound': 'Ni', 'name': 'Ni13', 'ad': 23.153},
        {'compound': 'Sn', 'name': 'Sn13', 'ad': 7.354},
        {'compound': 'Ta', 'name': 'Ta13', 'ad': 27.337},
        {'compound': 'Cu', 'name': 'Cu13', 'ad': 22.168},
        {'compound': 'Al', 'name': 'Al_degrader_E10', 'ad': ad_degrader_e},

        # compartment14
        {'compound': 'Ni', 'name': 'Ni14', 'ad': 23.067},
        {'compound': 'Sn', 'name': 'Sn14', 'ad': 7.620},
        {'compound': 'Ta', 'name': 'Ta14', 'ad': 27.361},
        {'compound': 'Cu', 'name': 'Cu14', 'ad': 22.125},
    ]
    if build:
        full_stack = ci.Stack(stack, E0=E_p, particle='p', dE0=0.55, N=1E6, max_steps=100)
        return full_stack
    else:
        return stack




dp_array = np.arange(0.8, 1.21, 0.01)
dp_array_length = len(dp_array)
index = 0

for dp in dp_array:
    index += 1
    print('__________________________________________')
    print(f'Running stack calculation for dp = {dp:.2f}')
    
    st = ci.Stack(stack_30(30, build=False), E0=30, dE0=0.55, N=1e6, particle='p', dp=dp)
    st.saveas(f'stack_30MeV_dp_{dp:.2f}.csv')
    
    percent_done = index/dp_array_length*100
    print(f'{percent_done:.2f}% of the calculation is done')
    print('__________________________________________\n')



# st = ci.Stack(stack_30(30, build=False), E0=30, dE0=0.55, N=1e5, particle='p', dp=1) # satt dp=dp til 1.
# st.plot(filter_name="Cu*") 