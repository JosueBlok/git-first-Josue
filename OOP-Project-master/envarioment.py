#   a b c d e f g h
# 1 R K B Q K B K R
# 2 p p p p p p p p
# 3 O * O * O * O *
# 4 * O * O * O * O
# 5 O * O * O * O *
# 6 * O * O * O * O
# 7 p p p p p p p p
# 8 R K B Q K B K R

import pieces

class board():

    def __init__(self):
        self.board =               [[" ", "A", "B", "C", "D", "E", "F", "G", "H"],
                                           ["1", "R", "K", "B", "Q",  "Kg", "B", "K", "R"],
                                           ["2", "p", "p", "p", "p", "p", "p", "p", "p"],
                                           ["3", "O", "*", "O", "*", "O", "*", "O", "*"],
                                           ["4", "*", "O", "*", "O", "*", "O", "*", "O"],
                                           ["5", "O", "*", "O", "*", "O", "*", "O", "*"],
                                           ["6", "*", "O", "*", "O", "*", "O", "*", "O"],
                                           ["7", "p", "p", "p", "p", "p", "p", "p", "p"],
                                           ["8", "R", "K", "B", "Kg", "Q", "B", "K", "R"]]
    def show(self):
        for entry in self.board:
            print(entry[0], entry[1], entry[2], entry[3],
                  entry[4], entry[5], entry[6], entry[7], entry[8])
        
    def fill(self): #entra las piezas(objetos) al tablero.

        #entra los peones, de ambos equipos.
        for columna in range( 1, 9 ): 
            for fila in range( 1, 3 ):                    
                if ( fila == 1):
                    if ( columna == 1):
                        self.board[columna][fila] = pieces.rook("white", columna, fila, "rook") #torres
                    if ( columna == 2 or columna == 7):
                        self.board[columna][fila] = pieces.knight("white", columna,  fila,"knight") #torres
                    if ( columna == 3 or columna == 6):
                        self.board[columna][fila]= pieces.bishoop("white", columna, fila,  "bishoop") #alfil
                    if ( columna == 4 ):
                        self.board[columna] [fila]= pieces.queen("white",columna, fila,  "queen") #reina
                    if ( columna == 5 ):
                        self.board[columna][fila] = pieces.king("white", columna, fila,"king") #rey
                if ( fila == 2 ):
                    self.board[columna][fila]= pieces.pawn("white", columna, fila,  "pawn") #peones
        
                    
                    
            

        
board = board()
board.fill()
board.show()
