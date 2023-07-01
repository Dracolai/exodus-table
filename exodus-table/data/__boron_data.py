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
#Intitialise le dataframe
boron_dataframe = pd.DataFrame()

# Boron dataset
silicium_range = np.array([9.140, 11.703, 14.546, 17.664, 21.056,
                        24.72, 28.64, 32.83, 37.29, 42.00,
                        52.18, 63.36, 75.53, 88.67, 102.76,
                        150.6, 248.3, 367.4, 506.8, 665.8,
                        843.6, 1_039.6, 1_253.1, 1_483.8, 1_731.1,
                        1_995., 2_274., 2_878., 3_542., 4_262., 8_640.,
                        14_172., 20_684., 27_997., 36_003.,
                        44_617., 53_764., 63_383.,
                        ])

boron_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
boron_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
boron_dataframe['A'] = 11
boron_dataframe['Z'] = 5
boron_dataframe['Z_material'] = 14
boron_dataframe['A_material'] = 28