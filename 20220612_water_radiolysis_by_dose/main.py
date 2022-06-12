"""
This program is fundamentally referred to  ''N. M. Schneider et al., J Phys Chem C. 118, 22373–22382 (2014)''
"""
import numpy as np
import matplotlib.pyplot as plt

"""
Equilibrium constants @25℃
K2 : H2O <-> Hp + OHm
K3 : H2O2 <-> Hp + HO2m
K4 : OH <-> Hp + Om
K5 : HO2 <-> Hp + O2m
K6 : H <-> Hp + eaqm
"""
K2, K3, K4, K5, K6 = 10**-13.999, 10**-11.65, 10**-11.9, 10**-4.57, 10**-9.77
