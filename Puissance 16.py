from random import *

def grille_vide() : #question 1
    """fait apparaitre une grille vide de puissance 2 du jeu de puissance 4"""
    grille=[[0]*7 for i in range(6)]
    return grille


def affiche(g) : #question 2
    for k in range(6) :
        for w in range(7) :
            if g[5-k][w] == 0 :
                print(".",end=" ")
            elif g[5-k][w] == 1 :
                print("X",end=" ")
            elif g[5-k][w] == 2 :
                print("O",end=" ")
                
        print()


def coup_possible(g,c) : #question 3
    return g[5][c] == 0


def jouer(g,j,c) : #question 4
    z = 0
    while g[z][c] != 0 :
        z += 1
    g[z][c] = j
    return g


def horiz(g,j,l,c) : #question 5
##    m = g[l][c]
##    for i in range (0,5) :
##        if m != g[i][c] :
##            return False
##    return True 


    return g[l][c]==j and g[l][c+1]==j and g[l][c+2]==j and g[l][c+3]==j

def vert(g,j,l,c) :
    return g[l][c]==j and g[l+1][c]==j and g[l+2][c]==j and g[l+3][c]==j

def diag_haut(g,j,l,c) :
    return g[l][c]==j and g[l+1][c+1]==j and g[l+2][c+2]==j and g[l+3][c+3]==j

def diag_bas(g,j,l,c) :
    return g[l][c]==j and g[l-1][c+1]==j and g[l-2][c+2]==j and g[l-3][c+3]==j

def victoire(g,j) : #question 6      
    for i in range(0,3):
        for f in range(0,7):
            if vert(g,j,i,f): return True
            
    for i in range(0,4):
        for f in range(0,4):
            if diag_haut(g,j,i,f): return True
            
    for i in range(3,6):
        for f in range(0,4):
            if diag_bas(g,j,i,f): return True


    for i in range(0,6):
        for f in range(0,4):
            if horiz(g,j,i,f): return True
     
    return False


def match_nul(g):  #question 7
    if victoire(g,1)==True : return False
    if victoire(g,2)==True : return False
    for e in g[5]:
        if e==0: return False
    return True


def coup_aléatoire(g,j):  #question 8
    while True:
        p = randint(0,6)
        if coup_possible(g,p):
            jouer(g,j,p)
            return g
    

def ia_vs_ia():  #question 9
    '''fonction qui premet a deux utilisateur de jouer au puissance 4 l'un contre l'autre.
    Il faut rentrer des valeurs entre 0 et 6
    '''
    g=grille_vide()
    while match_nul(g)!=True:
        coup_aléatoire(g,1)
        affiche(g)
        print("-----------------")
        if victoire(g,1):
            print("Victoire du joueur X !")
            return
        coup_aléatoire(g,2)
        affiche(g)
        print("-----------------")
        if victoire(g,2):
            print("Victoire du joueur O !")
            return
        
    affiche(g)
    return "Match nul"
    

def j_s_ia(g,j,c):  #question 10
    '''fonction qui premet a un utilisateur de jouer au puissance 4 contre l'ordinatueur.
    Il faut rentrer des valeurs entre 0 et 6
    '''
    jouer(g,j,c)
    if victoire(g,j)== True:
        affiche(g)
        return "Vous avez gagné !"
    if j==1:
        coup_aléatoire(g,2)
        if victoire(g,2)== True:
            affiche(g)
            return "L'ordinatuer a gagné"
        if match_nul(g) == True:
            affiche(g)
            return "Il y a égalité."
        affiche(g)
        return g
    if j==2:
        coup_aléatoire(g,1)
        if victoire(g,1) == True:
            affiche(g)
            return "L'ordinatuer a gagné."
        if match_nul(g) == True:
            affiche(g)
            return "Il y a égalité."
        affiche(g)
        return g
    

def s():
    '''fonction qui premet a deux utilisateur de jouer au puissance 4 l'un contre l'autre.
    Il faut rentrer des valeurs entre 0 et 6
    '''
    g=grille_vide()
    affiche(g)
    print("0 1 2 3 4 5 6")
    print()
    while True:
        a=int(input("Le joueur 1 (signe X) choisit une colonne : "))
        if a < 0 :
            jouer(g,1,0)
        elif a > 6 :
            jouer(g,1,6)
        else :
            jouer(g,1,a)
        affiche(g)
        print("0 1 2 3 4 5 6")
        if victoire(g,1):
            print("Le joueur X a gagné !")
            return
        print ()
        a=int(input("Le joueur 2 (signe O) choisit une colonne : "))
        if a < 0 :
            jouer(g,2,0)
        elif a > 6 :
            jouer(g,2,6)
        else :
            jouer(g,2,a)
        affiche(g)
        print("0 1 2 3 4 5 6")
        print()
        if victoire(g,2):
            print("Le joueur O a gagné !")
            return
        if match_nul(g):
            print("Il y a égalité.")
            return

def j_vs_ia() :
    g=grille_vide()
    affiche(g)
    print("0 1 2 3 4 5 6")
    print()
    while True:
        a=int(input("Le joueur 1 (signe X) choisit une colonne : "))
        if a < 0 :
            jouer(g,1,0)
        elif a > 6 :
            jouer(g,1,6)
        else :
            jouer(g,1,a)
        if victoire(g,1):
            affiche(g)
            print("Vous avez gagné !")
            return
        print ()
        
        coup_aléatoire(g,2)
        affiche(g)
        print("0 1 2 3 4 5 6")
        print()
        if victoire(g,2): return "L'ordinatueur a gagné."
        if match_nul(g): return "Il y a égalité."



c = int(input("Comment voulez vous jouer ? \n1 pour faire une partie contre un autre joueur \n2 pour faire une partie contre l'ordinateur et \n3 pour voir une partie ia contre ia. \n==> "))
if c == 1 :
    s()
elif c == 2 :
    j_vs_ia()
else :
    ia_vs_ia()
