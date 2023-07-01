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
magnesium_dataframe = pd.DataFrame()

# Magnesium dataset
silicium_range = np.array([5.910, 7.168, 8.513, 9.946, 11.468,
                            13.08, 14.78, 16.58, 18.46, 20.43,
                            24.64, 29.21, 34.12, 39.38, 44.99,
                            63.82, 101.76, 147.57, 200.95, 261.61,
                            329.3, 403.8, 485.0, 572.6, 666.4,
                            766.4, 872.3, 1_101.4, 1_352.9, 1_625.7,
                            3_284., 5_380., 7_847., 10_617., 13_650.,
                            16_912., 20_377., 24_021.,
                            ])

magnesium_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
magnesium_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
magnesium_dataframe['A'] = 24
magnesium_dataframe['Z'] = 12
magnesium_dataframe['Z_material'] = 14
magnesium_dataframe['A_material'] = 28