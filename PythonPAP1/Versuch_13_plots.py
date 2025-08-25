import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def resonanzkurve(f, f0, Q):
    A = 1
    omega = 2 * np.pi * f
    omega_0 = 2 * np.pi * f0
    delta = omega_0 / (2 * Q)
    b_omega = (A * omega_0**2) / np.sqrt((omega_0**2 - omega**2)**2 + (2 * delta * omega)**2)
    return b_omega

# Parameter
f0 = 1.0
Q = 3
f = np.linspace(0, 2, 5000)

# Kurve berechnen
amplitude = resonanzkurve(f, f0, Q)

# Maximum
idx_max = np.argmax(amplitude)
f_max = f[idx_max]
b_max = amplitude[idx_max]

# Halbwertsbreite
def halbwert(f_hw):
    return resonanzkurve(f_hw, f0, Q) - b_max/np.sqrt(2)

f1 = fsolve(halbwert, f_max*0.8)[0]  # links
f2 = fsolve(halbwert, f_max*1.2)[0]  # rechts

b_half = b_max/np.sqrt(2)

# Plot
plt.figure(figsize=(8,5))
plt.plot(f, amplitude, label="Resonanzkurve")

# Vertikale Linien bis zur Kurve
plt.vlines(f_max, 0, b_max, color='#C61826', linestyle='--', label='Maximum')
plt.vlines(f1, 0, b_half, color='#590D08', linestyle='--', label='Halbwertspunkt')
plt.vlines(f2, 0, b_half, color='#590D08', linestyle='--')

# Horizontale Linie zwischen Halbwertpunkten
plt.hlines(b_half, f1, f2, colors='purple', linestyles='--', label='Halbwertbreite')

plt.xlabel("Frequenz [Hz]")
plt.xlim(0, 2)
plt.ylabel("Amplitude b(ω)")
plt.ylim(0, b_max*1.1)
# plt.title(f"Resonanzkurve: f0={f0} Hz, δ={(2 * np.pi * f0 / (2*Q)):.3f}")
plt.legend()
plt.grid(False)
plt.show()

# Ausgabe
print(f"Maximum: f_max = {f_max:.4f} Hz, b_max = {b_max:.4f}")
print(f"Halbwertspunkte: f1 = {f1:.4f} Hz, f2 = {f2:.4f} Hz")
print(f"Halbwertsbreite: Δf = {f2 - f1:.4f} Hz")
