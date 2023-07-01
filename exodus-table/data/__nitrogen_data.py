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
#Intialisation du DataFrame
nitrogen_dataframe = pd.DataFrame()

# Nitrogen dataset
silicium_range = np.array([6.850, 8.627, 10.575, 12.694, 14.983,
                           17.44, 20.06, 22.86, 25.81, 28.93,
                           35.65, 43.02, 51.01, 59.62, 68.84,
                           100.10, 163.75, 241.20, 331.84, 435.14,
                           550.6, 677.9, 816.6, 966.4, 1_127.,
                           1_298., 1_479., 1_872., 2_303., 2_770.,
                           5_613., 9_206., 13_434., 18_183., 23_382.,
                           28_975., 34_915., 41_727.,
                           ])

nitrogen_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
nitrogen_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
nitrogen_dataframe['A'] = 14
nitrogen_dataframe['Z'] = 7
nitrogen_dataframe['Z_material'] = 14
nitrogen_dataframe['A_material'] = 28