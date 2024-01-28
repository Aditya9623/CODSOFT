from tkinter import *
# from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)


playerScore = Label(root, text=0, font = ("arial", "40", "bold"), bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font = ("arial", "40", "bold"), bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

user_indicator = Label(root, font = ("arial", "20", "bold"), text="\n: USER : \n--------------------------", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font = ("arial", "20", "bold"), text="\n: COMPUTER : \n--------------------------",
                       bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

msg = Label(root,  font = ("arial", "20", "bold"), bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)



def updateMessage(x):
    msg['text'] = x



def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)



def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)



def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose!!!")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose!!!")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose!!!")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()

    else:
        pass



choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)


rock = Button(root, width=20, height=2, font = ("arial", "10", "bold"), text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, font = ("arial", "10", "bold"), text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, font = ("arial", "10", "bold"), text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()