import math

def distancia_euclidiana(x1, y1, x2, y2):
    resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(resultado, 5)

