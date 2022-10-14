"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCounter = 0
    oCounter = 0

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                xCounter += 1
            elif board[i][j] == O:
                oCounter += 1

    if xCounter > oCounter:
        return O
    else:
        return X


def actions(board):
    # """
    # Returns set of all possible actions (i, j) available on the board.
    # """
    # raise NotImplementedError
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    # if action not in actions(board):
    #     raise Exception("Invalid Action!!!")
    
    board2 = copy.deepcopy(board)
    # print(player(board))
    board2[action[0]][action[1]] = player(board)

    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None 
            
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    # for i in range(3):
    #     for j in range(3):
    #         if board[i][j]==EMPTY:
    #             return False
    # return True
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError
    if terminal(board):
        return None
    elif player(board)==X:
        value,move =  MaxFunc(board)
        return move
    elif player(board)==O:
        value,move =  MinFunc(board)
        return move

def MaxFunc(board):
    if terminal(board):
        return utility(board),None
    ans = -2
    move = None
    for action in actions(board):
       

        val,mov = MinFunc(result(board,action))
        if val>ans:
            ans = val
            move = action

       
        

    return ans,move
        

    

def MinFunc (board):           
    if terminal(board):
        return utility(board),None
    ans = 2
    move = None
    for action in actions(board):
        board[action[0]][action[1]] = player(board)

        val,mov = MaxFunc(board)
        if val<ans:
            ans = val
            move = action 

        board[action[0]][action[1]] = EMPTY
        if val == -1:
            return val,action

    return ans,move
#returns of our final result
