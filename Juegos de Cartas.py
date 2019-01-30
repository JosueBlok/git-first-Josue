import random
class carta():

    def __init__(self, valor, simbolo):
        
        self.valor = valor # 0 es A, 1 es 2, 2 es 3, ..., 10 es J, 11 es Q, 12 es K
        self.simbolo = simbolo # 0 es diamantes, 1 es corazon, 2 es trebol, 3 es picas
        
    def mostrar(self):
        valores = {0 : "A", 1 : "2", 2 : "3", 3 : "4", 4 : "5", 5 : "6", 6 : "7", 7 : "8", 8 : "9", 9 : "10", 10 : "J", 11 : "Q", 12 : "K"}
        simbolos = {0 : "Diamantes", 1 : "Corazon", 2 : "Trebol", 3 : "Picas"}
        dicionario = {"valor" : valores[self.valor], "simbolo" : simbolos[self.simbolo]}
        return dicionario

        
            
class mazo():
    	
    def __init__(self):
        self.cartas = []

    def rellenar(self):
        for j in range(4):
            for i in range(13):
                self.cartas.append(carta(i, j))
                
    def barajar(self): #remueve la cartas, el arreglo cartas se llena con la cartas aleatoriamente
        cartas_barajadas = []
        while True:
            barajar = random.choice(self.cartas)
            if barajar not in cartas_barajadas:
                cartas_barajadas.append(barajar)
                self.cartas.remove(barajar)
            if len(cartas_barajadas) == 52:
                self.cartas = cartas_barajadas
                return self.cartas

    def quitar_arriba(self): #quita un objeto carta del array self.cartas
        carta_quitada = self.cartas.pop()
        return carta_quitada.mostrar()


        
class juego():

    def __init__(self):
        self.cartas_rival = []
        self.cartas_usuario = []
        self.segundo_mazo = []

    def repartir_cartas(self):
        for i in range(5):
            self.cartas_rival.append(mazo.quitar_arriba())
            self.cartas_usuario.append(mazo.quitar_arriba())
            
        self.segundo_mazo.append(mazo.quitar_arriba())    
        #print (self.cartas_rival, self.cartas_usuario, self.segundo_mazo)
    
    def rival(self):
        
        def botar(cartas): # esto lo cree para saber cual carta botar, el programa no botala cartas repetidas
            repetidos = []
            i, acu = 0, 0
            while i <= 4:
                for j in cartas:
                    if j["valor"] == cartas[i]["valor"]:
                        acu += 1
                repetidos.append(acu)
                acu = 0
                i += 1
            for idx,i in enumerate(repetidos):
                if i < 2:
                    return idx
            return 0                  

        #para cojer cartas del segundo mazo    
        for i in self.cartas_rival:
            if i["valor"] == self.segundo_mazo[len(self.segundo_mazo) - 1]["valor"]:
                carta_botar = botar(self.cartas_rival)
                self.cartas_rival.append(self.segundo_mazo[0])
                self.segundo_mazo.pop()
                self.segundo_mazo.append(self.cartas_rival[carta_botar])
                self.cartas_rival.pop(carta_botar)
                break
        #si no coje carta del segundo mazo, cojera del primer mazo
        carta_quitada = mazo.quitar_arriba()   
        for i in self.cartas_rival:
            if i["valor"] == carta_quitada["valor"]:
                carta_botar = botar(self.cartas_rival)
                self.cartas_rival.append(carta_quitada)           
                self.cartas_rival.pop(carta_botar)
        self.segundo_mazo.append(carta_quitada)        
           
        
#Preparacion            
mazo = mazo()
mazo.rellenar() #para rellenar las cartas
mazo.barajar() #para barajar las cartas
jugar = juego()
jugar.repartir_cartas() #reparte cartas a los jugadores

#Juego
def reglas_juego(cartas):
    
     repetidos = []
     i, acu = 0, 0
     while i <= 4:
         for j in cartas:
             if j["valor"] == cartas[i]["valor"]:            
                 acu += 1
         repetidos.append(acu)
         acu = 0
         i += 1

     dos = None
     tres = None
     for i in repetidos:
         if i == 2:
             dos = True
         if i == 3:
             tres = True
     if dos == True and tres == True:
         return True
     else:
         return False
        
def jugar_juego():
    while True:
        jugar.rival()
        verificar_ganador = reglas_juego(jugar.cartas_rival)
        if verificar_ganador == True:
           print ("JAJA Perdiste mojon, mi programa acaba de humillarte jaja xD")
           return False
        
        print ("Carta del mazo visible", jugar.segundo_mazo[len(jugar.segundo_mazo) - 1])
        print ("\nTus cartas")
        for idx, i in enumerate(jugar.cartas_usuario):
            print (idx, " - ", i)
        
        cojer_mazo_visible = input("Cojer del mazo visible y/n:  ")
        if cojer_mazo_visible == "y":
            carta = jugar.segundo_mazo.pop()
            jugar.cartas_usuario.append(carta)
            botar = input("Cual botas 0-1-2-3-4:  ")
            botada = jugar.cartas_usuario.pop(int(botar))
            jugar.segundo_mazo.append(botada)
            verificar_ganador = reglas_juego(jugar.cartas_usuario)
            if verificar_ganador == True:
                print ("Ganaste pendejo")
                return True 
            continue
        if   cojer_mazo_visible == "n":        
            pass
            
        cojer_mazo = input("Cojer del mazo y:   ")
        if cojer_mazo == "y":
            carta_cojida = mazo.quitar_arriba()
            print (carta_cojida)
            cojer_dejar = input("Cojer o Dejar y/n:  ")
            if cojer_dejar == "y":
                jugar.cartas_usuario.append(carta_cojida)
                botar = input("Cual botas 0-1-2-3-4:  ")
                botada = jugar.cartas_usuario.pop(int(botar))
                jugar.segundo_mazo.append(botada)
            if cojer_dejar == "n":
                jugar.segundo_mazo.append(carta_cojida)
                
        #print("\n\n\n", len(mazo.cartas), len(jugar.segundo_mazo))
        for i in jugar.cartas_rival:
            print (i["valor"])
        verificar_ganador = reglas_juego(jugar.cartas_usuario)
        if verificar_ganador == True:
            print ("Ganaste pendejo")
            return True
        
jugar_juego()
