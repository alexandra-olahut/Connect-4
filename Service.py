import random

class Game:
    
    def __init__(self, board, algorithm):
        self.board = board
        self.algorithm = algorithm

    def get_board(self):
        # getter for the board
        return self.board.get_board()
    
    def get_open_spot(self, column):
        '''
        Function that finds the first empty spot on given column
        '''
        return self.board.get_next_open_line(column)
    
    def reset(self):
        # resets the game
        self.board.reset()
    
    
    def player_move(self, column):
        '''
        Function that drops a piece for the player on the given column
        '''
        self.board.move(column, -1)
    
    def computer_move(self, column):
        '''
        Function that drops a piece for the computer on the column chosen using the algorithm
        '''
        self.board.move(column, 1)
        
    def get_computer_move(self):
        return self.algorithm.next_move(self.board)
        
    def check_game_over(self):
        '''
        Function that checks when the game is over
        Returns: False - if the game is on
                 True - if th game is over; with 1 - if the computer won
                                                -1 - if the player won
                                                 0 - if it is a tie
        '''
        return self.board.check_game_over()

class Algorithm_random:
    
    def next_move(self, board):
        '''
        Function that chooses a random column from those available and returns it for the computer move
        '''
        valid_columns = board.get_valid_columns()
        column = random.choice(valid_columns)
        return column

class Algorithm:
    
    def next_move(self, board):
        '''
        Function that finds the best move for the computer using the minimax algorithm and a scoring system
        Returns the column corresponding to that move
        Params:board - the current state of the game
        '''
        best_score = -1000000
        score = 0
        move = random.randint(0,6)
        for column in range(7):
            if board.column_is_valid(column): 
                line = board.get_next_open_line(column)
                board.set(line, column, 1)
                #score = board.score_board()
                score = self.minimax(board, 3, False)
                board.set(line, column, 0)
                if score>best_score:
                    best_score = score
                    move = column
        return move
    
    def minimax(self, board, depth, is_maximizing):
        '''
        Algorithm that finds the best move by generating the next possible moves and calculating the score for each of them
        - it is a recursive function
        Returns - best score that can be obtained
        
        Params: - board: current state of the board
                - depth: the number of steps remained to be performed (the number of levels left to be generated for the tree)
                - is_maximizing: boolean variable - True: if we calculate the best score for the maximizing player
                                                  - False: -||- for minimizing player
        '''
        if is_maximizing:
            player = 1
        else:
            player = -1
        game_over, result = board.check_game_over()
        if game_over == True or depth == 0:
            return board.score_board()
        
        if is_maximizing:
            best_score = -100000000
            for column in range(7):
                if board.column_is_valid(column):
                    line = board.get_next_open_line(column)
                    board.set(line, column, 1)
                    score = self.minimax(board, depth-1, False)
                    board.set(line, column, 0)
                    best_score = max(score, best_score)
            return best_score
        
        else:
            best_score = 100000000
            for column in range(7):
                if board.column_is_valid(column):
                    line = board.get_next_open_line(column)
                    board.set(line, column, -1)
                    score = self.minimax(board, depth-1, True)
                    board.set(line, column, 0)
                    best_score = min(score, best_score)
            return best_score
        
