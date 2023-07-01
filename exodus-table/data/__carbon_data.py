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
# Initialise le dataframe
carbon_dataframe = pd.DataFrame()

silicium_range = np.array([7.490, 9.493, 11.701, 14.113, 16.727,
                         19.54, 22.56, 25.77, 29.17, 32.77,
                         40.54, 49.06, 58.33, 68.32, 79.03,
                         115.37, 189.48, 279.75, 385.42, 505.89,
                         640.6, 789.1, 950.9, 1_125.6, 1_313.,
                         1513., 1724., 2_182., 2_685., 3_320.,
                         6_547., 10_738., 15_671., 21_211., 27_275.,
                         33_802., 40_732., 48_019.,
                         ])

carbon_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
carbon_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
carbon_dataframe['A'] = 12
carbon_dataframe['Z'] = 6
carbon_dataframe['Z_material'] = 14
carbon_dataframe['A_material'] = 28