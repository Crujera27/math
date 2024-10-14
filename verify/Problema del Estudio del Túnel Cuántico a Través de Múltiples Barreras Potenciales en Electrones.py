# Verificador del cálculo para el Problema del Estudio del Túnel Cuántico a Través de Múltiples Barreras Potenciales en Electrones
# Disponible en https://crujera.galnod.com/math/index.php

import math

# Constantes

m = 9.11e-31  # Masa del electrón en kg
hbar = 1.055e-34  # Constante reducida de Planck en J·s
eV_to_J = 1.602e-19  # Factor de conversión de eV a Joules

# Parámetros del problema

V01_eV = 10  # Altura de la primera barrera en eV
V02_eV = 15  # Altura de la segunda barrera en eV
E_eV = 8     # Energía del electrón en eV
a1 = 1e-9    # Ancho de la primera barrera en metros
a2 = 2e-9    # Ancho de la segunda barrera en metros

# Convertir energías de eV a Joules

V01 = V01_eV * eV_to_J  
V02 = V02_eV * eV_to_J 
E = E_eV * eV_to_J     

# Calcular gamma para ambas barreras

gamma1 = math.sqrt((2 * m * (V01 - E)) / (hbar ** 2))
gamma2 = math.sqrt((2 * m * (V02 - E)) / (hbar ** 2))

# Calcular probabilidades de túnel

T1 = math.exp(-2 * gamma1 * a1)
T2 = math.exp(-2 * gamma2 * a2)


print(f'Gamma para la primera barrera (gamma1): {gamma1:.6e} m^-1')
print(f'Gamma para la segunda barrera (gamma2): {gamma2:.6e} m^-1')
print(f'Probabilidad de túnel para la primera barrera (T1): {T1:.6e}')
print(f'Probabilidad de túnel para la segunda barrera (T2): {T2:.6e}')
