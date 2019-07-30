'''
Name : Hugo Ruiz Villar & lanxiang Yang
NetID: hruizvil & lanxiany
IDs #: 66212078 & 63972549

    This is a unit test module, it is a class made
    to test components of the Connect Four module.
    
'''
import unittest
import connect_four

class test_board(unittest.TestCase):
    
    def setUp(self):
        ''' 
        This method will be called automatically for every single test run, in order
        to avoid repetition (DRY). 
        '''
        self.game = connect_four.Board()
        self.board = self.game.board
        
    def test_type(self):
        '''
        This method tests whether the object instantiated named 'game', 
        is the correct instance of the class Board.
        '''
        self.assertIsInstance(self.game, connect_four.Board) 
        
    def test_is_player_switched(self):
        '''
        This method tests if the method whose_turn_is_it() changes the players
        from player 1 to player 2
        '''
        self.game.whose_turn_is_it()
        self.assertEqual(self.game.current_player, 2)
        
    def test_chip_placement(self):
        '''
        This method tests if a 'R' chip or 'Y' chip is place in the correct slot when 
        a player makes a move
        '''
        self.game.make_move(1,1)    # @params - current_player, column_number
        self.assertEqual(self.board[6][0], 'R')
        self.game.whose_turn_is_it()
        self.game.make_move(2, 2)
        self.assertEqual(self.board[6][1], 'Y')
        
    def test_invalid_input(self):
        '''
        This method tests if the make_move function raises an error whenever 
        something that is not a number is entered to the console.
        '''
        self.assertRaises(TypeError, self.game.make_move, 1, 'a')
        self.assertRaises(TypeError, self.game.make_move, 1, ' ')
        self.assertRaises(TypeError, self.game.make_move, 1, '!')
        self.assertRaises(TypeError, self.game.make_move, 1, 2)
        
    def test_input_out_of_range(self):
        '''
        Tests if make_move raises an Index Error when a player tries
        to make a move that is not within the 7 columns allowed
        '''
        self.assertRaises(IndexError, self.game.make_move, 1, 9)
        self.assertRaises(IndexError, self.game.make_move, 1, 0)
        
#    For the following tests:
#        1) test_is_draw
#        2) test_is_horizontal_win
#        3) test_is_vertical_win
#        4) test_is_diagonal_win
#        5) test_is_game_over
#         
#        A tuple is used by the connect four module, and will return three elements
#        in order to analyze whether: 
#        ..The game is over 
#        ...the game ends in a draw 
#        ....and who the winner is (if there is one)
        
