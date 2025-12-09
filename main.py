class Game:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.player = {}

    def display_board(self):
        b = """
"""
        for ligne in range(8):
            for colonne in range(8):
                b += str(self.board[ligne][colonne])
                b += " "
            b += "\n"

        print(b)

    def init_game(self):
        pieces_blanches = {
            "rooks": [Rook("blanc", (0, 0)), Rook("blanc", (0, 7))],
            "knights": [Knight("blanc", (0, 1)), Knight("blanc", (0, 6))],
            "bishops": [Bishop("blanc", (0, 2)), Bishop("blanc", (0, 5))],
            "pawns": [Pawn("blanc", (1, i)) for i in range(8)],
            "queen": Queen("noir", (0, 3)),
            "king": King("noir", (0, 4)),
        }

        pieces_noires = {
            "rooks": [Rook("noir", (7, 0)), Rook("noir", (7, 7))],
            "knights": [Knight("noir", (7, 1)), Knight("noir", (7, 6))],
            "bishops": [Bishop("noir", (7, 2)), Bishop("noir", (7, 5))],
            "pawns": [Pawn("noir", (6, i)) for i in range(8)],
            "queen": Queen("noir", (7, 4)),
            "king": King("noir", (7, 3)),
        }

        self.player["blanc"] = Player("blanc", pieces_blanches)
        self.player["noir"] = Player("noir", pieces_noires)

    def is_position_empty(self, coords):
        return self.board[coords[0]][coords[1]] == 0


class Player:
    def __init__(self, couleur, pieces):
        self.couleur = couleur
        self.pieces = pieces


class Pawn:
    def __init__(self, couleur, coords):
        self.couleur = couleur
        self.coords = coords
        game.board[coords[0]][coords[1]] = 1


class Rook:
    def __init__(self, couleur, coords):
        self.couleur = couleur
        self.coords = coords
        game.board[coords[0]][coords[1]] = 2


class Knight:
    def __init__(self, couleur, coords):
        self.couleur = couleur
        self.coords = coords
        game.board[coords[0]][coords[1]] = 3


class Bishop:
    def __init__(self, couleur, coords):
        self.couleur = couleur
        self.coords = coords
        game.board[coords[0]][coords[1]] = 4


class Queen:
    def __init__(self, couleur, coords):
        self.couleur = couleur
        self.coords = coords
        game.board[coords[0]][coords[1]] = 5


class King:
    def __init__(self, couleur, coords):
        self.couleur = couleur
        self.coords = coords
        game.board[coords[0]][coords[1]] = 6


game = Game()
game.init_game()
game.display_board()
