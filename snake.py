class Board:

    def __init__(self, x, y):
        self.board = [["0" for _ in range(x)] for _ in range(y)]
        self.snake = [[y // 2, x // 2]]

    def snakeInit(self):
        if len(self.snake) == 1:
            self.board[self.snake[0][0]][self.snake[0][1]] = "X"

    def __str__(self):
        matrix = []
        for row in self.board:
            matrix.append(" ".join(row))
        return "\n".join(matrix)
