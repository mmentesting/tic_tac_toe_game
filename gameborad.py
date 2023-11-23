
class GameBoard:
    def create_board(self):
        return [["🔲" for item in range(3)] for row in range(3)]

    def show_board(self, board):
        for row in board:
            modified_row = " | ".join(row)  # modified_row = " | ".join(row)
            print(modified_row)
