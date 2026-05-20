from tkinter import *
import random

def turn(row,column):

    global player

    if two_d_list[row][column]['text'] =="" and check_winner()==False:
        if player==symbols[0]:
            two_d_list[row][column]['text']=player
            if check_winner()==False:
                player=symbols[1]
                label.config(text=player+ " TURN")
        elif player==symbols[1]:
             two_d_list[row][column]['text']=player
             if check_winner()==False:
                player=symbols[0]
                label.config(text=player+ " TURN")

def check_winner():

    for row in range(3):

        if two_d_list[row][0]['text']==two_d_list[row][1]['text']==two_d_list[row][2]['text']!='':
            label.config(text=player+ ' WINS!')
            two_d_list[row][0]['bg']='green'
            two_d_list[row][1]['bg']='green'
            two_d_list[row][2]['bg']='green'
            return True

    for column in range(3):

        if two_d_list[0][column]['text']==two_d_list[1][column]['text']==two_d_list[2][column]['text']!='':
            label.config(text=player+ ' WINS!')
            two_d_list[0][column]['bg']='green'
            two_d_list[1][column]['bg']='green'
            two_d_list[2][column]['bg']='green'
            return True

    if two_d_list[0][0]['text']==two_d_list[1][1]['text']==two_d_list[2][2]['text']!='':
        label.config(text=player+ ' WINS!')
        two_d_list[0][0]['bg'] = 'green'
        two_d_list[1][1]['bg'] = 'green'
        two_d_list[2][2]['bg'] = 'green'
        return True

    if two_d_list[0][2]['text'] == two_d_list[1][1]['text'] == two_d_list[2][0]['text'] != '':
        label.config(text=player + ' WINS!')
        two_d_list[0][2]['bg'] = 'green'
        two_d_list[1][1]['bg'] = 'green'
        two_d_list[2][0]['bg'] = 'green'
        return True

    elif empty_spaces()==True:

        for row in range(3):

            two_d_list[row][0]['bg'] ='yellow'
            two_d_list[row][1]['bg'] = 'yellow'
            two_d_list[row][2]['bg'] = 'yellow'

        for column in range(3):

            two_d_list[0][column]['bg'] = 'yellow'
            two_d_list[1][column]['bg'] = 'yellow'
            two_d_list[2][column]['bg'] = 'yellow'


        two_d_list[0][0]['bg']='yellow'
        two_d_list[0][1]['bg']='yellow'
        two_d_list[0][2]['bg']='yellow'

        return "Tie"
    else:
        return False

def empty_spaces():

        spaces=9
        for row in range(3):
            for column in range(3):
                if two_d_list[row][column]['text']!='':
                    spaces-=1
                    if spaces==0:
                        label.config(text="   TIE!")
                        return True
                else:
                    return False



def new_game():

    label.config(text=random.choice(symbols) + ' TURN')
    for row in range(3):
        for column in range(3):
            two_d_list[row][column]['text']=''
            two_d_list[row][column]['bg']='#F0F0F0'













window = Tk()
WINDOW_WIDTH = 530
WINDOW_HEIGHT = 525
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
window.config(padx=40, pady=120)
window.title('TicTacToe')
window.iconbitmap('favicon.ico')
label = Label(window, text="",font=("Arial Bold", 40))
label.place(x=125,y=-100)

symbols = ('X','O')

player = random.choice(symbols)
label_text = label.config(text=player+' TURN')


two_d_list = (
    [0,0,0],
    [0,0,0],
    [0,0,0])
restart = Button(window, text="RESTART", command=new_game,font=("Arial Bold", 10))
restart.place(x=185,y=-40)

for row in range(3):
    for column in range (3):
        two_d_list[row][column] = Button(window,text= "", width=8, height=3, font=("Arial Bold", 20), command=lambda row=row,column=column: turn(row,column))
        two_d_list[row][column].grid(row=row, column=column)






















window.mainloop()