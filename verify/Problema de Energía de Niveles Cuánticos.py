# Datos del problema
n1 = 5
n2 = 2
h = 6.626e-34  # J·s
c = 3e8        # m/s
eV_to_J = 1.602e-19  # Conversión de eV a J

# Energía de los niveles
E_n1 = -13.6 / n1**2
E_n2 = -13.6 / n2**2
delta_E = E_n2 - E_n1

# Convertir energía a longitud de onda
energia_J = delta_E * eV_to_J
longitud_onda_nm = h * c / energia_J * 1e9  # Convertir a nm

print(f"Longitud de onda del fotón emitido: {longitud_onda_nm:.2f} nm")
