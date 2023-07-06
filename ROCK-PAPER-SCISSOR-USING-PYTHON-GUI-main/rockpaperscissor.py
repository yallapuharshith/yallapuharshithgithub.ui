from tkinter import*
from PIL import Image,ImageTk
import random


noofchoices=5
game=['rock','paper','scissor']
root = Tk()
root.title("LET'S PLAY")
root.configure(background="yellow")

name=Label(root,text="game aadu mowaa",font=100,bg="yellow")
name.grid(row=0,column=2)
#images
crock = ImageTk.PhotoImage(Image.open("comprock.png"))
cpaper = ImageTk.PhotoImage(Image.open("comppaper.png"))
cscissor = ImageTk.PhotoImage(Image.open("compscissors.png"))
urock = ImageTk.PhotoImage(Image.open("userrock.png"))
upaper = ImageTk.PhotoImage(Image.open("userpaper.png"))
uscissor = ImageTk.PhotoImage(Image.open("userscissors.png"))

#inserting images
complabel = Label(root, image=cpaper,bg="yellow")
userlabel = Label(root, image=upaper,bg="yellow")
complabel.grid(row=2,column=0)
userlabel.grid(row=2,column=5)

#scores
compscore = Label(root, text=0,bg="yellow",font=100,fg="blue")
userscore = Label(root, text=0,bg="yellow",font=100,fg="blue")
compscore.grid(row=2,column=1)
userscore.grid(row=2,column=3)

#outputmessage
result=Label(root,font=100,width=30,height=1,fg="#083248",bg="white")
result.grid(row=2,column=2)

#player choice
def playerchoice(x):
   #computer's
    computer=random.choice(game)
    a = game.index(computer)
    if computer=="rock":
        complabel.configure(image=crock)
    elif computer=="paper":
        complabel.configure(image=cpaper)
    if computer=="scissor":
        complabel.configure(image=cscissor)

    #player's
    if x=="rock":
        userlabel.configure(image=urock)
    elif x=="paper":
        userlabel.configure(image=upaper)
    else:
        userlabel.configure(image=uscissor)
    b=game.index(x)

#updatescores

    if b==a+1 or a==b+2:
        score=int(userscore["text"])
        score+=1
        userscore["text"] = str(score)
        result["text"]="YOU WIN 😃"
    elif a==b+1 or b==a+2:
        score=int(compscore["text"])
        score+=1
        compscore["text"] = str(score)
        result["text"] = "YOU LOSE 😕"
    else:
        result["text"] = "TIE 😐"



#buttons

rock = Button(root,text="ROCK",font=100,bg="red",fg="white",height=2,width=10,command=lambda:playerchoice("rock"))
paper = Button(root,text="PAPER",font=100,bg="blue",fg="white",height=2,width=10,command=lambda:playerchoice("paper"))
scissor = Button(root,text="SCISSOR",font=100,bg="orange",fg="white",height=2,width=10,command=lambda:playerchoice("scissor"))
rock.grid(row=4,column=1)
paper.grid(row=4,column=2)
scissor.grid(row=4,column=3)





#indicator
comp = Label(root,text="COMPUTER",font=100,bg="yellow")
user = Label(root,text="YOU",font=100,bg="yellow")
comp.grid(row=1,column=0)
user.grid(column=5,row=1)


root.mainloop()
