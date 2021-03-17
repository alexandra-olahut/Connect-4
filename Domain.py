class Board:
    def __init__(self):
        #initialize board as matrix of zeros
        self.board = [[0]*7, [0]*7, [0]*7, [0]*7, [0]*7, [0]*7]
        self.moves = 0
        self.line_count = 6
        self.column_count = 7
        
    def get_board(self):
        return self.board
    
    '''
    Getter and setter for elements of the board, given by line and column
    '''
    def get(self, line,column):
        return self.board[line][column]
    def set(self, line,column, value):
        self.board[line][column] = value
    
    def __str__(self):
        for line in self.board:
            print(line)
        
    def reset(self):
        '''
        Function that clears the board, initializing it with zeros
        '''
        for line in range(self.line_count):
            for column in range(self.column_count):
                self.board[line][column] = 0
        self.moves = 0
        
    
    def get_valid_columns(self):
        '''
        Function that returns all the columns which are not full yet
        '''
        valid_columns = []
        for column in range(self.column_count):
            if self.column_is_valid(column):
                valid_columns.append(column)
        return valid_columns
    
    def column_is_valid(self, column):
        '''
        Function that checks if a column is valid (is not full)
        '''
        for line in range(self.line_count):
            if self.board[line][column] == 0:
                return True 
        return False
            
    
    def get_next_open_line(self, column):
        '''
        Function that finds the first empty spot on given column
        (considering from bottom to the top)
        Returns: the line found
        '''
        for line in range(self.line_count-1,-1,-1):
            # it checks from bottom to the top 
            if self.board[line][column] == 0:
                return line
        raise Exception('Column is full')
        
    def move(self, column, player):
        '''
        Function that drops a new piece
        Params: - column: on which the new piece is dropped
                - player: whose piece is dropped
        '''
        line = self.get_next_open_line(column)
        self.board[line][column] = player
        self.moves +=1
        
        
    def check_game_over(self):
        '''
        Function that checks if the game is over and returns the result
        Returns: True - if game is finished; 0 - if the board is full but there is no winner
                                             1/-1 - if there is a winner
                    
                 False - if game is still on
        '''
        if self.winner() == None:
            if self.moves == self.line_count * self.column_count:
                return True, 0
            else:
                return False, ''
        else:
            return True, self.winner()
            
    
    def check_winner(self, sum_):
        '''
        Function that returns the winner, if there is a winner
        Returns: 1 - if the computer wins
                -1 - if the player wins
        '''
        if sum_ == 4:
            return 1
        if sum_ == -4:
            return -1
    
    def winner(self):
        '''
        Function that checks if the game was won
        Returns: 1 - if the computer wins
                -1 - if the player wins
                None - if the game is not won
        '''
        board = self.board 
        # check lines
        for line in range(self.line_count):
            for column in range(self.column_count-3):
                sum_ = board[line][column]+board[line][column+1]+board[line][column+2]+board[line][column+3] 
                if self.check_winner(sum_) != None:
                    return self.check_winner(sum_)
                
        # check columns
        for column in range(self.column_count):
            for line in range(self.line_count-3):
                sum_ = board[line][column]+ board[line+1][column]+ board[line+2][column]+ board[line+3][column]
                if self.check_winner(sum_) != None:
                    return self.check_winner(sum_)
                
        # check positive slopes
        for line in range(5,2,-1):
            for column in range(0,4):
                sum_ = board[line][column]+board[line-1][column+1]+board[line-2][column+2]+board[line-3][column+3]
                if self.check_winner(sum_) != None:
                    return self.check_winner(sum_)
                            
        # check negative slopes
        for line in range(5,2,-1):
            for column in range(3,7):
                sum_ = board[line][column]+board[line-1][column-1]+board[line-2][column-2]+board[line-3][column-3]
                if self.check_winner(sum_) != None:
                    return self.check_winner(sum_)
                
                
    
    
    def evaluate_section(self, section, player):
        # player = 1 is the computer
        # player = -1 is the human
        empty = 0
        opponent = 1
        if player == 1:
            opponent = -1
        score = 0
        
        if section.count(player) == 4:
            score += 1000000
        elif section.count(player) == 3 and section.count(empty) == 1:
            score += 50
        elif section.count(player) == 2 and section.count(empty) == 2:
            score += 10
            
        if section.count(opponent) == 4:
            score -= 500    
        elif section.count(opponent) == 3 and section.count(empty) == 1:
            score -= 80
        elif section.count(opponent) == 2 and section.count(empty) == 2:
            score -= 30
    
        return score
        
    def score_board(self):
        '''
        Function that calculates the score for the current state of the board
            - higher score means favorable for the computer
            - lower score means favorable for the player
          *points are arbitrary chosen
        '''
        score = 0
        # score horizontal
        for line in range(self.line_count):
            line_array = self.board[line]
            for column in range(self.column_count-3):
                section = line_array[column:column+4]
                score += self.evaluate_section(section, 1)
                score -= self.evaluate_section(section, -1)
        
        # score vertical
        for column in range(self.column_count):
            column_array = [self.board[line][column] for line in range(self.line_count)]
            for line in range(self.line_count-3):
                section = column_array[line:line+4]
                score += self.evaluate_section(section, 1)
                score -= self.evaluate_section(section, -1)
                
        # score positive slopes
        for line in range(self.line_count-3):
            for column in range(self.column_count-3):
                section = [self.board[line+i][column+i] for i in range(4)]
                score += self.evaluate_section(section, 1)
                score -= self.evaluate_section(section, -1)
                
        # score negative slopes
        for line in range(self.line_count-3):
            for column in range(self.column_count-3):
                section = [self.board[line+3-i][column+i] for i in range(4)]
                score += self.evaluate_section(section, 1)
                score -= self.evaluate_section(section, -1)
                
        return score