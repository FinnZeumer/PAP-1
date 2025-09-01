import csv
import matplotlib.pyplot as plt
import numpy as np

# values = []

# with open("PythonPAP1/11_nulldurchgang", newline="") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         for item in row:
#             try:
#                 values.append(round(float(item) / 3, 3))
#             except ValueError:
#                 continue

# def calc_mean_and_diffs(data):
#     mean_val = np.mean(data)
#     diffs = [round(v - mean_val, 3) for v in data]
#     diffs_percent = [round((v - mean_val) / mean_val * 100, 2) for v in data]
#     return mean_val, diffs, diffs_percent

# mean_val, diffs, diffs_percent = calc_mean_and_diffs(values)

# # Write results to CSV
# with open("output.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Index", "Value", "Difference", "Difference (%)"])
    
#     for i, (val, diff, diff_pct) in enumerate(zip(values, diffs, diffs_percent), start=1):
#         idx = (i - 1) % 10 + 1  # cycles index 1-10
#         writer.writerow([idx, val, diff, diff_pct])





# Daten
massen = np.array([50, 100, 150, 200, 250])

# Einzelmessungen flach auflisten
einzelmessungen_list = [0.927, 0.933, 0.940,
                        1.213, 1.218, 1.227,
                        1.500, 1.510, 1.493,
                        1.673, 1.680, 1.707,
                        1.863, 1.860, 1.847]

# Index für Einzelmessungen
index_einzel = np.arange(1, len(einzelmessungen_list)+1)

# Mittelwerte pro Masse
einzelmessungen_dict = {
    50: [0.927, 0.933, 0.940],
    100: [1.213, 1.218, 1.227],
    150: [1.500, 1.510, 1.493],
    200: [1.673, 1.680, 1.707],
    250: [1.863, 1.860, 1.847]
}
mittelwerte = [np.mean(einzelmessungen_dict[m]) for m in massen]

# X-Positionen der Mittelwerte: Mitte der jeweiligen Einzelmessungen
mittelwerte_index = [2, 5, 8, 11, 14]  # ungefähre Mitte je 3 Messungen pro Masse

# Plot
plt.figure(figsize=(8,5))

# Einzelmessungen
plt.scatter(index_einzel, einzelmessungen_list, color='blue', alpha=0.6, label='Einzelmessungen')

# Mittelwerte
plt.scatter(mittelwerte_index, mittelwerte, color='red', s=100, label='Mittelwerte')

# Achsenbeschriftung
plt.xlabel('Messung (der Einzelmessungen)')
plt.ylabel('Periodendauer T [s]')
plt.title('Periodendauer vs. Masse')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Optional: zweite X-Achse für Masse oben
ax = plt.gca()
ax2 = ax.twiny()
ax2.set_xlim(ax.get_xlim())
ax2.set_xticks(mittelwerte_index)
ax2.set_xticklabels(massen)
ax2.set_xlabel('Masse [g] (für Mittelwerte)')

plt.show()
