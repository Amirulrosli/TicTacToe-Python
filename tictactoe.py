'''
Assessment 1: Tic Tac Toe Game

Muhammad Amirul Amin Bin Rosli [B20210053] BSc in Information Security
Ahmad Izzuddin Bin Azis [B20210115] BSc in Information Security
Justin Ong Yue Xiang [B20210042] BSc in Computer Networking
Bryant Kua Vui Lun [B20210411] BSc in Information Security


'''


from tkinter import *
import tkinter.messagebox
import random


#initialize tkinter / to use Tkinter method 
root = Tk()

#set interface title
root.title("Tic Tac Toe")

#set app icon (only support ico)
root.iconbitmap('favicon.ico')

#disallow app to be resizable
root.resizable(False,False)

#create button (9 button) variables with string var object, that holds type string / to manage value of widget
btn1 = StringVar() 
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

#create variable player 1 and 2 that holds string value
player1 = StringVar()
player2 = StringVar()

#new game with string var object that will holds string value (manage widget)
newGame = StringVar()

#Initialize variable needed for count, players turn and computer turn
count = 0
click = True 
playerTurn = True
computerTurn = False

#set win and draw count to 0 (default)
player1Win = 0
player2Win = 0
draw = 0


#set Image for O, X, Icon
xImg = PhotoImage(file='x.png') 
oImg = PhotoImage(file='o.png')
iconImg = PhotoImage(file='icon.png')
#initialized xoList contains 'X' and 'O'
xoList = ['X','O']


#This function is to generate the First Interface (Instruction and Game Mode)
def gameMode():
    
    #Initialize all components needed for first interface
    #create Game header label
    gameHeader = Label(root, text="Tic Tac Toe!",font=("Arial",10))
    gameHeader.grid(row=1,column=0,pady=10,padx=10)
    
    #Display icon on the grid
    iconPhoto = Label(root, image=iconImg)
    iconPhoto.grid(row=2,column=0,padx=10)
    
    #create instruction label
    instructionLabel = Label(root,text='1. The game is played on a grid that\'s 3 squares by 3 squares.\n2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.',anchor='e', justify='left')
    instructionLabel.grid(row=2,column=1,pady=10,padx=10)
    
    #create game mode label
    gameMode = Label(root, text="Select Game Mode:",font=("Arial",13))
    gameMode.grid(row=3,column=1)
    
    #create button for game mode options which are multiplayer and play against computer button
    multiBtn = Button(root, height=2, width=20, relief='ridge',borderwidth=.5,background='#000000',fg='white',text='Multiplayer',command=lambda:playerOptions(False))
    multiBtn.grid(row=4,column=1,pady=10)
    compBtn = Button(root, height=2, width=20, relief='ridge',borderwidth=.5,background='#ff0000',fg='white',text='Play Against Computer',command=lambda:playerOptions(True))
    compBtn.grid(row=5,column=1,pady=10)
    

#This function is to generate the Second Interface for user to enter player 1 and 2 name
def playerOptions(computer):
    global computerTurn
    
    #set computerTurn into computer variable passed when button for game mode is clicked
    computerTurn = computer
    
    #clear grid component
    deleteComponent()
    
    #create label and input (entry and label widget for players name)
    l1 = Label(root, text="Enter Player 1 Name: ")
    l1.grid(row=0,column=0,padx=10,pady=10)
    entry1 = Entry(root, bg="white", textvariable=player1)
    entry1.grid(row=0,column=1,padx=10,pady=10)
    
    l2 = Label(root, text="Enter Player 2 Name: ")
    l2.grid(row=1,column=0)
    
    #if computerTurn is True, set player 2 as a computer
    if computerTurn:
        #set player to as a computer
        player2.set("Computer")
        entry2 = Entry(root, bg="white", textvariable=player2,state='disabled')
        #add label to grid by row and column
        entry2.grid(row=1,column=1,padx=10,pady=10)
    else:
        #display entry for player 2 name
        entry2 = Entry(root, bg="white", textvariable=player2)
        #add label to grid by row and column
        entry2.grid(row=1,column=1,padx=10,pady=10)
    
    #create startbutton component that execute validateStart() function
    startButton = Button(root,height=2,width=10,text="Start Game", command=lambda:validateStart(player1,player2))
    #add into grid
    startButton.grid(row=3,column=0,padx=10,pady=10)

#Validate players name function
def validateStart(player1,player2):
    
    #check if empty or same return error message and if valid execute second interface which is the background() function
    if player1.get() == '' or player2.get() == '':
        tkinter.messagebox.showerror("Invalid Input", "Please Fill in the empty Field!")
    elif player1.get() == player2.get():
        tkinter.messagebox.showerror("Change Name","Do not use the same name, please change the player's name")
    else:
        background()
        

