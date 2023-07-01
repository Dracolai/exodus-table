"""
Programme effectuant la conversion des données de la table de parcours de F. Hubert and R. Bimbot and H. Gauvin, 1990, "Stopping powers and ranges are tabulated for all ions of atomic number 2 ≤ Z ≤ 103 in the energy region 2.5 ≤ EA ≤ 500 MeV/u for 36 solid materials. 
The calculations use stopping powers for alpha particles and a new parameterization for the heavy-ion effective charge which is deduced from a set of about 600 experimental stopping-power values covering an energy range from 3 to 90 MeV/u for 15 incident heavy ions and 18 solid stopping materials."
https://doi.org/10.1016/0092-640X(90)90001-Z
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

# Scandium dataset
Scandium_range = np.array([6.070, 7.121, 8.212, 9.348, 10.739,
                           11.761, 13.042, 14.374, 15.755, 17.188,
                           20.21, 23.43, 26.85, 30.47, 34.29, 
                           46.93, 71.84, 101.37, 135.38, 173.70,
                           216.2, 262.8, 313.4, 367.8, 425.9, 
                           487.8, 553.2, 694.6, 849.4, 1_017.2,
                           2_035., 3_320., 4_831, 6_527., 8_384.,
                           10_382., 12_503., 14_734.,])

scandium_dataframe = pd.DataFrame()
scandium_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
scandium_dataframe['range_micron'] = Scandium_range/Convertion_factor['Si']
scandium_dataframe['A'] = 45
scandium_dataframe['Z'] = 21
scandium_dataframe['Z_material'] = 14
scandium_dataframe['A_material'] = 28

# Titanium dataset
Titanium_range = np.array([6.190, 7.242, 8.331, 9.463, 10.640,
                           11.863, 13.135, 14.455, 15.824, 17.242,
                           20.22, 23.40, 26.78, 30.35, 34.11, 
                           46.93, 71.84, 101.37, 135.38, 173.70,
                           216.2, 262.8, 313.4, 367.8, 425.9,
                           487.8, 553.2, 694.6, 849.4, 1_017.2, 
                           2_035., 3_320., 4_831, 6_527., 8_384.,
                           10_382., 12_503., 14_734.,])

titanium_dataframe = pd.DataFrame()
titanium_dataframe['energy_per_nucleon_mev'] = energy_per_nuc
titanium_dataframe['range_micron'] = Titanium_range/Convertion_factor['Si']
titanium_dataframe['A'] = 48
titanium_dataframe['Z'] = 22
titanium_dataframe['Z_material'] = 14
titanium_dataframe['A_material'] = 28

                           
                           



# Build a dataframe to make .csv file
# dataframe = pd.concat([helium_dataframe, lithium_dataframe,
#                           beryllium_dataframe, boron_dataframe, carbon_dataframe,
#                             nitrogen_dataframe, oxygen_dataframe, fluorine_dataframe,
#                                 neon_dataframe, sodium_dataframe, magnesium_dataframe,
#                                     aluminum_dataframe, silicon_dataframe, phosphorus_dataframe,
#                                         sulfur_dataframe, chlorine_dataframe, argon_dataframe,
#                                             potassium_dataframe, calcium_dataframe])

dataframe.to_csv('HBG_range_2.5_to_500_mev_per_nuc_1990_in_silicon_helium_to_calcium.csv', index=False, header=True)
