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
#Initialisation du dataframe
lithium_dataframe = pd.DataFrame()

silicium_range = np.array([13.66, 18., 22.86, 28.23, 34.10,
                          40.46, 47.30, 64.42, 62.40, 70.65,
                          88.53, 108.19, 129.61, 152.76, 177.60,
                          262.1, 434.6, 645., 891.5, 1_172.4,
                          1_487., 1_833., 2_211., 2_618., 3055.,
                          3_521., 4_015., 5_083, 6_256., 7_529.,
                          15_268., 25_047., 36_557., 49_484., 63_638.,
                          78_863., 96_032., 112_036.,
                          ])

lithium_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
lithium_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
lithium_dataframe['A'] = 7
lithium_dataframe['Z'] = 3
lithium_dataframe['Z_material'] = 14
lithium_dataframe['A_material'] = 28