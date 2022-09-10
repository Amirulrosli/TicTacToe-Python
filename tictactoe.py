from tkinter import *
import tkinter.messagebox

#initialize tkinter / to use method
root = Tk()

root.title("Tic Tac Toe")
root.iconbitmap('icon.ico')
root.resizable(False,False)

#create button (9 button), type string
btn1 = StringVar() 
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()
player1 = StringVar()
player2 = StringVar()
#Initialize variable needed
count = 0
click = True #Player X

#win count
player1Win = 0
player2Win = 0

#new game btn
newGame = StringVar()

#set Image for O and X
xImg = PhotoImage(file='x.png') 
oImg = PhotoImage(file='o.png')

#First Page
def playerOptions():
    
    #Input for players name
    l1 = Label(root, text="Enter Player 1 Name: ")
    l1.grid(row=0,column=0,padx=10,pady=10)
    entry1 = Entry(root, bg="white", textvariable=player1)
    entry1.grid(row=0,column=1,padx=10,pady=10)
    
    l2 = Label(root, text="Enter Player 2 Name: ")
    l2.grid(row=1,column=0)
    entry2 = Entry(root, bg="white", textvariable=player2)
    entry2.grid(row=1,column=1,padx=10,pady=10)
    
    startButton = Button(root,height=2,width=10,text="Start Game", command=lambda:validateStart(player1,player2))
    startButton.grid(row=3,column=0,padx=10,pady=10)

#Validate name
def validateStart(player1,player2):
    if player1.get() == '' or player2.get() == '':
        tkinter.messagebox.showerror("Invalid Input", "Please Fill in the empty Field!")
    elif player1.get() == player2.get():
        tkinter.messagebox.showerror("Change Name pls","Please change your name")
    else:
        background()
        

#Second Page
def background():
    global click
    
    #create background w/ color for 9 buttons
    back1 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#f2e6ff',textvariable=btn1,command=lambda:clickBtn(1,0,0,turnLabel))
    back1.grid(row=0,column=0)
    
    back2 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#f2e6ff',textvariable=btn2,command=lambda:clickBtn(2,0,1,turnLabel))
    back2.grid(row=0,column=1)
    
    back3 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#f2e6ff',textvariable=btn3,command=lambda:clickBtn(3,0,2,turnLabel))
    back3.grid(row=0,column=2)

    back4 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#f2e6ff',textvariable=btn4,command=lambda:clickBtn(4,1,0,turnLabel))
    back4.grid(row=1,column=0)

    back5 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#f2e6ff',textvariable=btn5,command=lambda:clickBtn(5,1,1,turnLabel))
    back5.grid(row=1,column=1)

    back6 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#f2e6ff',textvariable=btn6,command=lambda:clickBtn(6,1,2,turnLabel))
    back6.grid(row=1,column=2)

    back7 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#f2e6ff',textvariable=btn7,command=lambda:clickBtn(7,2,0,turnLabel))
    back7.grid(row=2,column=0)

    back8 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#f2e6ff',textvariable=btn8,command=lambda:clickBtn(8,2,1,turnLabel))
    back8.grid(row=2,column=1)
    
    back9 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#f2e6ff',textvariable=btn9,command=lambda:clickBtn(9,2,2,turnLabel))
    back9.grid(row=2,column=2)
    
    restartBtn = Button(root, height=2, width=10, relief='ridge',borderwidth=.5,background='#000000',fg='white',text='Restart Game',command=lambda:restartGame())
    restartBtn.grid(row=3,column=0)
    
    newBtn = Button(root, height=2, width=10, relief='ridge',borderwidth=.5,background='#ff66d9',fg='white',text='New Game',command=lambda:newGame())
    newBtn.grid(row=3,column=2)
    
    if click == True:
        turnLabel = Label(root, text="Turn: "+player1.get()+" (Player 1) ", fg="green")
    else:
        turnLabel = Label(root, text="Turn: "+player2.get()+" (Player 2) ", fg="red")
        
    turnLabel.grid(row=3, column=1)
    
    gameLabel = Label(root, height=3, width=20, text="Win Count", borderwidth=.5).grid(row=4,column=0)
    player1Label = Label(root, height=3,width=20,text=player1.get()+" (Player 1)", bg="white",fg="green",relief='ridge', borderwidth=.5).grid(row=5,column=0,padx=1,pady=1)
    player2Label = Label(root, height=3,width=20,text=player2.get()+" (Player 2)", bg="white",fg="red",relief='ridge', borderwidth=.5).grid(row=5, column=1,padx=1,pady=1)
    
    player1Count = Label(root, height=3,width=20,text=str(player1Win)+" Win ", bg="white",fg="green",relief='ridge', borderwidth=.5).grid(row=6,column=0,padx=1,pady=1)
    player2Count = Label(root, height=3,width=20,text=str(player2Win)+" Win ", bg="white",fg="red",relief='ridge', borderwidth=.5).grid(row=6,column=1,padx=1,pady=1)

