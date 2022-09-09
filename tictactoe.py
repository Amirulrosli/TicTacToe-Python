from tkinter import *
import tkinter.messagebox

#intialize tkinter / to use the method, etc
root = Tk()

#set icon
root.iconbitmap('icon.ico')

#set title
root.title("Tic Tac Toe")

#Disallow resize
root.resizable(False,False)

#click -> True (start with X)
click = True
count = 0

#Win Count
player1Win = 0
player2Win = 0

#Create Button (9 button), type of string
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
newGame = StringVar()


#set image for o and x
xImg = PhotoImage(file="x.png")
oImg = PhotoImage(file="o.png")

#First Page window, Player 1 & 2 name
def playerOptions():

    #Label and input entry field
    l1 = Label(root, text="Enter Player 1 Name: ")
    l1.grid(row=0,column=0,padx=2,pady=10)
    entry1 = Entry(root,bg="white",textvariable=player1)
    entry1.grid(row=0,column=1,padx=5,pady=10)
    
    l2 = Label(root, text="Enter Player 2 Name: ")
    l2.grid(row=1,column=0,padx=2,pady=10)
    entry2 = Entry(root,bg="white",textvariable=player2)
    entry2.grid(row=1,column=1,padx=5,pady=10)
    
    #startButton to start the game
    startButton = Button(root, text="Start",width=10, height=2, command=lambda:validateStart(player1,player2)).grid(row=3,column=0,pady=5)
    
#to validate the input whether it is valid or not (same name and empty field is invalid)
def validateStart(player1,player2):
    if player1.get() == "" or player2.get() == "":
        tkinter.messagebox.showerror("Invalid Input","Please Fill in the empty field")
    elif player1.get() == player2.get():
        tkinter.messagebox.showerror("Change Player's Name","Do not use the same player name!")
    else:
        background()

#render second interface with the game grid
def background():
    global click, player1Win,player2Win
    
    #create Background w/ color for the 9 buttons (r=>row,c=>column)
    back1 = Button(root,height=10,width=20,relief='groove',borderwidth=.5,background='#f2e6ff', textvariable=btn1,command=lambda:clickBtn(1,0,0,turnLabel))
    back1.grid(row=0,column=0)
    
    back2 = Button(root,height=10,width=20,relief='groove',borderwidth=.5,background='#f2e6ff', textvariable=btn2,command=lambda:clickBtn(2,0,1,turnLabel))
    back2.grid(row=0,column=1)
    
    back3 = Button(root,height=10,width=20,relief='groove',borderwidth=.5,background='#f2e6ff', textvariable=btn3,command=lambda:clickBtn(3,0,2,turnLabel))
    back3.grid(row=0,column=2)
    
    back4 = Button(root,height=10,width=20,relief='groove',borderwidth=.5,background='#f2e6ff', textvariable=btn4,command=lambda:clickBtn(4,1,0,turnLabel))
    back4.grid(row=1,column=0)
    
    back5 = Button(root,height=10,width=20,relief='groove',borderwidth=.5,background='#f2e6ff', textvariable=btn5,command=lambda:clickBtn(5,1,1,turnLabel))
    back5.grid(row=1,column=1)
    
    back6 = Button(root,height=10,width=20,relief='groove',borderwidth=.5,background='#f2e6ff', textvariable=btn6,command=lambda:clickBtn(6,1,2, turnLabel))
    back6.grid(row=1,column=2)
    
    back7 = Button(root,height=10,width=20,relief='groove',borderwidth=.5,background='#f2e6ff', textvariable=btn7,command=lambda:clickBtn(7,2,0,turnLabel))
    back7.grid(row=2,column=0)
    
    back8 = Button(root,height=10,width=20,relief='groove',borderwidth=.5,background='#f2e6ff', textvariable=btn8,command=lambda:clickBtn(8,2,1,turnLabel))
    back8.grid(row=2,column=1)
    
    back9 = Button(root,height=10,width=20,relief='groove',borderwidth=.5,background='#f2e6ff', textvariable=btn9,command=lambda:clickBtn(9,2,2,turnLabel))
    back9.grid(row=2,column=2)

    back10 = Button(root,height=2,width=10,relief='ridge',borderwidth=.5,fg='white',background='#000000', text="Restart Game",command=lambda:restartGame())
    back10.grid(row=3,column=0)
    
    #show the players turn
    if click==True:
        turnLabel = Label(root, text="Turn: "+player1.get()+" (Player 1)", fg="green")
    else: 
        turnLabel = Label(root,text="Turn: "+player2.get()+" (Player 2)", fg="red")
    
    turnLabel.grid(row=3,column=1) 
    
    #new game button if player want to start new game
    newBtn = Button(root,height=2,width=10,relief='ridge',borderwidth=.5,fg='white',background='#ff4d4d', text="New Game",command=lambda:newGame())
    newBtn.grid(row=3,column=2)
    
    #show win count for each player
    gameLabel=Label(root,height=3,width=20,text="Win Count", borderwidth=.5).grid(row=4, column=0)
    player1Label = Label(root, height=3,width=20,text=player1.get()+" (Player 1)", bg="white",fg="green",relief='ridge', borderwidth=.5).grid(row=5,column=0,padx=1,pady=1)
    player2Label = Label(root, height=3,width=20,text=player2.get()+" (Player 2)", bg="white",fg="red",relief='ridge', borderwidth=.5).grid(row=5, column=1,padx=1,pady=1)
    
    player1Count = Label(root, height=3,width=20,text=str(player1Win)+" Win ", bg="white",fg="green",relief='ridge', borderwidth=.5).grid(row=6,column=0,padx=1,pady=1)
    player2Count = Label(root, height=3,width=20,text=str(player2Win)+" Win ", bg="white",fg="red",relief='ridge', borderwidth=.5).grid(row=6,column=1,padx=1,pady=1)
    

