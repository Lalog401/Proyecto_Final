import sys

# Ejercicio 4: Triangulo de Mayor Area

def calcular_area(p1, p2, p3):
    # Formula del determinante para sacar el area con coordenadas
    val = p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])
    return 0.5 * abs(val)

def resolver_triangulo():
    postes = []
    
    # Intentamos leer el archivo campo.in
    try:
        with open('campo.in', 'r') as f:
            for linea in f:
                datos = list(map(int, linea.split()))
                # El archivo termina con -1 -1
                if datos == [-1, -1]: break
                postes.append(datos)
    except FileNotFoundError:
        print("No se encontro el archivo campo.in")
        return

    n = len(postes)
    print(f"Procesando {n} postes...")
    
    max_area = -1.0
    mejor_triangulo = []

    # Fuerza Bruta: Tres ciclos para probar todas las combinaciones posibles
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                
                # Calculamos el area de estos 3 puntos
                area_actual = calcular_area(postes[i], postes[j], postes[k])
                
                # Si encontramos una mas grande, actualizamos
                if area_actual > max_area:
                    max_area = area_actual
                    mejor_triangulo = [postes[i], postes[j], postes[k]]

    # Imprimimos y guardamos el resultado
    print(f"Area Maxima: {max_area}")
    
    try:
        with open('campo.out', 'w') as f:
            for p in mejor_triangulo:
                f.write(f"{p[0]} {p[1]}\n")
        print("Archivo campo.out creado.")
    except IOError:
        print("Error al guardar el archivo.")

if __name__ == "__main__":
    resolver_triangulo()