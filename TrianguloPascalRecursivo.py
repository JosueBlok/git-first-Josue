array = [ [1],
        [1, 1] ]

#para arreglar el que implima dos gilas de mas pon dos array.pop() en el caso base, tienes que ser antes
#del for

def triangulo(n, pos_1=0, pos_2=1, poc_array=1):
 
  #Caso Base
  if (n == 0):
    array.pop()
    array.pop()
    for i in array:
      print i
    return array

  #Recursividad
  if (pos_1 == 0):
    array.append([1])
  resultado = array[poc_array][pos_1] + array[poc_array][pos_2]
  array[poc_array + 1].append(resultado)

  if ( len(array[poc_array + 1]) == len(array[poc_array]) ):
    array[poc_array + 1].append(1)
    return triangulo((n-1), 0, 1, (poc_array + 1))
  return triangulo(n, (pos_1 + 1), (pos_2 + 1), poc_array)

triangulo(10)