#X and O if button is clicked  
def clickBtn(num,row,column,turnLabel):
    global click,count
    
    #check if click is true show X image else if false show O image and show which player turn
    if click==True:
        labelPhoto = Label(root, image=xImg)
        labelPhoto.grid(row=row,column=column)
        turnLabel.config(text="Turn: "+player2.get()+" (Player 2)", fg="red")
        click = False
        count+=1
        setBtn(num,'X')
    else:
        labelPhoto = Label(root, image=oImg)
        labelPhoto.grid(row=row,column=column)
        turnLabel.config(text="Turn: "+player1.get()+" (Player 1)", fg="green")
        click = True
        count+=1
        setBtn(num,'O')
    
    #check who win the game / draw if button clickes 9 times
    checkWin()

#set value to btn1-9 depending on which grid is clicked
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
    
#check win by combination e.g (1,2,3)
def checkWin():
    global count,click, player1Win, player2Win
    
    #check if the condition met the win probability (combination possibility)
    if btn1.get() == 'X' and btn2.get()=='X' and btn3.get()=='X' or \
       btn4.get() == 'X' and btn5.get()=='X' and btn6.get()=='X' or \
       btn7.get() == 'X' and btn8.get()=='X' and btn9.get()=='X' or \
       btn1.get() == 'X' and btn4.get()=='X' and btn7.get()=='X' or \
       btn2.get() == 'X' and btn5.get()=='X' and btn8.get()=='X' or \
       btn3.get() == 'X' and btn6.get()=='X' and btn9.get()=='X' or \
       btn1.get() == 'X' and btn5.get()=='X' and btn9.get()=='X' or \
       btn3.get() == 'X' and btn5.get()=='X' and btn7.get()=='X':
        
        #Display message and count ++ (if player 1 win), after that restart the game
        tkinter.messagebox.showinfo("Game Over","Player 1: "+player1.get()+ " Wins!")
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
        
        #Display message and count ++ (if player 2 win) after that restart the game
        tkinter.messagebox.showinfo("Game Over","Player 2: "+ player2.get() +" Wins!")
        player2Win +=1
        restartGame()
        
    elif count==9:
        #Display message if draw
        tkinter.messagebox.showinfo("Tie Game","Its a Draw!!")
        restartGame()
    
#clear value in each button
def clearGame():
    btn1.set("")
    btn2.set("")
    btn3.set("")
    btn4.set("")
    btn5.set("")
    btn6.set("")
    btn7.set("")
    btn8.set("")
    btn9.set("")

#restart the game
def restartGame():
    global click, count
    click=True
    count=0
    deleteComponent()
    clearGame()
    background()

#function to create a new game
def newGame():    
    global click, count, root,player1Win,player2Win          
    click=True
    count=0
    player1.set('')
    player2.set('')
    player1Win = 0
    player2Win = 0
    clearGame()
    deleteComponent()
    playerOptions()

#function to delete component set in the grids
def deleteComponent():
    #Delete all component on the grids  
    for label in root.grid_slaves():
        label.grid_forget()
    
    
    
# Render first Interface
playerOptions()

#event handler function (event)
root.mainloop()

'''
Muhammad Amirul Amin IS 
Please state /credit the owner of this code. If you want to copy this code, please cite as shown below:

Credit: Amirul Rosli (Maars Technologies), TicTacToe

'''