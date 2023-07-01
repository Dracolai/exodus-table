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
silicon_dataframe = pd.DataFrame()

# Silicon dataset
silicium_range = np.array([5.780, 6.944, 8.177, 9.483, 10.863,
                          12.318, 13.848, 15.453, 17.134, 18.890,
                          22.63, 26.66, 30.99, 35.61, 40.52,
                          56.96, 89.91, 129.54, 175.60, 227.86,
                          286.1, 350.2, 419.9, 495.1, 575.9,
                          661.5, 752.4, 949.0, 1_164.6, 1_398.6,
                          2_821., 4_617., 6_732., 9_106., 11_705.,
                          14_502., 17_472., 20_595.,
                          ])

silicon_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
silicon_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
silicon_dataframe['A'] = 28
silicon_dataframe['Z'] = 14
silicon_dataframe['Z_material'] = 14
silicon_dataframe['A_material'] = 28