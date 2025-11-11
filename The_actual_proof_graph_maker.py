import numpy as np
import matplotlib.pyplot as plt

R = 8.314
kB = 1.38e-23
h = 6.63e-34
kmax = 1e9
dG = 75e3  # J/mol

T = np.linspace(250, 400, 200)
C = (kB * T) / (h * kmax)
P = C * np.exp(-dG / (R * T))

plt.semilogy(T, P)
plt.xlabel("Temperature (K)")
plt.ylabel("Reaction probability $P_{react}$")
plt.title("Temperature dependence of reaction probability")
plt.grid(True)
plt.show()
