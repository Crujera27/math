# Datos del problema
probabilidad_inicial_estado_2 = 0.4
probabilidad_inicial_estado_1 = 1 - probabilidad_inicial_estado_2

# Probabilidad en dimensión alternativa
probabilidad_estado_2_nueva = probabilidad_inicial_estado_2 / 2

print(f"Probabilidad de medir el espín como ↓ en la dimensión alternativa: {probabilidad_estado_2_nueva:.2f}")
