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

#Initialise le dataframe 
beryllium_dataframe = pd.DataFrame()

silicium_range = np.array([10.750, 13.946, 17.508, 21.432, 26.710,
                            30.34, 35.31, 40.63, 46.28, 52.27,
                            65.22, 79.49, 94.98, 111.74, 129.72,
                            190.8, 315.7, 467.8, 646.1, 849.3,
                            1_076.6, 1_327.1, 1_600.1, 1_895., 2_211.1,
                            2_548., 2_905., 3_678., 4_526., 5_446.,
                            11_043., 18_116., 26_440., 35_789., 46_025.,
                            57_036., 68_730., 81_028.,
                            ])

beryllium_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
beryllium_dataframe['range_micron'] = silicium_range/Convertion_factor['Si']
beryllium_dataframe['A'] = 9
beryllium_dataframe['Z'] = 4
beryllium_dataframe['Z_material'] = 14
beryllium_dataframe['A_material'] = 28