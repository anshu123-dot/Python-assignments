class TicTacToe:
    def __init__(self):
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.current_winner = None  # Keep track of the winner!

    def print_board(self):
        for row in self.board:
            print([cell if cell is not None else '_' for cell in row])

    def available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] is None]

    def empty_squares(self):
        return any(None in row for row in self.board)

    def make_move(self, square, letter):
        row, col = square
        if self.board[row][col] is None:
            self.board[row][col] = letter
            if self.winner(row, col, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, row, col, letter):
        # Check the row
        if all([self.board[row][c] == letter for c in range(3)]):
            return True
        # Check the column
        if all([self.board[r][col] == letter for r in range(3)]):
            return True
        # Check diagonals
        if row == col and all([self.board[i][i] == letter for i in range(3)]):
            return True
        if row + col == 2 and all([self.board[i][2-i] == letter for i in range(3)]):
            return True
        return False
def minimax(board, depth, maximizing_player):
    if board.current_winner == 'O':
        return {'position': None, 'score': 1 * (len(board.available_moves()) + 1)}  # AI wins
    elif board.current_winner == 'X':
        return {'position': None, 'score': -1 * (len(board.available_moves()) + 1)}  # Human wins
    elif not board.empty_squares():
        return {'position': None, 'score': 0}  # Tie

    if maximizing_player:
        best = {'position': None, 'score': -float('inf')}
        letter = 'O'
    else:
        best = {'position': None, 'score': float('inf')}
        letter = 'X'

    for move in board.available_moves():
        board.make_move(move, letter)
        sim_score = minimax(board, depth + 1, not maximizing_player)
        board.board[move[0]][move[1]] = None
        board.current_winner = None
        sim_score['position'] = move

        if maximizing_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score

    return best
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()

    letter = 'X'  # Starting letter
    while game.empty_squares():
        if letter == 'O':
            move = o_player.get_move(game)
        else:
            move = x_player.get_move(game)

        if game.make_move(move, letter):
            if print_game:
                print(f"{letter} makes a move to {move}")
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It's a tie!")

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (row,col): ")
            try:
                row, col = map(int, square.split(','))
                if game.board[row][col] is None:
                    val = (row, col)
                    valid_square = True
                else:
                    print("Square is already filled. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        return val

class AIPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return (0, 0)  # Choose a corner for the first move
        return minimax(game, 0, self.letter == 'O')['position']

# Instantiate the game and players
game = TicTacToe()
human = HumanPlayer('X')
ai = AIPlayer('O')

# Start the game
play(game, human, ai)
