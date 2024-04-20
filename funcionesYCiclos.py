# Usando un ciclo for
def sumarListaFor(lista):
  suma = 0
  for num in lista:
    suma += num
  return suma

# Usando un ciclo while
def sumarListaWhile(lista):
  suma = 0
  x = 0
  while x < len(lista): 
    suma += lista[x] 
    x += 1
  return suma

def productoListaWhile(lista):
  producto = 1
  x = 0
  while x < len(lista): 
    producto = producto * lista[x] 
    x += 1
  return producto


def productoListaFor(lista):
  producto = 1
  for num in lista:
    producto = producto * num
  return producto

def numerosParesFor(lista):
  modulo = 0
  contadorDePares=0
  for num in lista:
    modulo = num%2
    if modulo==0:
      contadorDePares+=1
  return contadorDePares

lista = [2, 10, 4, 20, 8]
resultado = numerosParesFor(lista)
print("la cantidad de numeros pares en la lista es:", resultado)