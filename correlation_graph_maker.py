import numpy as np
import matplotlib.pyplot as plt

R = 8.314
T = 298
kB = 1.38e-23
h = 6.63e-34
kmax = 1e9

dG = np.linspace(20e3, 120e3, 200)   # 20–120 kJ/mol
C = (kB * T) / (h * kmax)
P = C * np.exp(-dG / (R * T))

plt.semilogy(dG/1000, P)
plt.xlabel("Activation free energy $\Delta G^{\\ddagger}$ (kJ mol$^{-1}$)")
plt.ylabel("Reaction probability $P_{react}$")
plt.title("Dependence of reaction probability on activation energy")
plt.grid(True)
plt.show()
