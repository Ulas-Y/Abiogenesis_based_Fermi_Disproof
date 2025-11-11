import numpy as np
import matplotlib.pyplot as plt

R = 8.314
T = 298
H = np.linspace(-20e3, 120e3, 200)   # enthalpy (J/mol)
S = np.linspace(-200, 200, 200)      # entropy (J/mol·K)
H, S = np.meshgrid(H, S)

G = H - T*S
P = np.exp(-G / (R*T))

plt.figure(figsize=(7,5))
cp = plt.contourf(H/1000, S, np.log10(P), 40, cmap='viridis')
plt.colorbar(cp, label='log$_{10}(P_{thermo})$')
plt.xlabel('ΔH (kJ mol$^{-1}$)')
plt.ylabel('ΔS (J mol$^{-1}$ K$^{-1}$)')
plt.title('Thermodynamic landscape of reaction probability')
plt.tight_layout()
plt.show()
