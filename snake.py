class Board:

    def __init__(self, x, y):
        self.board = [["0" for _ in range(x)] for _ in range(y)]
        self.snake = [[y // 2, x // 2]]
        self.snakeInit()

    def snakeInit(self):
        if len(self.snake) == 1:
            self.board[self.snake[0][0]][self.snake[0][1]] = "X"

    def snakeMove(self, move):
        if move == "h":
            self.board[self.snake[0][0]][self.snake[0][1]] = "0"
            self.snake[0][1] -= 1
            self.snakeInit()
        elif move == "l":
            self.board[self.snake[0][0]][self.snake[0][1]] = "0"
            self.snake[0][1] += 1
            self.snakeInit()
        elif move == "k":
            self.board[self.snake[0][0]][self.snake[0][1]] = "0"
            self.snake[0][0] -= 1
            self.snakeInit()
        elif move == "j":
            self.board[self.snake[0][0]][self.snake[0][1]] = "0"
            self.snake[0][0] += 1
            self.snakeInit()

    def __str__(self):
        matrix = []
        for row in self.board:
            matrix.append(" ".join(row))
        return "\n".join(matrix) + "\n"
