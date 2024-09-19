# Datos del problema
n = 3
L_nm = 1
L_m = L_nm * 1e-9  # Convertir nm a metros
hbar = 1.055e-34  # J·s
m = 9.109e-31     # kg (masa del electrón)
pi = 3.14159

# Calcular energía
E_n = (n**2 * pi**2 * hbar**2) / (2 * m * L_m**2)

print(f"Energía en el estado n={n} (L = {L_nm} nm): {E_n:.2e} J")
