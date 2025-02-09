# -----------------------
# Date : 25-01-2025
# Auteure : Svelee
# Version : 0.1
# Nom du fichier : Morpion
# -----------------------




from tkinter import *
import random as r

root=Tk()
root.geometry("450x450")
root.minsize(450,450)
root.maxsize(1200,1000)
root.title("TicTacToe")

Dicoimage={
    0:PhotoImage(file='images\\case_vide.png'),
    1:PhotoImage(file='images\\X.png'),
    2:PhotoImage(file='images\\circle.png'),
    3:PhotoImage(file='images\\ez.png'),
    4:PhotoImage(file='images\\ard.png'),
    5:PhotoImage(file='images\\R.png')
    }

grille= [[0,0,0],
         [0,0,0],
         [0,0,0]]
X=True
win=False
Randbot=False
Bbot=False
caseset=False

#Vérifie s'il y a victoire ou égalité / Checks if there's a win or a tie
def wincheck():
    global X
    global win
    global Tie
    win=False
    Tie=False
    for i in range(3):
        if grille[0][i]==grille[1][i] and grille[1][i]==grille[2][i] and grille[0][i]!=0:
            win=True
        if grille[i][0]==grille[i][1] and grille[i][1]==grille[i][2] and grille[i][0]!=0:
            win=True
        if (grille[0][0]==grille[1][1]==grille[2][2] or grille[0][2]==grille[1][1]==grille[2][0]) and grille[1][1]!=0:
            win=True

    if win==True:
        for i in range(3):
            for j in range(3):
                butt=buttons[i][j]
                butt.config(state=DISABLED)
                
        if X==True:
            print ("X won :D")
        else:
            print("O won :D")

    Tie=True
    for i in range(3):
        if 0 in grille[i]:
            Tie=False
    
    if Tie:
        for i in range(3):
            for j in range(3):
                butt=buttons[i][j]
                butt.config(state=DISABLED)
        print("Tie :c")        


#Bot qui joue aléatoirement / bot playing randomly
def randomBotplay():
    wincheck()
    global X
    global win
    z=r.randint(0,2)
    y=r.randint(0,2)
    while grille[z][y]!=0:
        z=r.randint(0,2)
        y=r.randint(0,2)
    if X==True:
        grille[z][y]=1
        buttons[z][y].config(image=Dicoimage[1])
    else:
        grille[z][y]=2
        buttons[z][y].config(image=Dicoimage[2])

    wincheck()
    
    X=not X