#This function is to generate the board game (board or grid of X and O game)
def background():
    
    #pass global click and computerturn
    global click,computerTurn
    
    #label each button in the grid accordingly from 1-9
    btn1.set('1')
    btn2.set('2')
    btn3.set('3')
    btn4.set('4')
    btn5.set('5')
    btn6.set('6')
    btn7.set('7')
    btn8.set('8')
    btn9.set('9')
    
    #create background w/ color for 9 buttons and add it into grid by row and column
    #each of this button (9 buttons) when clicked will execute clickBtn() function
    back1 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#ffe6f2',textvariable=btn1,command=lambda:clickBtn(1,0,0,turnLabel))
    back1.grid(row=0,column=0)
    
    back2 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#ffe6f2',textvariable=btn2,command=lambda:clickBtn(2,0,1,turnLabel))
    back2.grid(row=0,column=1)
    
    back3 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#ffe6f2',textvariable=btn3,command=lambda:clickBtn(3,0,2,turnLabel))
    back3.grid(row=0,column=2)

    back4 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#ffe6f2',textvariable=btn4,command=lambda:clickBtn(4,1,0,turnLabel))
    back4.grid(row=1,column=0)

    back5 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#ffe6f2',textvariable=btn5,command=lambda:clickBtn(5,1,1,turnLabel))
    back5.grid(row=1,column=1)

    back6 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#ffe6f2',textvariable=btn6,command=lambda:clickBtn(6,1,2,turnLabel))
    back6.grid(row=1,column=2)

    back7 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#ffe6f2',textvariable=btn7,command=lambda:clickBtn(7,2,0,turnLabel))
    back7.grid(row=2,column=0)

    back8 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#ffe6f2',textvariable=btn8,command=lambda:clickBtn(8,2,1,turnLabel))
    back8.grid(row=2,column=1)
    
    back9 = Button(root, height=10, width=20, relief='groove',borderwidth=.5,background='#ffe6f2',textvariable=btn9,command=lambda:clickBtn(9,2,2,turnLabel))
    back9.grid(row=2,column=2)
    
    #create restart button to restart the game and newBtn for a new game session
    restartBtn = Button(root, height=2, width=10, relief='ridge',borderwidth=.5,background='#000000',fg='white',text='Restart Game',command=lambda:restartGame())
    restartBtn.grid(row=3,column=0)
    
    newBtn = Button(root, height=2, width=10, relief='ridge',borderwidth=.5,background='#ff66d9',fg='white',text='New Game',command=lambda:newGame())
    newBtn.grid(row=3,column=2)
    
    #check players turn (player x or player o)
    if click == True:
        #if click is true, display current turn belongs to player1
        turnLabel = Label(root, text="Turn: "+player1.get()+" (Player 1) ", fg="green")
    else:
        #if click is False, display current turn belongs to player2
        turnLabel = Label(root, text="Turn: "+player2.get()+" (Player 2) ", fg="red")
    #add label to grid
    turnLabel.grid(row=3, column=1)
    
    #Display win score for each player and draw count, display it into the grid
    gameLabel = Label(root, height=3, width=20, text="Win Count", borderwidth=.5).grid(row=4,column=0)
    player1Label = Label(root, height=3,width=20,text=player1.get()+" (Player 1)", bg="white",fg="green",relief='ridge', borderwidth=.5).grid(row=5,column=0,padx=1,pady=1)
    player2Label = Label(root, height=3,width=20,text=player2.get()+" (Player 2)", bg="white",fg="red",relief='ridge', borderwidth=.5).grid(row=5, column=2,padx=1,pady=1)
        
    player1Count = Label(root, height=3,width=20,text=str(player1Win)+" Win ", bg="white",fg="green",relief='ridge', borderwidth=.5).grid(row=6,column=0,padx=1,pady=1)
    drawCount = Label(root, height=3,width=20,text=str(draw)+" Draw(s) ", bg="white",fg="black",relief='ridge', borderwidth=.5).grid(row=6,column=1,padx=1,pady=1)
    player2Count = Label(root, height=3,width=20,text=str(player2Win)+" Win ", bg="white",fg="red",relief='ridge', borderwidth=.5).grid(row=6,column=2,padx=1,pady=1)
    

    #show message (info) which player will play first
    if playerTurn==True:
        tkinter.messagebox.showinfo("Player's Turn", "Player 1: "+player1.get()+" Start First!")
    else:
        tkinter.messagebox.showinfo("Player's Turn", "Player 2: "+player2.get()+" Start First!")
        #if player to is a computer execute computer move function
        if computerTurn:
            computerMove(turnLabel)
    
