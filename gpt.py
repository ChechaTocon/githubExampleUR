def contar_pares(lista):
  count = 0
  for num in lista:
      if num % 2 == 0:
          count += 1
  return count

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cantidad_pares = contar_pares(mi_lista)
print("Cantidad de números pares en la lista:", cantidad_pares)