def clickBtn(num,row,column,turnLabel):
    global click,count
    
    if click==True: #player x
        labelPhoto = Label(root, image=xImg)
        labelPhoto.grid(row=row,column=column)
        click = False #player o
        count +=1
        turnLabel.config(text="Turn: "+player2.get()+" (Player 2) ",fg="red")
        setBtn(num,'X')
        
    else:
        labelPhoto = Label(root, image=oImg)
        labelPhoto.grid(row=row,column=column)
        click = True #player o
        count+=1
        turnLabel.config(text="Turn: "+player1.get()+" (Player 1) ",fg="green")
        setBtn(num,'O')
    checkWin()

def setBtn(num, value):
    
    match num:
        case 1:
            btn1.set(value)
        case 2:
            btn2.set(value)
        case 3:
            btn3.set(value)
        case 4:
            btn4.set(value)
        case 5:
            btn5.set(value)
        case 6:
            btn6.set(value)
        case 7:
            btn7.set(value)
        case 8:
            btn8.set(value)
        case 9:
            btn9.set(value)
            

def checkWin():
    global count, player1Win, player2Win
    #check siapa manang
    
    #check if the condition met the win probability (combination possibility)
    if btn1.get() == 'X' and btn2.get()=='X' and btn3.get()=='X' or \
       btn4.get() == 'X' and btn5.get()=='X' and btn6.get()=='X' or \
       btn7.get() == 'X' and btn8.get()=='X' and btn9.get()=='X' or \
       btn1.get() == 'X' and btn4.get()=='X' and btn7.get()=='X' or \
       btn2.get() == 'X' and btn5.get()=='X' and btn8.get()=='X' or \
       btn3.get() == 'X' and btn6.get()=='X' and btn9.get()=='X' or \
       btn1.get() == 'X' and btn5.get()=='X' and btn9.get()=='X' or \
       btn3.get() == 'X' and btn5.get()=='X' and btn7.get()=='X':
           
        tkinter.messagebox.showinfo("Game Over", "Player 1: "+player1.get()+ " wins!")
        player1Win +=1
        restartGame()
    
    elif btn1.get() == 'O' and btn2.get()=='O' and btn3.get()=='O' or \
       btn4.get() == 'O' and btn5.get()=='O' and btn6.get()=='O' or \
       btn7.get() == 'O' and btn8.get()=='O' and btn9.get()=='O' or \
       btn1.get() == 'O' and btn4.get()=='O' and btn7.get()=='O' or \
       btn2.get() == 'O' and btn5.get()=='O' and btn8.get()=='O' or \
       btn3.get() == 'O' and btn6.get()=='O' and btn9.get()=='O' or \
       btn1.get() == 'O' and btn5.get()=='O' and btn9.get()=='O' or \
       btn3.get() == 'O' and btn5.get()=='O' and btn7.get()=='O':
           
        tkinter.messagebox.showinfo("Game Over", "Player 2: "+ player2.get() +" wins!")
        player2Win +=1
        restartGame()
        
    elif count==9:
        tkinter.messagebox.showinfo("Game Over", "Its a Draw")
        restartGame()

def restartGame():
    global count, click
    count = 0
    click = True
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')
    deleteComponent()
    background()
    
def newGame():
    global player1Win, player2Win
    restartGame()
    player1.set('')
    player2.set('')
    player1Win = 0
    player2Win = 0
    deleteComponent()
    playerOptions()

def deleteComponent():
    #Delete all components in the grid
    for component in root.grid_slaves():
        component.grid_forget()


#declare background
playerOptions()

#event handler function
root.mainloop()

