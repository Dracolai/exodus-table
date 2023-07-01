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
#Initialisation du DataFrame
aluminum_dataframe = pd.DataFrame()

# Aluminum dataset
silicon_range = np.array([6.060, 7.314, 8.647, 10.064, 11.565,
                            13.15, 14.82, 16.58, 18.42, 20.35,
                            24.45, 28.89, 33.67, 38.77, 44.20,
                            62.42, 99.01, 143.12, 194.45, 252.74,
                            317.8, 389.3, 467.2, 551.4, 641.2,
                            737.1, 838.7, 1_058.4, 1_299.5, 1_561.1,
                            3_151., 5_160., 7_525., 10_180., 13_087.,
                            16_215., 19_817., 23_029.,
                            ])

aluminum_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
aluminum_dataframe['range_micron'] = silicon_range/Convertion_factor['Si']
aluminum_dataframe['A'] = 27
aluminum_dataframe['Z'] = 13
aluminum_dataframe['Z_material'] = 14
aluminum_dataframe['A_material'] = 28