import spiceypy as spice
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

spice.furnsh("Kernel Nasa/naif0012.tls")
spice.furnsh("Kernel Nasa/jup365.bsp")
spice.furnsh("Kernel Nasa/pck00010.tpc")


tempo_osservazione = spice.str2et("2025-01-01T00:00:00")

# Satelliti medicei di Giove
satelliti = {
    'Io': '501',
    'Europa': '502',
    'Ganimede': '503',
    'Callisto': '504'
}


angoli = np.linspace(0, 2 * np.pi, 720)

# Funzione per calcolare le orbite
def calcola_orbita(id_satellite, tempo_base, passi=720):
    posizioni = []
    for angolo in angoli:
        tempo_shiftato = tempo_base + angolo * 691200  
        stato, _ = spice.spkezr(id_satellite, tempo_shiftato, "J2000", "NONE", "599")  
        posizioni.append(stato[:3])  
    return np.array(posizioni)


fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')


for nome, id_satellite in satelliti.items():
    orbita = calcola_orbita(id_satellite, tempo_osservazione)
    x, y, z = orbita[:, 0], orbita[:, 1], orbita[:, 2]
    ax.plot(x, y, z, label=nome)


ax.set_title("Orbita 3D dei satelliti medicei")
ax.legend()
plt.show()

spice.unload("Kernel Nasa/naif0012.tls")
spice.unload("Kernel Nasa/jup365.bsp")
spice.unload("Kernel Nasa/pck00010.tpc")
