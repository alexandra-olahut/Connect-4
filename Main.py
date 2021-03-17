from Domain import Board
from Service import Algorithm, Game , Algorithm_random
#from UI import UI
from GUI import GUI

board = Board()
ai = Algorithm()

game = Game(board, ai)


ui = GUI(game)
ui.start()

