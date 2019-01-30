class piece():

    def __init__(self, team, posX, posY, name):
        self.positionX = posX
        self.positionY = posY
        self.team = team
        self.name = name


class pawn(piece):
    def __str__(self):  #function para que no imprima en lenguaje maquina
        return "p"
    #     # A pawn move one step by one but in the exit it can do two step in one move.
    


class knight(piece):
    # A knight (in spanish called horse), it can do a move of L in any directions
    # A knight can... like jump others pieces
    def __str__(self): #function para que no imprima en lenguaje maquina
        return "Kn"


class bishoop(piece):
    def __str__(self): #function para que no imprima en lenguaje maquina
        return "B"


class rook(piece):
    # A rook (in spanish called tower), it can move straight but in diference of
    # a pawn is that the rook can move more than one step

    def __str__(self): #function para que no imprima en lenguaje maquina
        return "R"


class queen(piece):
    def __str__(self): #function para que no imprima en lenguaje maquina
        return "Q"


class king(piece):  # PROGRESS
    def __str__(self): #function para que no imprima en lenguaje maquina
        return "Kg"

