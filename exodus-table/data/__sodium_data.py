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
sodium_dataframe = pd.DataFrame()

# Sodium dataset
silicium_range = np.array([6.280, 7.660, 9.141, 10.726, 12.414,
                         14.21, 16.10, 18.11, 20.21, 22.42,
                         27.15, 32.28, 37.81, 43.75, 50.07,
                         71.38, 114.40, 166.44, 227.15, 296.20,
                         373.3, 458.2, 550.7, 650.5, 757.4,
                         871.4, 992.1, 1_253.4, 1_540.1, 1_851.2,
                         3_743., 6_133., 8_946., 12_103., 15_564.,
                         19_285., 23_237., 27_392.,
                         ])

sodium_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
sodium_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
sodium_dataframe['A'] = 23
sodium_dataframe['Z'] = 11
sodium_dataframe['Z_material'] = 14
sodium_dataframe['A_material'] = 28