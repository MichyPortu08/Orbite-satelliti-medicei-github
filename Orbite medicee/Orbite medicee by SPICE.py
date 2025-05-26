import spiceypy as spice
import matplotlib.pyplot as plt
import numpy as np

# Caricamento dei kernel SPICE
spice.furnsh("Kernel Nasa/naif0012.tls")
spice.furnsh("Kernel Nasa/jup365.bsp")
spice.furnsh("Kernel Nasa/pck00010.tpc")


# Tempo 0 di osservazione 
tempo_osservazione = spice.str2et("2025-01-01T00:00:00")

# Satelliti medicei di Giove (codici NAIF)
satelliti = {
    'Io': '501',
    'Europa': '502',
    'Ganimede': '503',
    'Callisto': '504'
}

# Suddivisione dell'orbita in angoli
angoli = np.linspace(0, 2 * np.pi, 720)

# Funzione per calcolare l'orbita del satellite
def calcola_orbita(id_satellite, tempo_base, passi=720):
    posizioni = []
    for angolo in angoli:
        tempo_shiftato = tempo_base + angolo * 691200  
        stato, _ = spice.spkezr(id_satellite, tempo_shiftato, "J2000", "NONE", "599")  # 599 = baricentro di Giove
        posizioni.append(stato[:3])  # cordinate spaziali (3 --> x,y,z)
    return np.array(posizioni)

# Grafico
plt.figure(figsize=(10, 10))

for nome, id_satellite in satelliti.items():
    orbita = calcola_orbita(id_satellite, tempo_osservazione)
    x, y = orbita[:, 0], orbita[:, 1]
    plt.plot(x, y, label=nome)

plt.gca().set_aspect('equal')
plt.legend()
plt.title("Satelliti medicei")
plt.show()


spice.unload("Kernel Nasa/naif0012.tls")
spice.unload("Kernel Nasa/jup365.bsp")
spice.unload("Kernel Nasa/pck00010.tpc")
