"""
This program is fundamentally referred to  ''N. M. Schneider et al., J Phys Chem C. 118, 22373–22382 (2014)''
"""
import numpy as np
import matplotlib.pyplot as plt

"""
G-Values (Molecules/eV) taken from Hill and Smith for 300 keV.
"""
gEm, gH, gH2, gOH, gH2O2, gHO2, gHp, gOHm = 3.47/100, 1.00/100, 0.17/100, 3.63/100, 0.47/100, 0.08/100, 4.42/100, 0.95/100
"""
Equilibrium constants @25℃
K2 : H2O <-> Hp + OHm
K3 : H2O2 <-> Hp + HO2m
K4 : OH <-> Hp + Om
K5 : HO2 <-> Hp + O2m
K6 : H <-> Hp + eaqm
"""
K2, K3, K4, K5, K6 = 10**-13.999, 10**-11.65, 10**-11.9, 10**-4.57, 10**-9.77
"""
Reaction Rates
K7 : Hp + OHm -> H2O
K8 : H2O  -> Hp + OHm
K9 : H2O2 -> Hp + HO2m
K10 : Hp + HO2m -> H2O2
K11 : H2O2 + OHm -> HO2m + H2O
K12 : HO2m + H2O -> H2O2 + OHm
K13 : eaqm + H2O -> H + OHm
K14 : H + OHm -> eaqm + H2O
K15 : H -> eaqm + Hp
K16 : eaqm + Hp -> H
K17 : OH + OHm -> Om + H2O
K18 : Om + H2O -> OH + OHm
"""
K7 = 1.4*10**11
K8 = K7*K2