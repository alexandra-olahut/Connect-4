#from texttable import Texttable
'''
class UI:

    def __init__(self, game):
        self.game = game
        self.message = {1:'You lost', -1:'You won', 0:"It's a tie"}

    def read_move(self):
        while True:
            try:
                invalid_input = False
                column = int(input('Column: '))
                if column<0 or column>6:
                    print('Invalid input')
                    invalid_input = True
            except ValueError:
                print('Invalid input')
                invalid_input = True
            if invalid_input == False:
                return column
            
    
    def print_board(self):
        board = self.game.get_board()
        t = Texttable()
        for line in board:
            t.add_row(line)
        print(t.draw())
            
            
    def start(self):
        self.print_board()
        game_over = False
        player = True
        while game_over == False:
            while True:
                try:
                    if player:
                    # player's turn
                        column = self.read_move()
                        self.game.player_move(column)
                        self.print_board()
                        game_over, result = self.game.check_game_over()
                        player = not player
            
                    else:
                    # computer's turn
                        column = self.game.get_computer_move()
                        self.game.computer_move(column)
                        self.print_board()
                        game_over, result = self.game.check_game_over()
                        player = not player 
                
                    if game_over == True:
                        print(self.message[result])
                        return
                    
                except Exception as text:
                    print(text) 
                    continue
                
        print(result)
'''