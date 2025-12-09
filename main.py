"""
Le jeu fait 8x8 cases (64 cases au total)
Les cases vides sont attribuées par le nom "EC" (empty-case)

Les cases remplies sont constituées de 3 arguments:
- Le premier: Le type de pièce (Roi, Reine, Fou, Cavalier, Tour, Pion)
- Le deuxième: La couleur (Blanc ou Noir)
- Le troisième: la position de la case (A1, B3, etc.)

Le premier et le deuxième sont collés alors que le troisième est séparé par un tiret


A implémenter en cours demain:
- Système de déplacement (pour les pions) => 1/2 cases au début, puis 1 droite ou diagonale selon
    s'il peut manger ou pas

"""
class Game:
    def __init__(self):
        self.board = [["EC" for _ in range(8)] for _ in range(8)]
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
            "queen": Queen("blanc", (0, 3)),
            "king": King("blanc", (0, 4)),
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


class Piece:
    def __init__(self, couleur, coords):
        self.couleur = couleur
        self.coords = coords

        p_type = self.get_type()
        game.board[coords[0]][coords[1]] = p_type

    def get_coords(self):
        return self.coords


class Pawn(Piece):
    def get_type(self):
        return "PW" if self.couleur == "blanc" else "PB"


class Rook(Piece):
    def get_type(self):
        return "RW" if self.couleur == "blanc" else "RB"


class Knight(Piece):
    def get_type(self):
        return "NW" if self.couleur == "blanc" else "KB"


class Bishop(Piece):
    def get_type(self):
        return "BW" if self.couleur == "blanc" else "BB"


class Queen(Piece):
    def get_type(self):
        return "QW" if self.couleur == "blanc" else "QB"


class King(Piece):
    def get_type(self):
        return "KW" if self.couleur == "blanc" else "KB"


game = Game()
game.init_game()
game.display_board()
