from players import Player
from gameborad import GameBoard
from time import sleep

class GameBrain:
    def __init__(self, player1: Player, player2: Player, g_board: GameBoard):
        self.players = [player1, player2]
        self.g_board = g_board

    def start_game(self):
        game_on = True
        num_of_players = input("Play Tic Tac Toe!\nFor 2 players press '2': ")
        board = self.g_board.create_board()
        self.g_board.show_board(board)
        while game_on:
            self.players[0].user_move(board)
            self.g_board.show_board(board)
            game_on = self.check_winner(board, self.players[0].pawn)
            if game_on:
                if num_of_players == "2":
                    self.players[1].user_move(board)
                else:
                    sleep(1)
                    self.players[1].comp_move(board)
                self.g_board.show_board(board)
                game_on = self.check_winner(board, self.players[1].pawn)
        if input("Press Y to play again: ").upper() == "Y":
            self.start_game()

    def check_winner(self, board, player):
        for row in board:  # horizontal check
            if row[0] == row[1] == row[2] == player:
                print(f"{player} Wins!")
                return False
        for col in range(3):  # vertical check
            if board[0][col] == board[1][col] == board[2][col] == player:
                print(f"{player} Wins!")
                return False
        if board[0][0] == board[1][1] == board[2][2] == player \
                or board[0][2] == board[1][1] == board[2][0] == player:  # diagonal check
            print(f"{player} Wins!")
            return False
        if not any("🔲" in rows for rows in board):
            print("Its a Draw.")
            return False
        return True
