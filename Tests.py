
import unittest
from Domain import Board
from Service import Algorithm, Game


class TestDomain(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def testGet_LineColumn_returnElement(self):
        board = Board()
        self.assertEqual(board.get(0,0),0)
    
    def testSet_LineColumnValue_ElementIsSet(self):
        board = Board()
        board.set(1, 1, 1)
        self.assertEqual(board.get(1,1),1)

    def testReset_self_boardCleared(self):
        board = Board()
        board.set(1,1,1)
        board.reset()
        for line in range(board.line_count):
            for column in range(board.column_count):
                self.assertEqual(board.get(line,column),0)

    def testGetValidColumns_self_validColumns(self):
        board = Board()
        for column in range(3):
            for line in range(board.line_count):
                board.set(line,column,1)
        self.assertEqual(board.get_valid_columns(), [3,4,5,6])

    def testColumnIsValid_validColumn_True(self):
        board = Board()
        board.set(0,0,1)
        self.assertTrue(board.column_is_valid(0))
    def testColumnIsValid_invalidColumn_False(self):
        board = Board()
        for line in range(board.line_count):
            board.set(line,0,1)
        self.assertFalse(board.column_is_valid(0))

    def test_getOpenLine_column_nextOpenLine(self):
        board = Board()
        board.set(5,0,1)
        board.set(4,0,1)
        self.assertEqual(board.get_next_open_line(0), 3)
        
    def testMove_columnANDvalue_moveIsMade(self):
        board = Board()
        board.set(5,0,1)
        board.set(4,0,1)
        board.move(0,1)
        self.assertEqual(board.get(3,0), 1)
        
        
    def testCheckWinner_4_computerWins(self):
        board = Board()
        self.assertEqual(board.check_winner(4), 1)
    def testCheckWinner_minus4_playerWins(self):
        board = Board()
        self.assertEqual(board.check_winner(-4), -1)
        
    def testWinner_computerWonVertical_1(self):
        board = Board()
        for line in range(4):
            board.set(line,0,1)
        self.assertEqual(board.winner(), 1)
    def testWinner_computerWonHorizontal_1(self):
        board = Board()
        for column in range(4):
            board.set(0,column,1)
        self.assertEqual(board.winner(), 1)
    def testWinner_computerWonDiagonal_1(self):
        board = Board()
        for line in range(4):
            board.set(line,line,1)
        self.assertEqual(board.winner(), 1)
        
    def testWinner_playerWonVertical_minus1(self):
        board = Board()
        for line in range(4):
            board.set(line,0,-1)
        self.assertEqual(board.winner(), -1)
    def testWinner_playerWonHorizontal_minus1(self):
        board = Board()
        for column in range(4):
            board.set(0,column,-1)
        self.assertEqual(board.winner(), -1)
    def testWinner_playerWonDiagonal_minus1(self):
        board = Board()
        for line in range(4):
            board.set(line,line,-1)
        self.assertEqual(board.winner(), -1)
    
    def testWinner_nobodyWon_none(self):
        board = Board()
        self.assertEqual(board.winner(), None)        


    def testGameOver_notOver_False(self):
        board = Board()
        game_over, result = board.check_game_over()
        self.assertFalse(game_over)
    def testGameOver_tie_TrueTie(self):
        board = Board()
        for line in range(board.line_count):
            for column in range(board.column_count):
                board.move(column, 10)
        game_over, result = board.check_game_over()
        self.assertTrue(game_over)
        self.assertEqual(result,0)

    
    def testEvaluateSection_section_score(self):
        board = Board()
        self.assertEqual(board.evaluate_section([1,0,1,1], 1), 50)
        
    def testScoreBoard_board_score(self):
        board = Board()
        board.move(1,-1)
        board.move(1,-1)
        board.move(2,-1)
        board.move(1,1)
        board.move(2,1)
        board.move(3,1)
        
        self.assertEqual(board.score_board(), 130)
        
        
        
class TestAlgorithm(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def testNextMove_board_columnForMove(self):
        board = Board()
        algorithm = Algorithm()
        board.move(3,-1)
        board.move(3,-1)
        board.move(3,-1)
        self.assertEqual(algorithm.next_move(board) , 3)

class TestGame(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def init(self):
        self.board = Board()
        self.algorithm = Algorithm()
        self.game = Game(self.board, self.algorithm)
        
    def testGetOpenSpot_column_line(self):
        self.init()
        self.assertEqual(self.game.get_open_spot(0), 5)
        
    def testReset_self_boardIsReset(self):
        self.init()
        self.game.reset()
        board = self.game.get_board()
        for line in range(6):
            for column in range(7):
                self.assertEqual(board[line][column], 0)
                
    def testPlayerMove_column_moveMade(self):
        self.init()
        self.game.player_move(6)
        board = self.game.get_board()
        self.assertEqual(board[5][6], -1)
        
    def testComputerMove_self_moveMade(self):
        self.init()
        self.game.computer_move(3)
        board = self.game.get_board()
        self.assertEqual(board[5][3], 1)
        
    def testGetComputerMove_self_returnColumn(self):
        self.init()
        self.game.player_move(6)
        self.game.player_move(6)
        self.game.player_move(6)
        self.assertEqual(self.game.get_computer_move(), 6)
        