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
#Initialisation le Dataframe
calcium_dataframe = pd.DataFrame()
# Calcium dataset
silicium_range = np.array([5.670, 6.669, 7.709, 8.793, 9.925,
                          11.104, 12.333, 13.611, 14.939, 16.317,
                          19.22, 22.33, 25.64, 29.14, 32.84,
                          45.09, 69.29, 98.04, 131.18, 168.57,
                          210.1, 255.6, 305.0, 358.2, 415.1,
                          475.6, 539.7, 678.0, 829.6, 993.9,
                          1_991., 3_250., 4_730., 6_392., 8_213.,
                          10_170., 12_249., 14_435.,
                          ])

calcium_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
calcium_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
calcium_dataframe['A'] = 40
calcium_dataframe['Z'] = 20
calcium_dataframe['Z_material'] = 14
calcium_dataframe['A_material'] = 28