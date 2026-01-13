class Board:

    def __init__(self, x, y):
        self.board = [["0" for _ in range(x)] for _ in range(y)]

    def __str__(self):
        matrix = []
        for row in self.board:
            matrix.append(" ".join(row))
        return "\n".join(matrix)
