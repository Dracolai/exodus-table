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

#Initialisation du Dataframe
sulfur_dataframe = pd.DataFrame()

# Sulfur dataset
Sulfur_range = np.array([5.710, 6.805, 7.957, 9.170, 10.445,
                         11.784, 13.187, 14.655, 16.187, 17.784,
                         21.17, 24.81, 28.71, 32.86, 37.26,
                         51.93, 81.19, 116.25, 156.88, 202.90,
                         254.1, 310.4, 371.6, 437.6, 508.3,
                         583.5, 663.2, 835.4, 1_024.3, 1_229.2,
                         2_474., 4_096., 5_896., 7_974., 10_249.,
                         12_696., 15_295., 18_027.,
                         ])

sulfur_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
sulfur_dataframe['range_micron'] = Sulfur_range/Convertion_factor['Si']
sulfur_dataframe['A'] = 32
sulfur_dataframe['Z'] = 16
sulfur_dataframe['Z_material'] = 14
sulfur_dataframe['A_material'] = 28