#        In the following format -> (True, True, 0) # This shows that the game is over, 
#                                                     it was a draw, and no player won

    def test_is_draw(self):
        '''
        This method tests if 2 players are able to end up in a tie.
        I.e, a game where no player wins and the game concludes.
        '''
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['Y', 'R', 'Y', 'R', 'R', 'Y', 'R'], 
                           ['R', 'Y', 'R', 'Y', 'Y', 'Y', 'R'], 
                           ['Y', 'R', 'R', 'Y', 'R', 'Y', 'R'], 
                           ['Y', 'R', 'Y', 'R', 'Y', 'R', 'Y'],
                           ['R', 'R', 'R', 'Y', 'Y', 'R', 'Y'],
                           ['R', 'Y', 'Y', 'R', 'R', 'R', 'Y']]
        
        # is_game_over() will return (True, True, 0) only if both players run out of moves
        self.assertEqual(self.game.is_game_over(), (True, True, 0))
    
    def test_is_horizontal_win(self):
        '''
        This method tests whether a player wins when the player has made
        a horizontal winning sequence of 4 chips, either 'Y' or 'R'.
        '''
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['R', 'R', 'R', 'R', '.', '.', '.']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a horizontal sequence
        self.assertEqual(self.game.is_game_over(),(True, False, 1))
        
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', 'Y', 'Y', 'Y', 'Y']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a horizontal sequence
        self.assertEqual(self.game.is_game_over(),(True, False, 2))
            
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', 'R', 'R', 'R', 'R'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a horizontal sequence
        self.assertEqual(self.game.is_game_over(),(True, False, 1))
        
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['Y', 'Y', 'Y', 'Y', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a horizontal sequence
        self.assertEqual(self.game.is_game_over(),(True, False, 2))
        
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['R', 'R', 'R', 'R', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a horizontal sequence
        self.assertEqual(self.game.is_game_over(),(True, False, 1))
        
        
    
    def test_is_vertical_win(self):
        '''
        This method tests whether a player wins when the player has made
        a vertical winning sequence of 4 chips, either 'Y' or 'R'.
        '''
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['R', '.', '.', '.', '.', '.', '.'], 
                           ['R', '.', '.', '.', '.', '.', '.'],
                           ['R', '.', '.', '.', '.', '.', '.'],
                           ['R', '.', '.', '.', '.', '.', '.']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a vertical sequence
        self.assertEqual(self.game.is_game_over(),(True, False, 1))
        
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['Y', '.', '.', '.', '.', '.', '.'], 
                           ['Y', '.', '.', '.', '.', '.', '.'], 
                           ['Y', '.', '.', '.', '.', '.', '.'], 
                           ['Y', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a vertical sequence
        self.assertEqual(self.game.is_game_over(),(True, False, 2))
        
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', '.', '.', '.', 'R'], 
                           ['.', '.', '.', '.', '.', '.', 'R'], 
                           ['.', '.', '.', '.', '.', '.', 'R'], 
                           ['.', '.', '.', '.', '.', '.', 'R'],
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a vertical sequence
        self.assertEqual(self.game.is_game_over(),(True, False, 1))
        
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', 'Y'], 
                           ['.', '.', '.', '.', '.', '.', 'Y'],
                           ['.', '.', '.', '.', '.', '.', 'Y'],
                           ['.', '.', '.', '.', '.', '.', 'Y']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a vertical sequence
        self.assertEqual(self.game.is_game_over(),(True, False, 2))
        
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', 'R', '.', '.', '.', '.', '.'], 
                           ['.', 'R', '.', '.', '.', '.', '.'],
                           ['.', 'R', '.', '.', '.', '.', '.'],
                           ['.', 'R', '.', '.', '.', '.', '.']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a vertical sequence
        self.assertEqual(self.game.is_game_over(),(True, False, 1))
        
    def test_is_diagonal_win(self):
        '''
        This method tests whether a player wins when the player has made
        a diagonal winning sequence of 4 chips, either 'Y' or 'R'.
        '''
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['R', '.', '.', '.', '.', '.', '.'], 
                           ['.', 'R', '.', '.', '.', '.', '.'],
                           ['.', '.', 'R', '.', '.', '.', '.'],
                           ['.', '.', '.', 'R', '.', '.', '.']]
    
        # is_game_over() will return (True, False, 1) if a player wins with a diagonal sequence
        self.assertEqual(self.game.is_game_over(), (True, False, 1))
        
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', '.', '.', '.', '.', '.', 'Y'], 
                           ['.', '.', '.', '.', '.', 'Y', '.'],
                           ['.', '.', '.', '.', 'Y', '.', '.'],
                           ['.', '.', '.', 'Y', '.', '.', '.']]
    
        # is_game_over() will return (True, False, 1) if a player wins with a diagonal sequence
        self.assertEqual(self.game.is_game_over(), (True, False, 2))
        
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', 'R', '.', '.', '.'], 
                           ['.', '.', '.', '.', 'R', '.', '.'], 
                           ['.', '.', '.', '.', '.', 'R', '.'], 
                           ['.', '.', '.', '.', '.', '.', 'R'],
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a diagonal sequence
        self.assertEqual(self.game.is_game_over(), (True, False, 1))
        
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', 'Y', '.', '.', '.'], 
                           ['.', '.', 'Y', '.', '.', '.', '.'], 
                           ['.', 'Y', '.', '.', '.', '.', '.'], 
                           ['Y', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.']]
        
        # is_game_over() will return (True, False, 1) if a player wins with a diagonal sequence
        self.assertEqual(self.game.is_game_over(), (True, False, 2))

    
    def test_is_game_over(self):
        '''
        This method tests whether a player wins when the player has made
        enough moves to obtain a winning sequence of 4 chips in any horizontal, 
        vertically or diagonal scenario.
        '''
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['.', '.', '.', '.', '.', '.', '.'], 
                           ['.', 'Y', '.', '.', '.', '.', '.'], 
                           ['R', 'R', '.', '.', '.', '.', '.'], 
                           ['Y', 'R', 'Y', '.', '.', '.', '.'],
                           ['Y', 'R', 'R', 'Y', 'Y', '.', '.'],
                           ['R', 'Y', 'R', 'R', 'R', 'Y', '.']]
        
        # Checks if the element within the tuple in game_is_over is True, i.e., the game is over.
        self.assertTrue(self.game.is_game_over()[0])  
    
    def test_column_full(self):
        '''
        This method tests whether a chip can be placed in a full column.
        '''
        self.game.board = [['1', '2', '3', '4', '5', '6', '7'], 
                           ['Y', '.', '.', '.', '.', '.', '.'], 
                           ['R', '.', '.', '.', '.', '.', '.'], 
                           ['Y', '.', '.', '.', '.', '.', '.'], 
                           ['R', '.', '.', '.', '.', '.', '.'],
                           ['Y', '.', '.', '.', '.', '.', '.'],
                           ['R', '.', '.', '.', '.', '.', '.']]
        
        # Checks if make_move returns False when a player attempts to place a chip in a full column
        # I.e., False would mean the move is not permitted.
        self.assertFalse(self.game.make_move(1, 1))
        
if __name__ == '__main__':
    unittest.main()
