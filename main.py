from players import Player
from gameborad import GameBoard
from brain import GameBrain

user1 = Player("💚")
user2 = Player("⭕")
game_board = GameBoard()
game_brain = GameBrain(user1, user2, game_board)


if __name__ == "__main__":
    game_brain.start_game()
