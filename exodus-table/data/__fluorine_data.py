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
#Intialisation du dataframe
fluorine_dataframe = pd.DataFrame()

# Fluorine dataset
silicium_range = np.array([6.570, 8.144, 9.850, 11.690, 13.664,
                           15.77, 18.01, 20.38, 22.89, 25.52,
                           31.18, 37.35, 44.03, 51.20, 58.88,
                           84.80, 137.39, 201.22, 275.82, 360.77,
                           455.7, 560.3, 674.2, 797.3, 929.2,
                           1_069.7, 1_218.6, 1_540., 1_894.6, 2_228.4,
                           4_613., 7_562., 11_033., 14_932., 19_200.,
                           23_792., 26_669., 33_797.,
                           ])

fluorine_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
fluorine_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
fluorine_dataframe['A'] = 19
fluorine_dataframe['Z'] = 9
fluorine_dataframe['Z_material'] = 14
fluorine_dataframe['A_material'] = 28