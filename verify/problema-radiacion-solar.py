# Verificador del cálculo para el problema de Radiación Solar 1
# Disponible en https://crujera.galnod.com/math/index.php
import math

# Datos proporcionados
d_T = 1.5e8  # distancia media entre la Tierra y el Sol en kilómetros (150 millones de km)
I_T = 1370   # radiación solar media en la Tierra en W/m²
I_sat = I_T * 1.10  # radiación que recibe el satélite en W/m²
I_S = 1361   # radiación solar en el espacio vacío sin atmósfera en W/m²

# Calcular la radiación en la dimensión alternativa
I_alt = I_sat  # en la dimensión alternativa, la radiación es igual a la del satélite

# Calcular la distancia al Sol en la dimensión alternativa usando la ley del inverso del cuadrado
d_alt = d_T * math.sqrt(I_S / I_alt)

print(f"La distancia al Sol en la dimensión alternativa es aproximadamente {d_alt:.0f} km")