#Bot qui joue de manière stratégique / More strategic bot
def Botplay():
    global X
    global win
    global caseset
    caseset=False

    wincheck()

    for i in range(3):
        if caseset==False:
            #Regarde sur une ligne si lui ou l'adversaire occupe deux cases / Checks if opponent or itself got two squares on the same row
            a=grille[i].count(0)
            b=grille[i].count(1)
            c=grille[i].count(2)
            if a==1 and (b==2 or c==2):
                if X:
                    buttons[i][grille[i].index(0)].config(image=Dicoimage[1])
                    grille[i][grille[i].index(0)]=1
                    caseset=True
                else:
                    buttons[i][grille[i].index(0)].config(image=Dicoimage[2])
                    grille[i][grille[i].index(0)]=2
                    caseset=True
    
    if caseset==False:
        for i in range(3):
            #Regarde sur une colonne si lui ou l'adversaire occupe deux cases / Checks if opponent or itself got two squares on the same column
            if (grille[0][i]==grille[1][i] or grille[2][i]==grille[1][i] or grille[0][i]==grille[2][i]) and ((grille[0][i]!=0 and grille[1][i]!=0) or (grille[2][i]!=0 and grille[1][i]!=0) or (grille[0][i]!=0 and grille[2][i]!=0)):
                for j in range(3):
                    if caseset==False:
                        if grille[j][i]==0:
                            if X:
                                grille[j][i]=1
                                buttons[j][i].config(image=Dicoimage[1])
                                caseset=True
                            else:
                                grille[j][i]=2
                                buttons[j][i].config(image=Dicoimage[2])
                                caseset=True
    
    if caseset==False:
        #Regarde sur une diagonale si lui ou l'adversaire occupe deux cases / Checks if opponent of itself got two squares on one diagonal
        if (grille[0][0]==grille[1][1] or grille[1][1]==grille[2][2] or grille[0][0]==grille[2][2]) and ((grille[0][0]!=0 and grille[1][1]!=0) or (grille[2][2]!=0 and grille[1][1]!=0) or (grille[0][0]!=0 and grille[2][2]!=0)):
            for i in range (3):
                if caseset==False:
                    if grille[i][i]==0:
                        if X:
                            grille[i][i]=1
                            buttons[i][i].config(image=Dicoimage[1])
                            caseset=True
                        else:
                            grille[i][i]=2
                            buttons[i][i].config(image=Dicoimage[2])
                            caseset=True
    
    if caseset==False:
        #Regarde sur l'autre diagonale si lui ou l'adversaire occupe deux cases / Checks if opponent of itself got two squares on the other diagonal
        if (grille[0][2]==grille[1][1] or grille[1][1]==grille[2][0] or grille[0][2]==grille[2][0]) and ((grille[0][2]!=0 and grille[1][1]!=0) or (grille[2][0]!=0 and grille[1][1]!=0) or (grille[0][2]!=0 and grille[2][0]!=0)):
            for i in range (3):
                if caseset==False:
                    if grille[i][2-i]==0:
                        print('Diagonale2')
                        if X:
                            grille[i][2-i]=1
                            buttons[i][2-i].config(image=Dicoimage[1])
                            caseset=True
                        else:
                            grille[i][2-i]=2
                            buttons[i][2-i].config(image=Dicoimage[2])
                            caseset=True

    if caseset==False:
    #Si aucune des conditions ci-dessus n'est remplie, occupe un coin aléatoire / If none of the above, takes a random corner
        z=r.choice([0,2])
        y=r.choice([0,2])
        while grille[z][y]!=0:
            z=r.choice([0,2])
            y=r.choice([0,2])
        if X:
            grille[z][y]=1
            buttons[z][y].config(image=Dicoimage[1])
            caseset=True
        else:
            grille[z][y]=2
            buttons[z][y].config(image=Dicoimage[2])
            caseset=False
    wincheck()
    X=not X

#Permet de jouer / Allows the player to take a square
def clickbutton(row,col):
    global caseset
    global Randbot
    global Bbot
    global X
    global win
    wincheck()
    if grille[row][col]==0:
        if X==True:
            grille[row][col]=1
            buttons[row][col].config(image=Dicoimage[1])
        else:
            grille[row][col]=2
            buttons[row][col].config(image=Dicoimage[2])

        wincheck()
        X = not X
        if win==False:
            if Tie==False:
                if Bbot:
                    Botplay()
                elif Randbot:
                    randomBotplay()
    
#Rénitialise la grille / Create a new grid
def reset():
    global win
    global X
    X=True
    win=False
    for i in range(3):
        for j in range(3):
            grille[i][j]=0
            buttons[i][j].config(image=Dicoimage[0], state=NORMAL)

#Crée des boutons / Create buttons
buttons = [[None for _ in range(3)] for _ in range(3)]

for a in range (3):
    for b in range (3):
        buttons[a][b] = Button(root, image=Dicoimage[grille[a][b]], command=lambda i=a, j=b:clickbutton(i,j), bg="#111111")
        buttons[a][b].grid(row=a,column=b)

#Les deux fonctions ci-dessous permettent d'activer ou de désactiver les bots / The two fonction below allows the player to activate or desactivate bots
def Rbot():
    global Randbot
    Randbot=not Randbot

def Bplay():
    global Bbot
    Bbot=not Bbot

#Configuration des boutons  
RandomBot=Button(root,image=Dicoimage[3],command=Rbot)
RandomBot.grid(row=0,column=3)

SmartBot=Button(root,image=Dicoimage[4], command=Bplay)
SmartBot.grid(row=1, column=3)

Reseting=Button(root,image=Dicoimage[5], command=reset)
Reseting.grid(row=2,column=3)


root.mainloop()
