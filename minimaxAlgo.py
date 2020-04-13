# c defines the not initialize state of every cell of the board
c = None
def isMovesLeft(board):
    # print("nice")
    for i in range(3):
        for j in range(3):
            if board[i][j] == c:
                return True
    return False

def check_win(board):
    # row
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != c:
            if board[i][0] == player:
                return +10
            elif board[i][0] == opponent:
                return -10
    
    # col
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != c:
            if board[0][i] == player:
                return +10
            elif board[0][i] == opponent:
                return -10
    
    # diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != c:
        if board[0][0] == player:
            return +10
        elif board[0][0] == opponent:
            return -10
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != c:
        if board[0][2] == player:
            return +10
        elif board[0][2] == opponent:
            return -10
    
    return 0

def minimax(board,depth,isMaximizing):
    score = check_win(board)

    if score == 10:
        # print("score is 10")
        return score
    if score == -10:
        # print("Score is -10")
        return score
    
    if isMovesLeft(board) == False:
        # print("Score is 0")
        return 0
    if isMaximizing:
        maxEval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == c:
                    board[i][j] = player
                    tempScore = minimax(board,depth+1, not isMaximizing)
                    maxEval = max(maxEval, tempScore)
                    board[i][j] = c
        return maxEval
    else:
        minEval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == c:
                    board[i][j] = opponent
                    tempScore = minimax(board,depth+1, not isMaximizing)
                    board[i][j] = c
                    minEval = min(minEval,tempScore)
        return minEval

def findBestMove(board):
    bestMove = []
    bestScore = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == c:
                board[i][j] = player
                score = minimax(board,0,False)
                board[i][j] = c
                if score > bestScore:
                    bestScore = score
                    bestMove = [i,j]
    # print("Value of best move is :",bestScore)
    return bestMove

def main(board,non_char,current_player,opponent_player):
    global player
    player = current_player
    global opponent
    opponent = opponent_player
    global c
    c = non_char
    # print(board)

    return findBestMove(board)

if __name__ == "__main__":
    c=None
    board = [
        ['O',c,c],
        [c,c,c],
        [c,c,c]
    ]
    player = 'X'
    opponent = 'O'
    print(isMovesLeft(board))
    # print(check_win(board))

    print(findBestMove(board))