#once one of the 9 buttons clicked, this function will be executed
def clickBtn(num,row,column,turnLabel):
    #add global click and count var
    global click,count
    
    #check if it is player x or player o
    if click==True: 
        
        #if it is player x turn, add photo of X into row and column associated with the clicked button position
        labelPhoto = Label(root, image=xImg)
        labelPhoto.grid(row=row,column=column)
        click = False
        count +=1
        turnLabel.config(text="Turn: "+player2.get()+" (Player 2) ",fg="red")
        #store X string value into the btn that holds stringVar object
        setBtn(num,'X')
        
    else:
         #if it is player o turn, add photo of O into row and column associated with the clicked button position
        labelPhoto = Label(root, image=oImg)
        labelPhoto.grid(row=row,column=column)
        click = True 
        count+=1
        turnLabel.config(text="Turn: "+player1.get()+" (Player 1) ",fg="green")
         #store O string value into the btn that holds stringVar object
        setBtn(num,'O')
    
    
    
    #Check which player win the game
    checkWin()
    
    #if it is against computer execute computerMove to set computer turn after checkwin()
    if click==FALSE and computerTurn:
        computerMove(turnLabel)

#This function is executed to play the computer's turn
def computerMove(turnLabel):
    
    #if button 5 is not x or o, click button 5 and set it as 'O'
    if btn5.get() not in xoList:
        clickBtn(5,1,1,turnLabel)
    else:
        
        #if not, loop through and set btnNo into random number from 1-9
        computer_Action = True
        while computer_Action:
            btnNo = random.randint(1,9)
            
            #check if button/slot is already fully occupied, then break the loop, if btn is available then execute match statement below
            if btnIsAvailable()==FALSE:
                break
                
            #match the random number to button number, if matched, click the button and set it as 'O'
            # set the computer_Action to False to break the loop
            match btnNo:
                case 1:
                    if btn1.get() not in xoList:
                        clickBtn(1,0,0,turnLabel)
                        computer_Action = FALSE
                case 2:
                    if btn2.get() not in xoList:
                        clickBtn(2,0,1,turnLabel)
                        computer_Action = FALSE
                case 3:
                     if btn3.get() not in xoList:
                        clickBtn(3,0,2,turnLabel)
                        computer_Action = FALSE
                case 4:
                    if btn4.get() not in xoList:
                        clickBtn(4,1,0,turnLabel)
                        computer_Action = FALSE
                case 5:
                    if btn5.get() not in xoList:
                        clickBtn(5,1,1,turnLabel)
                        computer_Action = FALSE
                case 6:
                    if btn6.get() not in xoList:
                        clickBtn(6,1,2,turnLabel)
                        computer_Action = FALSE
                case 7:
                    if btn7.get() not in xoList:
                        clickBtn(7,2,0,turnLabel)
                        computer_Action = FALSE
                case 8:
                    if btn8.get() not in xoList:
                        clickBtn(8,2,1,turnLabel)
                        computer_Action = FALSE
                case 9:
                    if btn9.get() not in xoList:
                        clickBtn(9,2,2,turnLabel)
                        computer_Action = FALSE
                
                
def btnIsAvailable():
    #check if button is already occupied by 'X' or 'O', if fully occupied return false else return true
    if btn1.get() in xoList and btn2.get() in xoList and btn3.get() in xoList \
       and btn4.get() in xoList and btn5.get() in xoList and btn6.get() in xoList \
       and btn7.get() in xoList and btn8.get() in xoList and btn9.get() in xoList  :  
        return FALSE
    else:
        return TRUE        
    

#This function is to store the value x or o into button based on the button number 
# where num is the button number and value is 'X' or 'O'
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
            
#This function is used to check which player win the game
def checkWin():
    global count, player1Win, player2Win,draw
    
    #check if the condition met the win probability (combination)
    if btn1.get() == 'X' and btn2.get()=='X' and btn3.get()=='X' or \
       btn4.get() == 'X' and btn5.get()=='X' and btn6.get()=='X' or \
       btn7.get() == 'X' and btn8.get()=='X' and btn9.get()=='X' or \
       btn1.get() == 'X' and btn4.get()=='X' and btn7.get()=='X' or \
       btn2.get() == 'X' and btn5.get()=='X' and btn8.get()=='X' or \
       btn3.get() == 'X' and btn6.get()=='X' and btn9.get()=='X' or \
       btn1.get() == 'X' and btn5.get()=='X' and btn9.get()=='X' or \
       btn3.get() == 'X' and btn5.get()=='X' and btn7.get()=='X':
        
        #if player x win, show message, add 1 to win count and drawlines 
        # to which 3 buttons (that contains 'X') that met the condition
        
        drawLines('X')
        tkinter.messagebox.showinfo("Game Over", "Player 1: "+player1.get()+ " wins!")
        player1Win +=1
        #restart game
        restartGame()
    
    elif btn1.get() == 'O' and btn2.get()=='O' and btn3.get()=='O' or \
       btn4.get() == 'O' and btn5.get()=='O' and btn6.get()=='O' or \
       btn7.get() == 'O' and btn8.get()=='O' and btn9.get()=='O' or \
       btn1.get() == 'O' and btn4.get()=='O' and btn7.get()=='O' or \
       btn2.get() == 'O' and btn5.get()=='O' and btn8.get()=='O' or \
       btn3.get() == 'O' and btn6.get()=='O' and btn9.get()=='O' or \
       btn1.get() == 'O' and btn5.get()=='O' and btn9.get()=='O' or \
       btn3.get() == 'O' and btn5.get()=='O' and btn7.get()=='O':
        
        #if player o win, show message, add 1 to win count and drawlines indicate
        #which 3 buttons (that contains 'O') that met the condition
        
        drawLines('O')
        tkinter.messagebox.showinfo("Game Over", "Player 2: "+ player2.get() +" wins!")
        player2Win +=1
        
        #restart the game
        restartGame()
        
    elif count==9:
        #show message if draw
        tkinter.messagebox.showinfo("Game Over", "Its a Draw")
        draw+=1
        restartGame()

