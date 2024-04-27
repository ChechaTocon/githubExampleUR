print("¡Bienvenido al programa conteo de vocales!\n")
print(
    "Este programa te ayudará a contar las vocales en una cadena de texto.\n ")

def conteo_vocales(cadena):  
  vocales = 'aeiouAEIOU'    
  contador = 0  
  for letra in cadena:    
    if letra in vocales:      
      contador += 1      
  return contador


cadena_ingresada = input("Ingrese un texto:  ")
print("\nEl numero total de vocales encontrado es:  ",
      conteo_vocales(cadena_ingresada))
