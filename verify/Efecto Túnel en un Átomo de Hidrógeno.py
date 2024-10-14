import math

# Constantes
m = 9.11e-31  # Masa del electrón en kg
hbar = 1.055e-34  # Constante reducida de Planck en J·s
eV_to_J = 1.602e-19  # Factor de conversión de eV a Joules

# Parámetros del problema
E_eV = -3.4  # Energía del electrón en el primer estado excitado en eV
V0_eV = 0  # Altura de la barrera en eV
a = 0.1e-9  # Ancho de la barrera en metros

# Convertir energías de eV a Joules
E = E_eV * eV_to_J
V0 = V0_eV * eV_to_J

# Calcular gamma
gamma = math.sqrt((2 * m * (V0 - E)) / (hbar ** 2))

# Calcular la probabilidad de túnel
T = math.exp(-2 * gamma * a)

print(f'Gamma: {gamma:.6e} m^-1')
print(f'Probabilidad de túnel (T): {T:.6e}')
