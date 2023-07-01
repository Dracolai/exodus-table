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
#Initialisation of the dataframe
helium_dataframe = pd.DataFrame()

#  Berillium range
helium_range = np.array([13.83, 18.63, 24.07, 30.14, 36.82,
                         44.12, 52.01, 60.49, 69.55, 79.19,
                         100.17, 123.38, 148.79, 176.35, 206.03,
                         307.5, 516.8, 773.8, 1076.7, 1423.5,
                         1_813., 2_243., 2_714., 3_223., 3_770., 
                         4_354., 4_973., 6_318., 7_797., 9_406.,
                         19_238., 31_735., 46_469., 63_057., 81_257., 
                         100_868., 121_426., 143_688.,])

row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['Be']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 4
row['A_material'] = 9
helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)

#  Carbon range 
helium_range = np.array([13.43, 17.92, 23.00 ,26.66, 34.89,
                         41.67, 49.01, 56.58, 65.29, 74.23, 93.66, 
                         115.14, 138.63, 164.09, 191.49, 
                         285.1, 477.1, 714.1, 992.2, 1_310.5,
                         1_668., 2_062., 2_493., 2_959., 3_460., 
                         3_994., 4_561., 5_790., 7_142., 8_611., 
                         17_586., 28_927., 42_211., 57_159., 73_556.,
                         91_220., 110_004., 129_779.,
                            ])  
row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['C']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 6
row['A_material'] = 12
helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)

#  Magnesium range

helium_range = np.array([16.22, 21.66,27.81, 34.60, 42.04,
                         50.11, 58.81, 68.13, 78.05, 88.57, 
                         111.37, 136.49, 163.87, 193.47, 225.26, 
                         333.4, 554.7, 824.7, 1_141.2, 1502.3,
                         1_906., 2_352., 2_837., 3_362., 3_924., 
                         4_524., 5_159., 6_535., 8_045., 9_683., 
                         19_650., 32_208., 46_883., 63_364., 81_416., 
                         100_839., 121_471., 143_173.,
                            ])
row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['Mg']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 12
row['A_material'] = 24
helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)

#  Aluminum range
helium_range = np.array([16.76, 22.41, 28.77, 35.80, 43.51, 
                         51.87,60.87, 70.51, 80.78, 91.66, 
                         115.25, 141.23, 169.54, 200.15, 233.02, 
                         344.8, 573.4, 852.3, 1_179.1, 1551.8,
                         1_969., 2_428., 2_929., 3_470., 4_051., 
                         4_669., 5_324, 6_742., 8_229., 9_988., 
                         20_257., 33_208., 48_352., 65_362., 83_992.,
                         104_041., 125_339., 147_743.])

row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['Al']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 13
row['A_material'] = 27
helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)
                         
#  Silicim range
helium_range = np.array([16.61, 22.13, 28.33, 35.20, 42.71,
                         50.86, 59.64, 69.03, 79.02, 89.62,
                         112.58, 137.84, 165.37, 195.13, 227.06,
                         335.6, 557.5, 828.0, 1_144.8, 1_506.1,
                         1_910., 2_355., 2_841., 3_365., 3_927.,
                         4_526., 5_161., 6_534., 8_042., 9_678.,
                         19_629., 32_202., 47_001., 63_621., 81_818,
                         101_394., 122_183., 144_045.,
                         ])

row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['Si']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 14
row['A_material'] = 28
helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)

#  Calcium range

helium_range = np.array([17.81, 23.64, 30.17, 37.38, 45.27,
                         53.82,63.01, 72.83, 83.29, 94.36,
                         118.31, 144.65, 173.32, 204.27, 237.46,
                         350.2, 580., 859.6, 1_186.6, 1_559.1,
                         1_975., 2_434., 2_933., 3_472., 4_049., 
                         4_664., 5315., 6_724, 8_270., 9_946., 
                         20_126., 32_950., 47_928., 64_737., 83_134.,
                         102_919., 123_931., 146_021.,])

row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['Ca']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 20
row['A_material'] = 40
helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)

# Titanium range

