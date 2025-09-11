import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import matplotlib.ticker as ticker


# def resonanzkurve(f, f0, Q):
#     A = 1
#     omega = 2 * np.pi * f
#     omega_0 = 2 * np.pi * f0
#     delta = omega_0 / (2 * Q)
#     b_omega = (A * omega_0**2) / np.sqrt((omega_0**2 - omega**2)**2 + (2 * delta * omega)**2)
#     return b_omega

# # Parameter
# f0 = 1.0
# Q = 3
# f = np.linspace(0, 2, 5000)

# # Kurve berechnen
# amplitude = resonanzkurve(f, f0, Q)

# # Maximum
# idx_max = np.argmax(amplitude)
# f_max = f[idx_max]
# b_max = amplitude[idx_max]

# # Halbwertsbreite
# def halbwert(f_hw):
#     return resonanzkurve(f_hw, f0, Q) - b_max/np.sqrt(2)

# f1 = fsolve(halbwert, f_max*0.8)[0]  # links
# f2 = fsolve(halbwert, f_max*1.2)[0]  # rechts

# b_half = b_max/np.sqrt(2)

# # Plot
# plt.figure(figsize=(8,5))
# plt.plot(f, amplitude, label="Resonanzkurve")

# # Vertikale Linien bis zur Kurve
# plt.vlines(f_max, 0, b_max, color='#C61826', linestyle='--', label='Maximum')
# plt.vlines(f1, 0, b_half, color='#590D08', linestyle='--', label='Halbwertspunkt')
# plt.vlines(f2, 0, b_half, color='#590D08', linestyle='--')

# # Horizontale Linie zwischen Halbwertpunkten
# plt.hlines(b_half, f1, f2, colors='purple', linestyles='--', label='Halbwertbreite')

# plt.xlabel("Frequenz [Hz]")
# plt.xlim(0, 2)
# plt.ylabel("Amplitude b(ω)")
# plt.ylim(0, b_max*1.1)
# # plt.title(f"Resonanzkurve: f0={f0} Hz, δ={(2 * np.pi * f0 / (2*Q)):.3f}")
# plt.legend()
# plt.grid(False)
# plt.show()

# # Ausgabe
# print(f"Maximum: f_max = {f_max:.4f} Hz, b_max = {b_max:.4f}")
# print(f"Halbwertspunkte: f1 = {f1:.4f} Hz, f2 = {f2:.4f} Hz")
# print(f"Halbwertsbreite: Δf = {f2 - f1:.4f} Hz")


def plot_with_fit(x, y1, y2, label, color):
    # average and std from two measurements
    y1 = np.array(y1, dtype=float)
    y2 = np.array(y2, dtype=float)
    y_avg = (y1 + y2) / 2
    y_std = np.std(np.vstack([y1, y2]), axis=0, ddof=1)

    # fit ln(y) = a + b·x
    mask = y_avg > 0
    coeffs = np.polyfit(x[mask], np.log(y_avg[mask]), 1)
    b, a = coeffs[0], coeffs[1]
    y_fit = np.exp(a + b * x)

    # plot data points with error bars
    ax.errorbar(x, y_avg, yerr=y_std, fmt="o", 
                color=color, label=f"{label} data", capsize=3)

    # plot exponential fit
    ax.semilogy(x, y_fit, color=color, linestyle="--", 
                label=f"{label} fit")

    return a, b


# Periods
x = np.arange(1, 16)

# 340 mA data (two measurements)
y1_340 = [15.0, 13.0, 11.0, 8.8, 7.6, 6.4, 5.2, 4.6, 3.8, 3.2, 2.6, 2.2, 1.8, 1.6, 1.2]
y2_340 = [14.6, 12.2, 10.2, 8.6, 6.8, 5.8, 4.6, 3.8, 3.0, 2.4, 1.8, 1.4, 1.0, 0.8, 0.4]

# 440 mA data (only first 10 periods measured)
y1_440 = [14.2, 10.4, 8.0, 5.8, 4.2, 3.6, 2.6, 2.0, 1.0, 1.0]
y2_440 = [13.2, 10.0, 7.4, 5.2, 3.8, 2.6, 1.8, 1.4, 0.8, 0.4]
x_440 = np.arange(1, len(y1_440) + 1)


# fig, ax = plt.subplots(figsize=(8.27, 11.69)) # A4
fig, ax = plt.subplots(figsize=(7.0866, 10.31496))  # 180mm x 262mm plotting area

# plot both
a340, b340 = plot_with_fit(x, y1_340, y2_340, "340 mA", "blue")
a440, b440 = plot_with_fit(x_440, y1_440, y2_440, "440 mA", "red")

# grid and ticks
ax.set_axisbelow(True)
ax.grid(which="both", linestyle=":", linewidth=0.7, color="gray")
# ax.set_ylim(1e-2, 1e1)
ax.set_ylim(-100, 100) 
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2))
ax.yaxis.set_major_locator(ticker.LogLocator(base=10.0, subs=None))
ax.yaxis.set_major_formatter(ticker.LogFormatterMathtext(base=10.0))

# Minor ticks at 2..9 in each decade
ax.yaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs=np.arange(1.0, 10.0)*0.1, numticks=100))

ax.set_xlim(0, 18)
ax.xaxis.set_major_locator(plt.MultipleLocator(1))   # each major tick = 1 unit = 10 mm
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2)) # optional minor ticks
# ax.set_xlabel("Period")
# ax.set_ylabel("Amplitude [units]")
# ax.set_title("Average amplitude with error bars and exponential fits")
# ax.legend()

plt.tight_layout()
plt.show()

print("340 mA fit: y = exp({:.3f} + {:.3f}·x)".format(a340, b340))
print("440 mA fit: y = exp({:.3f} + {:.3f}·x)".format(a440, b440))