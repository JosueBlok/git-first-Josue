import random
class carta():

    def __init__(self, valor, simbolo):
        
        self.valor = valor # 0 es A, 1 es 2, 2 es 3, ..., 10 es J, 11 es Q, 12 es K
        self.simbolo = simbolo # 0 es diamantes, 1 es corazon, 2 es trebol, 3 es picas
        
    def mostrar(self):
        valores = {0 : "A", 1 : 2, 2 : 3, 3 : 4, 4 : 5, 5 : 6, 6 : 7, 7 : 8, 8 : 9, 9 :10, 10 : "J", 11 : "Q", 12 : "K"}
        simbolos = {0 : "Diamantes", 1 : "Corazon", 2 : "Trebol", 3 : "Picas"}
        return valores[self.valor], simbolos[self.simbolo]
        
            
class mazo():
    	
    def __init__(self):
        self.cartas = []

    def rellenar(self):
        for j in range(4):
            for i in range(13):
                self.cartas.append(carta(i, j))
                
    def barajar(self):
        random.choice(self.cartas)
        
        
        
                

				 		 			    
prueba = mazo()
prueba.rellenar()
#print(len(prueba.cartas))
for i in prueba.cartas:
    print(i.mostrar())
prueba.barajar()
