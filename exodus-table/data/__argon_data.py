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
# Initialisation du Datframe
argon_dataframe = pd.DataFrame()

# Argon dataset
silicium_range = np.array([6.290, 7.448, 8.658, 9.927, 11.254,
                        12.643, 14.094, 15.608, 17.184, 18.822,
                        22.29, 26.00, 29.97, 34.17, 38.63,
                        53.43, 82.80, 117.84, 158.34, 204.13,
                        255.0, 310.9, 371.6, 437.0, 507.0,
                        581.5, 660.3, 830.8, 1_017.6, 1_220.1,
                        2_450., 4_003., 5_831., 7_883., 10_130.,
                        12_547, 15_114., 17_812.,
                        ])

argon_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
argon_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
argon_dataframe['A'] = 40
argon_dataframe['Z'] = 18
argon_dataframe['Z_material'] = 14
argon_dataframe['A_material'] = 28