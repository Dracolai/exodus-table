
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
#Initialisation du Datframe
potassium_dataframe = pd.DataFrame()

# Potassium dataset
silicium_range = np.array([5.820, 6.866, 7.958, 9.098, 10.290,
                            11.535, 12.834, 14.186, 15.593, 17.054,
                            20.14, 23.44, 26.96, 30.70, 34.64,
                            47.74, 73.65, 104.51, 140.13, 180.36,
                            225.1, 274.1, 327.3, 384.7, 446.0,
                            511.3, 580.4, 729.7, 893.3, 1_070.7,
                            2_148., 3_507, 5_106., 6_902., 8_868.,
                            10_983., 13_229., 15_591.,
                            ])

potassium_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
potassium_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
potassium_dataframe['A'] = 39
potassium_dataframe['Z'] = 19
potassium_dataframe['Z_material'] = 14
potassium_dataframe['A_material'] = 28