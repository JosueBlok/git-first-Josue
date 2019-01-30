
#   a b c d e f g h
# 1 R K B Q K B K R
# 2 p p p p p p p p
# 3 O * O * O * O *
# 4 * O * O * O * O
# 5 O * O * O * O *
# 6 * O * O * O * O
# 7 p p p p p p p p
# 8 R K B Q K B K R
class piece():

    def __init__(self, team, pos):
        self.position = pos
        self.team = team


class pawn(piece):

    # A pawn move one step by one but in the exit it can do two step in one move.
    pass


class knight(piece):

    # A knight (in spanish called horse), it can do a move of L in any directions
    # A knight can... like jump others pieces
    pass


class bishoop(piece):

    # A bishop can move in diagonals like a "X"
    pass


class rook(piece):

    # A rook (in spanish called tower), it can move straight but in diference of
    # a pawn is that the rook can move more than one step
    pass


class queen(piece):

    # A queen is the combination of bishoop and rook
    pass


class king(piece):  # PROGRESS
    pass

class boards():

def __init__(self):
        self.board = [
                [pawn("blanco", 0)], [pawn("blanco", 1)], [pawn("blanco", 3)], [pawn("blanco", 4)], [pawn("blanco", 5)], [pawn("blanco", 6)], [pawn("blanco", 7)], [pawn("blanco", 8)],
                [[], [], [], [], [], [], [], []],
                [[], [], [], [], [], [], [], []],
                [[], [], [], [], [], [], [], []],
                [[], [], [], [], [], [], [], []],
                [[], [], [], [], [], [], [], []],
                [[], [], [], [], [], [], [], []],
                [[], [], [], [], [], [], [], []]
                ]

    pass
josue = boards()
print (josue.board)
