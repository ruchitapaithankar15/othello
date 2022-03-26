import math
import random
from copy import deepcopy
import sys

EMPTY = 2
PLAYER1 = 0
PLAYER2 = 1
PLAYER_NAMES = ["O", "X", "."]
OTHER_PLAYER = {PLAYER1:PLAYER2, PLAYER2:PLAYER1}



class Player:

    def choose_move(self, state):
        raise NotImplementedError


class Game:

    def __init__(self, initial_state, player1, player2):
        self.initial_state = initial_state
        self.players = [player1, player2]

    def play(self):
        state = self.initial_state.clone()
        states = [state]
        player_index = 0
        while not state.game_over():
            # Display the current state in the console:
            print("\nCurrent state, " + PLAYER_NAMES[state.nextPlayerToMove] + " to move:")
            print(state)
            # Get the move from the player:
            player = self.players[player_index]
            move = player.choose_move(state)
            if move != None: print(move)
            state = state.applyMoveCloning(move)
            states.append(state)
            # util.pprint(state)
            player_index = (player_index + 1) % len(self.players)
        
        print("\n*** Final winner: " + state.winner() +" ***" )
        print(state)
        return states
class rhp44(Player):

    def __init__(self, tm):
        super().__init__()
        self.time = tm
        self.alpha_beta = False

    def choose_move(self, state):
        # generate the list of moves:
        moves = state.generateMoves()
        # If there's more than 12 seconds left, use ply 4
        if self.time > 12.0:
            return self.get_move_minmax(state, 4)[1]

        # If there's more than 1 seconds left, use ply 3
        elif self.time > 1.0:
            return self.get_move_minmax(state, 3)[1]

        # Otherwise, pick a random move
        else:

            return random.choice(moves)

    def get_move_minmax(self, state, depth):
        moves = state.generateMoves()

        if not moves:
            return (state.score(),)

        if depth == 0:
            return (state.score(),)
        best_score = -99999
        best_move = None
        for move in moves:
            newstate = deepcopy(state)
            newstate.applyMoveCloning(move)
            res = self.get_move_minmax(newstate, depth - 1)
            if -res[0] > best_score:
                best_move = move
                best_score = res[0]

        return (best_score, best_move)



#### AGENTS  ####
class HumanPlayer(Player):

    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        # generate the list of moves:
        moves = state.generateMoves()
        if not moves:
            return None
        move = ''
        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
        
        while not move:
            response = input('Please choose a move: ')
            try:
                move = moves[int(response)]
            except:
                print('invalid move choice')
        return move

class RandomAgent(Player):
    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        # generate the list of moves:
        moves = state.generateMoves()
        return random.choice(moves)


class MinimaxAgent(Player):
    def __init__(self,depth):
        super().__init__()
        self.depth = depth
    
    
    def get_move_minmax(self,state,depth):
        moves = state.generateMoves()
        
        
        if not moves:
            return (state.score(),)
        
        if depth == 0:
            return (state.score(),)
        best_score = -99999
        best_move=None
        for move in moves:
            newstate= deepcopy(state)
            newstate.applyMoveCloning(move)
            res = self.get_move_minmax(newstate,depth-1)
            if -res[0] > best_score:
                best_move = move
                best_score = res[0]
        
        return (best_score,best_move)

    def choose_move(self, state):
        # generate the list of moves:
        result = self.get_move_minmax(state,self.depth)
        print('result: ',result)
        return result[1]
        


class AlphaBeta(Player):
    def __init__(self,depth):
        super().__init__()
        self.depth = depth


    def get_move_alpha(self,state,depth,myscore,oppscore):
        moves = state.generateMoves()
        
        
        if not moves:
            return (state.score(),)
        
        if depth == 0:
            return (state.score(),)
        best_score = myscore
        best_move=None
        for move in moves:
            newstate= deepcopy(state)
            newstate.applyMoveCloning(move)
            res = self.get_move_alpha(newstate,depth-1,-oppscore,-best_score)
            if res[0] > best_score:
                best_move = move
                best_score = res[0]
            if best_score > oppscore:
                return(best_score,best_move)
        
        return (best_score,best_move)

    def choose_move(self, state):
        # generate the list of moves:
        result = self.get_move_alpha(state,self.depth,-10000,10000)
        
        return result[1]
def get_arg(index, default=None):
    '''Returns the command-line argument, or the default if not provided'''
    return sys.argv[index] if len(sys.argv) > index else default


