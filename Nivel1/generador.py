def factoeres(n):
  for i in range(1, n+1):
    if n % i == 0:
      yield i #la palabra yield se utiliza en funciones generadoras
    
for factor in factoeres(100):
  print(factor)

#al utilizar yield puede generar y entregar cada factor uno a uno sin tener que almaecenar todos los valores en una lista
