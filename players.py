from random import randint

class Player:
    def __init__(self, pawn):
        self.pawn = pawn

    def user_move(self, board):
        user_pick = input(f"{self.pawn} Move. Enter row and column numbers (e.g. 11):")
        if len(user_pick) != 2 or user_pick[0] not in "123" or user_pick[1] not in "123":
            print("Invalid Move - Out of range! Try again.")
            self.user_move(board)
        else:
            row = int(user_pick[0]) - 1
            col = int(user_pick[1]) - 1
            if board[row][col] != "🔲":
                print("Invalid Move - Position taken! Try again.")
                self.user_move(board)
            else:
                board[row][col] = self.pawn

    def comp_move(self, board):
        row = randint(0, 2)
        col = randint(0, 2)
        if board[row][col] != "🔲":
            self.comp_move(board)
        else:
            print("My move:")
            board[row][col] = self.pawn
