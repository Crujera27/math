# Datos del problema
lambda_nm = 600
d_mm = 0.5
L_m = 2

# Convertir d de mm a m
d = d_mm * 1e-3  

# Calcular distancia entre franjas
distancia_franja_mm = lambda_nm * L_m / d * 1e3  # Convertir a mm

print(f"Distancia entre franjas (λ = {lambda_nm} nm): {distancia_franja_mm:.2f} mm")

# Para λ' = 450 nm
lambda_prime_nm = 450
distancia_franja_prime_mm = lambda_prime_nm * L_m / d * 1e3  # Convertir a mm

print(f"Distancia entre franjas (λ' = {lambda_prime_nm} nm): {distancia_franja_prime_mm:.2f} mm")