#This function is used to create straight line once player x or o wins
def drawLines(value):
    #Value in parameter will be 'X' or 'O'
    lineCondition = [btn1.get() == value and btn2.get()==value and btn3.get()==value, \
       btn4.get() == value and btn5.get()==value and btn6.get()==value , \
       btn7.get() == value and btn8.get()==value and btn9.get()==value , \
       btn1.get() == value and btn4.get()==value and btn7.get()==value , \
       btn2.get() == value and btn5.get()==value and btn8.get()==value , \
       btn3.get() == value and btn6.get()==value and btn9.get()==value , \
       btn1.get() == value and btn5.get()==value and btn9.get()==value , \
       btn3.get() == value and btn5.get()==value and btn7.get()==value]
    
    #check which condition statement in lineCondition return true (condition met)
    lineIndex = lineCondition.index(True)
    #set columns, line width and height
    cols = [0,1,2]
    x1 = 130
    y1 = 2
    
    #check condition index indicating which buttons combinations are met
    #execute display line after getting the cols, rows, width and height of the line
    match lineIndex:
        case 0:
            rows = [0,0,0]
            displayLine(rows,cols,x1,y1)
        case 1:
            rows = [1,1,1]
            displayLine(rows,cols,x1,y1)
        case 2:
            rows = [2,2,2]
            displayLine(rows,cols,x1,y1)
        case 3:
            rows = [0,1,2]
            cols = [0,0,0]
            displayLine(rows,cols,y1,x1)
        case 4:
            rows = [0,1,2]
            cols = [1,1,1]
            displayLine(rows,cols,y1,x1)
        case 5:
            rows = [0,1,2]
            cols = [2,2,2]
            displayLine(rows,cols,y1,x1)
        case 6:
            rows = [0,1,2]
            cols = [0,1,2]
            displayLine(rows,cols,x1,y1)
        case 7:
            rows = [0,1,2]
            cols = [2,1,0]
            displayLine(rows,cols,x1,y1)
        
    
#This function is used to display the line on the grid
def displayLine(rows,cols,width,height):
    
    #loops through the rows to add the canvas (line) into the grid
    for i in range(len(rows)):  
        #design the canvas into lines
        frame = Canvas(root,width=width,height=height,bg='#000000',borderwidth=.5,highlightbackground="#000000")
        frame.grid(row=rows[i],column=cols[i])
    
    
#This function is used to restart the game
def restartGame():
    #add global variables
    global count, click,playerTurn
    
    #set count back to 0
    count = 0
    
    #condition to set which player will play first in the next game
    if playerTurn==True:
        click = False
        playerTurn = False

    else:
        click = True
        playerTurn = True
    
    #clear button value, delete all component in the grid slaves and 
    # execute background function for second interface
    clearBtn()
    deleteComponent()
    background()

#This function is used to clear button object values (string values into empty string)
def clearBtn():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')
    
#This new game function is used to generate a new game session and clear the previous session  
def newGame():
    #add global variable
    global player1Win, player2Win,click,count,draw,computerTurn,playerTurn
    
    #set player 1 and player 2 into empty string
    player1.set('')
    player2.set('')
    
    #set win count (score) to 0, click to True and count to 0
    #set all variable to default
    player1Win = 0
    player2Win = 0
    draw=0
    click = True
    count = 0
    click = True 
    computerTurn = False
    playerTurn = True
    
    #clear button value, delete all component in the grid slaves and 
    # execute gamemode function for first interface
    clearBtn()
    deleteComponent()
    gameMode()

#This function is used to delete all components displayed on the grids
def deleteComponent():
    #Delete all components in the grid
    for component in root.grid_slaves():
        component.grid_forget()
        
        


#execute the first interface of the game which is the instruction page
gameMode()

#event handler function
root.mainloop()


