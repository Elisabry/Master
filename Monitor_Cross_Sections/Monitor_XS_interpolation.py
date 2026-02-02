import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator


def load_iaea_file(path):
    data = []
    with open(path) as f:
        for line in f.readlines()[6:]:
            try:
                e, xs, unc = map(float, line.split()[:3])
                data.append((e, xs, unc))
            except ValueError:
                pass

    if len(data) < 2:
        return None

    E, xs, unc = map(np.array, zip(*data))
    return PchipInterpolator(E, xs, extrapolate=False)


# energy grid
E_mon = np.linspace(0, 50, 100_000)

base = os.path.dirname(__file__)
data_dir = os.path.join(base, "IAEA_Monitor_Data")

# Minimal change: accept all .txt files in the folder
curves = [
    (fname.replace(".txt", ""), load_iaea_file(os.path.join(data_dir, fname)))
    for fname in sorted(os.listdir(data_dir))
    if fname.endswith(".txt")
]


for label, interp in filter(lambda x: x[1] is not None, curves):
    y = interp(E_mon)
    mask = ~np.isnan(y)
    plt.plot(E_mon[mask], y[mask], label=label)

plt.xlabel("Proton Energy (MeV)", fontsize=14)
plt.ylabel("Cross Section (mb)", fontsize=14)
plt.title(r"IAEA Monitor Cross Sections for Cu,p and Ni,p", fontsize=14)
plt.legend()
plt.xlim(0, 50)
plt.ylim(0, 400)
plt.show()
