import numpy as np
import matplotlib.pyplot as plt

# DENNE ER IKKE KALIBRERT OG DET SYNS!

def load_canberra_mca(path):
    """
    Load a Canberra .mca file (text format) and return the counts as a NumPy array.
    This version uses latin-1 encoding to avoid UnicodeDecodeError.
    """
    counts = []
    with open(path, 'r', encoding='latin-1') as f:
        read_data = False
        for line in f:
            line = line.strip()
            if line == "<<DATA>>":
                read_data = True
                continue
            if line == "<<END>>":
                break
            if read_data and line:
                counts.append(int(line))
    return np.array(counts)

# --- Load and plot the spectrum ---
file_path = "Calibration/CE10182025_Xray_Co57_HC6928_p4.mca"

counts = load_canberra_mca(file_path)
channels = np.arange(len(counts))

plt.figure(figsize=(10, 5))
plt.step(channels, counts, where='mid')
plt.xlabel("Channel")
plt.ylabel("Counts")
plt.title("Spectrum — CE10182025_Xray_Co57_HC6928_p4")
plt.grid(True)
plt.tight_layout()
plt.show()