helium_range = np.array([20.36, 27.03, 34.48, 42.69, 51.66, 
                         61.36, 71.78, 82.91, 94.74, 107.25,
                         134.32, 164.04, 196.35, 231.21, 268.57,
                         395.3, 653.1, 966.3, 1_332.2, 1_748.6,
                         2_213., 2_725., 3_282., 3_883., 4_526., 
                         5_212., 5_937., 7_506., 9_227., 11_091., 
                         22_407., 36_657., 53_308., 71_987., 92_425., 
                         114_400., 137_728., 162_254.,])

row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['Ti']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 22
row['A_material'] = 48
helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)

# Chromium range

helium_range = np.array([21.55, 28.44, 36.14, 44.62, 53.87,
                         63.86, 74.59, 86.04, 98.19, 11.05,
                         138.04, 169.31, 202.43, 238.13, 276.38,
                         405.9, 669.2, 988.7, 1_361.6, 1_785.6,
                         2_259., 2_779., 3_346., 3_957., 4_611., 
                         5_307., 6_045., 7_639., 9_385., 11_279., 
                         22_759., 37_220., 54_268., 73_604., 94_822., 
                         117_613., 141_785., 167_172.,])

row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['Cr']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 24
row['A_material'] = 52
helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)

# Iron range

helium_range = np.array([22.08, 29.11,36.96, 45.59, 54.99,
                         65.15, 76.05, 87.67, 100.01, 113.05,
                            141.22, 172.10, 205.63, 241.77, 280.46,
                            411.4, 677.3, 999.7, 1_375.7, 1_803., 2_280.,
                            2_804., 3_374., 3_989., 4_647., 
                            5_348., 6_089., 7_691., 9_447., 11_349., 
                            22_877., 37_358., 54_242., 73_169., 93_870,
                            116_115., 139_728.,164_540., ])

row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['Fe']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 26
row['A_material'] = 56
helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)

# Nickel range

helium_range = np.array([22.78, 29.92, 37.86, 46.59, 56.08, 
                         66.31, 77.28, 88.97, 101.37, 114.47, 
                         142.72, 173.67, 207.24, 243.39, 282.07,
                         412.09, 678.0, 999.0, 1_373.2, 1_798.1, 
                         2_272., 2_792., 3_359., 3_969., 4_622.,
                         5_317., 6_053., 7_642., 9_382., 11_267., 
                         22_680., 36_996., 53_676., 72_369., 92_806., 
                         114_764., 138_061., 162_540.,])

row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['Ni']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 28
row['A_material'] = 58

helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)

# Copper range

helium_range = np.array([24.27, 31.85, 40.28, 49.53, 59.60,
                         70.45, 82.07, 94.45, 107.58, 121.45, 
                         151.36, 184.11, 219.63, 257.87, 298.78,
                         437.1, 717.2, 1_056.3, 1_451.4, 1_899.9,
                         2_400., 2_949., 3_547., 4_190., 4_879., 
                         5_612. ,6388., 8_063., 9_898., 11_885., 
                         23_911., 39_004., 56_595., 76_304., 97_846.,
                         120_988., 154_536., 171_325.,])

row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['Cu']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 29
row['A_material'] = 63

helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)

# Germanium range

helium_range = np.array([24.94, 32.90, 41.76, 51.47, 62.02,
                         73.39, 85.57, 98.54, 112.28, 126.80, 
                         158.08, 192.32, 229.44, 269.39, 312.11,
                         456.4, 746.6, 1_102., 1_513.4, 1_980.4,
                         2_501., 3_072., 3_694., 4_363., 5_080.,
                         5_842., 6_648., 8_389., 10_295., 12_360., 
                         24_849., 40_190., 58_052., 78_071., 99_960., 
                         123_485., 148_851., 174_690.,])

row = pd.DataFrame()
row['energy_per_nucleon_mev'] = energy_per_nuc
row['range_micron'] = helium_range/Convertion_factor['Ge']
row['A'] = 4
row['Z'] = 2
row['Z_material'] = 32
row['A_material'] = 72

helium_dataframe = pd.concat([helium_dataframe, row], ignore_index=True)