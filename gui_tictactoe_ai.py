import tkinter as tk
import time
import random
from minimaxAlgo import main

# game states 
ai = 'AI'
pl1 = ''
pl2 = ''
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
buttons_binding = {}

players = []

alieas = {}
alieas_inv = {}

current_player = ''
game_round = 0

play_with_ai = True

# handling functions
def choose_curr_player(curr_player):
    if curr_player == 'X':
        return 'O'
    else:
        return 'X'

def clear_every_states():
    global board
    global current_player
    global game_round
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    # current_player = choose_curr_player(current_player)
    current_player = 'O'
    game_round = 0
    box_frame.pack()
    print_board()
    play_again_button.pack_forget()
    status_label['text'] = f"{alieas.get(current_player)} ({alieas_inv.get(alieas.get(current_player))}) it's your turn"

    # enabling every buttons
    button1.configure(state='normal')
    button2.configure(state='normal')
    button3.configure(state='normal')
    button4.configure(state='normal')
    button5.configure(state='normal')
    button6.configure(state='normal')
    button7.configure(state='normal')
    button8.configure(state='normal')
    button9.configure(state='normal')
    


def init_names():
    global pl1
    global pl2
    global players
    global alieas
    global alieas_inv
    global current_player
    global buttons_binding
    buttons_binding = {(0,0):button1,(0,1):button2,(0,2):button3,(1,0):button4,(1,1):button5,(1,2):button6,(2,0):button7,(2,1):button8,(2,2):button9}

    pl1 = player1_name.get()
    pl2 = ai
    # pl2 = player2_name.get()
    players = [pl1,pl2]
    alieas = {'O':pl1,'X':pl2}
    alieas_inv = {pl1:'O',pl2:'X'}

    # if random.randint(0,1):
    #     players.reverse()
    current_player = alieas_inv.get(players[0])

    top_frame.destroy()
    # print(pl1,pl2)
    box_frame.pack()
    status_label['text'] = f"{alieas.get(current_player)} ({alieas_inv.get(alieas.get(current_player))}) it's your turn"
    status_label.pack()

def mark(position,button):
    # print(position)
    global board
    global current_player
    global game_round
    try:
        board[position[0]][position[1]] = current_player
    except:
        pass
    print_board()
    if check_win(board,alieas.get(current_player),game_round) == None:
        game_round+=1
        #cahnging the current player for the next round
        current_player = choose_curr_player(current_player)
        status_label['text'] = f"{alieas.get(current_player)} ({alieas_inv.get(alieas.get(current_player))}) it's your turn"
        if current_player == alieas_inv.get(ai):
            ai_mark(board)
        # print_board()
    elif check_win(board,alieas.get(current_player),game_round) == True:
        # box_frame.pack_forget()
        status_label['text'] = f"{alieas.get(current_player)} is the Winner!!!"
        # give a option to play again
        play_again_button.pack()
    else:
        # box_frame.pack_forget()
        status_label['text'] = "It's a Draw!!!"
        # give a option to play again
        play_again_button.pack()
        
    button.configure(state='disabled')

def ai_mark(board):
    global buttons_binding
    bestmove = main(board,' ','X','O')
    # print(bestmove)
    mark(bestmove,buttons_binding.get(tuple(bestmove)))


def print_board():
    global board
    button1['text'] = board[0][0]
    button2['text'] = board[0][1] 
    button3['text'] = board[0][2]
    button4['text'] = board[1][0]
    button5['text'] = board[1][1]
    button6['text'] = board[1][2]
    button7['text'] = board[2][0]
    button8['text'] = board[2][1]
    button9['text'] = board[2][2]

def check_win(board,curr_player,game_round):
    flag = False
    for i in range(3):
        #row
        if(board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' '):
            flag = True
        #col
        elif(board[0][i]== board[1][i] == board[2][i] and board[0][i] != ' '):
            flag = True

    #diagonal
    if(board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ' or board[0][2] == board[1][1] == board[2][0]  and board[0][2] != ' ' ):
        flag = True
    if(flag):
        # print(f"======== {curr_player.upper()} is the winner ========")
        return True
    #draw
    if(game_round==8 and not flag):
        # print("==============   IT'S A DRAW   ==============")
        return False
    return None



# GUI
root = tk.Tk()
root.minsize(300,400)

top_frame = tk.Frame(root)
label_for_player1_name = tk.Label(top_frame,text='Enter Your Name')
label_for_player1_name.pack()
player1_name = tk.Entry(top_frame)
player1_name.pack()
# player2_name = tk.Entry(top_frame)
# player2_name.pack()
tk.Button(top_frame,text='Submit',command=init_names).pack()

label_frame = tk.Frame(root)

status_label = tk.Label(label_frame,text='',font=("Bold", 12))
# status_label.pack()
play_again_button= tk.Button(root,text='Play Again',command=clear_every_states)

box_frame = tk.Frame(root)

button1 = tk.Button(box_frame,text='',height=3,width=4,border=2,command= lambda : mark([0,0],button1)) # 0,0
button2 = tk.Button(box_frame,text='',height=3,width=4,border=2,command= lambda : mark([0,1],button2)) # 0,1
button3 = tk.Button(box_frame,text='',height=3,width=4,border=2,command= lambda : mark([0,2],button3)) # 0,2
button4 = tk.Button(box_frame,text='',height=3,width=4,border=2,command= lambda : mark([1,0],button4)) # 1,0
button5 = tk.Button(box_frame,text='',height=3,width=4,border=2,command= lambda : mark([1,1],button5)) # 1,1
button6 = tk.Button(box_frame,text='',height=3,width=4,border=2,command= lambda : mark([1,2],button6)) # 1,2
button7 = tk.Button(box_frame,text='',height=3,width=4,border=2,command= lambda : mark([2,0],button7)) # 2,0
button8 = tk.Button(box_frame,text='',height=3,width=4,border=2,command= lambda : mark([2,1],button8)) # 2,1
button9 = tk.Button(box_frame,text='',height=3,width=4,border=2,command= lambda : mark([2,2],button9)) # 2,2
button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)

label_frame.pack()
top_frame.pack(pady=20)
# box_frame.pack(padx=10,pady=20)
root.mainloop()
