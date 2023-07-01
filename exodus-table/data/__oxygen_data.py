"""

"""
import pandas as pd
import numpy as np


# Data
energy_per_nuc = np.array([2.5, 3., 3.5, 4., 4.5,
                           5., 5.5, 6., 6.5, 7,
                           8., 9., 10., 11., 12.,
                           15., 20., 25., 30., 35.,
                           40., 45., 50., 55., 60.,
                           65., 70., 80., 90., 100,
                           150, 200., 250., 300., 350.,
                           400., 450., 500.,
                           ])
Convertion_factor = {'Be' : 0.1848, 'C' : 0.2267, 'Mg' : 0.1738, 'Al' : 0.2232, 'Si' : 0.2330,
                     'Ca' : 0.1550, 'Ti' : 0.4540, 'Cr' : 0.7190, 'Fe' : 0.7874, 'Ni' : 0.8902,
                     'Cu' : 0.8960, 'Ge' : 0.5323, 'Se' : 0.4790, 'Sr' : 0.2540, 'Zr' :0.6506,
                     'Mo' : 1.022, 'Rh' :1.241, 'Ag' : 1.050, 'Sn' : 0.7283, 'Te' : 0.6240,
                     'Ba' : 0.3500, 'La' : 0.6175, 'Pr' : 0.6773, 'Sm' :0.7520, 'Gd' : 0.7900,
                     'Ho' : 0.8795, 'Tm' : 0.9321, 'Lu' : 0.9840, 'Ta' : 1.655, 'Re' : 2.102,
                     'Ir' : 2.242, 'Au' : 1.930, 'Pb' : 1.135, 'Bi' : 0.9747, 'Th' : 1.172,
                     'U' : 1.895,
                     }# MeV/micron
#//                                                     
#Initialize the dataframe
oxygen_dataframe = pd.DataFrame()

# Oxygen dataset
silicium_range = np.array([6.450, 8.064, 9.823, 11.728, 13.778,
                         15.97, 18.31, 20.80, 23.44, 26.19,
                         32.14, 38.64, 45.69, 53.28, 61.39,
                         88.87, 144.72, 212.60, 291.99, 382.44,
                         483.5, 595., 716.4, 847.5, 988.,
                         1_138., 1_296., 1_640., 2_017., 2_426.,
                         4_914., 8_245., 11_989., 15_912., 20_461.,
                         25_355., 30_552., 36_018.,
                         ])

oxygen_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
oxygen_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
oxygen_dataframe['A'] = 16
oxygen_dataframe['Z'] = 8
oxygen_dataframe['Z_material'] = 14
oxygen_dataframe['A_material'] = 28