class State:
    def __init__(self, board=None, boardSize=8, nextPlayerToMove=PLAYER1):

        if board:
            self.board = board
            self.boardSize = boardSize
            self.nextPlayerToMove = nextPlayerToMove

        # This will creates a board with the initial state for the game of Othello
        else:
            self.boardSize = boardSize
            if boardSize < 2:
                self.boardSize = 2
            self.nextPlayerToMove = nextPlayerToMove

            self.board = [[EMPTY] * boardSize for y in range(boardSize)]
            #  initial position:
            self.board[boardSize // 2 - 1][boardSize // 2 - 1] = PLAYER1
            self.board[boardSize // 2][boardSize // 2] = PLAYER1
            self.board[boardSize // 2 - 1][boardSize // 2] = PLAYER2
            self.board[boardSize // 2][boardSize // 2 - 1] = PLAYER2

    # Converts a game board to a string, for displaying it via the console
    def __str__(self):
        output = ""
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                output += PLAYER_NAMES[self.board[i][j]] + " "
            output += "\n"
        return output

    def __eq__(self, state):
        return self.board == state.board

    def clone(self):
        return State(deepcopy(self.board), self.boardSize, self.nextPlayerToMove)

    def is_legal(self, x, y):
        return x >= 0 and x < self.boardSize and y >= 0 and y < self.boardSize

    def get(self, x, y):
        return self.board[y][x] if self.is_legal(x, y) else None

    def row(self, y):
        return self.board[y]

    def num_empties(self):
        return sum(r.count(EMPTY) for r in self.board)

    def equals(self, state):
        return self.board == state.board

    # Determines whether the game is over or not
    def game_over(self):
        return len(self.generateMoves(PLAYER1)) == 0 and len(self.generateMoves(PLAYER2)) == 0

    # Returns the final score, once a game is over
    def score(self):
        score = 0
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j] == PLAYER1:
                    score += 1
                if self.board[i][j] == PLAYER2:
                    score -= 1
        return score

    #  Returns the list of possible moves for player 'player'
    def generateMoves(self, player=None):

        if not player:
            player = self.nextPlayerToMove
        moves = []

        # these two arrays encode the 8 posible directions in which a player can capture pieces:
        offs_x = [0, 1, 1, 1, 0, -1, -1, -1]
        offs_y = [-1, -1, 0, 1, 1, 1, 0, -1]

        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j] == EMPTY:
                    moveFound = False
                    for k in range(len(offs_x)):
                        if not moveFound:
                            current_x = i + offs_x[k]
                            current_y = j + offs_y[k]
                            while (current_x + offs_x[k] >= 0 and current_x + offs_x[k] < self.boardSize and
                                   current_y + offs_y[k] >= 0 and current_y + offs_y[k] < self.boardSize and
                                   self.board[current_x][current_y] == OTHER_PLAYER[player]):
                                current_x += offs_x[k]
                                current_y += offs_y[k]
                                if self.board[current_x][current_y] == player:
                                    #  Legal move:
                                    moveFound = True
                                    moves.append(OthelloMove(player, i, j))
        return moves

    # Modifies the game state as for applying the given 'move'
    # Notice that move can be "null", which means that the player passes.
    # "passing" is only allowed if a player has no other moves available.
    def applyMove(self, move):

        if move == None:
            print("\nPlayer " + PLAYER_NAMES[self.nextPlayerToMove] + " passes the move!")
            self.nextPlayerToMove = OTHER_PLAYER[self.nextPlayerToMove]
            return  # player passes

        self.nextPlayerToMove = OTHER_PLAYER[self.nextPlayerToMove]

        # set the piece:
        self.board[move.x][move.y] = move.player

        # these two arrays encode the 8 posible directions in which a player can capture pieces:
        offs_x = [0, 1, 1, 1, 0, -1, -1, -1]
        offs_y = [-1, -1, 0, 1, 1, 1, 0, -1]

        # see if any pieces are captured:
        for i in range(len(offs_x)):
            current_x = move.x + offs_x[i]
            current_y = move.y + offs_y[i]
            while (current_x + offs_x[i] >= 0 and current_x + offs_x[i] < self.boardSize and
                   current_y + offs_y[i] >= 0 and current_y + offs_y[i] < self.boardSize and
                   self.board[current_x][current_y] == OTHER_PLAYER[move.player]):
                current_x += offs_x[i]
                current_y += offs_y[i]
                if self.board[current_x][current_y] == move.player:
                    # pieces captured!:
                    reversed_x = move.x + offs_x[i]
                    reversed_y = move.y + offs_y[i]
                    while reversed_x != current_x or reversed_y != current_y:
                        self.board[reversed_x][reversed_y] = move.player
                        reversed_x += offs_x[i]
                        reversed_y += offs_y[i]
                    break

    # Creates a new game state that has the result of applying move 'move'
    def applyMoveCloning(self, move):
        newState = self.clone()
        newState.applyMove(move)
        return newState

    def winner(self):
        if self.score() > 0:
            return PLAYER_NAMES[PLAYER1]
        elif self.score() < 0:
            return PLAYER_NAMES[PLAYER2]
        else:
            return "DRAW"


def create_player(arg,  depht_or_time):
    if arg == 'human':
        return HumanPlayer()
    elif arg == 'random':
        return RandomAgent()
    elif arg == 'minimax':
        return MinimaxAgent(depht_or_time)
    elif arg == 'alphabeta':
        return AlphaBeta(depht_or_time)
    elif arg == 'extra':
        return rhp44(depht_or_time)
    else:
        return RandomAgent()




class OthelloMove:
    def __init__(self, player, x, y):
        self.player = player
        self.x = x
        self.y = y

    def __str__(self):
        return "Player " + PLAYER_NAMES[self.player] + " to " + str(self.x) + "," + str(self.y)
if __name__ == '__main__':

    initial_state = State()
    if len(sys.argv) > 1:
        agent1 = sys.argv[1]
        agent2 = sys.argv[2]
        depth_or_time = 3
    if len(sys.argv) == 4 : 
        depth_or_time = int(sys.argv[3])


    player1 = create_player(get_arg(1), depth_or_time)
    player2 = create_player(get_arg(2), depth_or_time)

    
    game = Game(initial_state, player1, player2)

    game.play()

    
