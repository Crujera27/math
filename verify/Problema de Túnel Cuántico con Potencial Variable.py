# Disponible en https://crujera.galnod.com/math/index.php
import math

# Datos del problema
m = 9.109e-31  # kg (masa del electrón)
hbar = 1.055e-34  # J·s
k = 1e-20  # Constante de potencial (arbitraria para el ejemplo)
E = 1e-20  # Energía (arbitraria para el ejemplo)
x = 1e-10  # Posición en metros

# Calcular k
kappa = math.sqrt(2 * m * (k * x - E) / hbar**2)

print(f"Constante de decaimiento κ: {kappa:.2f} m⁻¹")
