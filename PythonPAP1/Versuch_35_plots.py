import matplotlib.pyplot as plt
import numpy as np

# Abzisse
U = np.array([0.30, 0.20, 0.10, 0.00, -0.10, -0.20, -0.30, -0.40, -0.50, -0.60, 
              -0.70])

# # Neue Werte für Ordinate Violett
# sqrt_Ud = np.array([1.504, 1.445, 1.383, 1.325, 1.253, 1.189, 1.122, 1.061, 0.990,
#                     0.916, 0.833, 0.754, 0.663, 0.570, 0.482, 0.396, 0.316, 0.230])
# D_sqrt_Ud = np.array([0.011, 0.011, 0.011, 0.010, 0.010, 0.009, 0.009, 0.009, 0.008,
#                       0.008, 0.007, 0.007, 0.007, 0.006, 0.006, 0.005, 0.004, 0.004])

# #Blau
# sqrt_Ud = np.array([1.9100, 1.83139, 1.7473, 1.66943, 1.578, 1.493, 1.394, 1.294,
#                     1.182, 1.066, 0.957, 0.837, 0.709, 0.574, 0.445, 0.344, 0.219])

# D_sqrt_Ud = np.array([0.014, 0.014, 0.0129, 0.0124, 0.012, 0.011, 0.011, 0.010,
#                       0.009, 0.009, 0.008, 0.008, 0.007, 0.006, 0.005, 0.005, 0.004])

# # Grün
# sqrt_Ud = np.array([2.156, 2.030, 1.8992, 1.7595, 1.596, 1.405, 1.252, 1.166,
#                     0.871, 0.663, 0.447, 0.257, 0.1789])

# D_sqrt_Ud = np.array([0.018, 0.016, 0.0141, 0.0130, 0.012, 0.011, 0.010, 0.009,
#                       0.008, 0.007, 0.005, 0.004, 0.0033])

#Gelb
sqrt_Ud = np.array([1.8839, 1.7300, 1.585, 1.420, 1.260, 1.086, 0.899, 0.701,
                    0.505, 0.338, 0.192])

D_sqrt_Ud = np.array([0.0140, 0.0128, 0.012, 0.011, 0.010, 0.009, 0.008, 0.007,
                      0.006, 0.005, 0.003])



# Lineare Regression
coeff = np.polyfit(U, sqrt_Ud, 1)
line = np.poly1d(coeff)

# Plot mit Fehlerbalken
plt.errorbar(U, sqrt_Ud, yerr=D_sqrt_Ud, fmt='o', capsize=4, ecolor='red', markerfacecolor='blue', markersize=5)

# Ausgleichsgerade zeichnen
U_fit = np.linspace(min(U), max(U), 100)
plt.plot(U_fit, line(U_fit), 'green', label=f'Ausgleichsgerade: y = {coeff[0]:.3f}x + {coeff[1]:.3f}')

# Achsenbeschriftung, Titel, Raster
# plt.xlabel('U [V]')
# plt.ylabel('sqrt(U_d) [sqrt V]')
# plt.title('Plot von sqrt(U_d) gegen U mit Fehlerbalken und Ausgleichsgerade')
plt.grid(True)
# plt.legend()

# Achse x von -1.5 bis 0.3 in 0.1-Schritten
plt.xticks(np.arange(-2.3, 0.41, 0.15))

plt.yticks(np.arange(-0.3, 2.5, 0.1))


plt.show()
