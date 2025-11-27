# Ejercicio 2: Insertion Sort modificado con Busqueda Binaria

def busqueda_binaria_posicion(arr, val, inicio, fin):
    # Funcion para encontrar rapido la posicion donde va el valor
    while inicio < fin:
        mid = (inicio + fin) // 2
        if arr[mid] < val:
            inicio = mid + 1
        else:
            fin = mid
    return inicio

def insertion_sort_binario(arr):
    # Empezamos desde el segundo elemento
    for i in range(1, len(arr)):
        val = arr[i]
        
        # 1. Buscamos donde debe ir el valor (esto es rapido)
        posicion = busqueda_binaria_posicion(arr, val, 0, i)
        
        # 2. Insertamos el valor en su lugar
        # Quitamos el elemento de donde estaba
        arr.pop(i)
        # Lo metemos en la posicion correcta (esto mueve los demas)
        arr.insert(posicion, val)
        
    return arr

# Probamos el codigo
if __name__ == "__main__":
    datos = [34, 2, 15, 89, 12, 5, 50, 23, 1]
    print(f"Lista Original: {datos}")
    
    ordenada = insertion_sort_binario(datos)
    
    print(f"Lista Ordenada: {ordenada}")