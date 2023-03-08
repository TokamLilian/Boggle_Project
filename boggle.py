#Sarah Jolia Enombo Ngosso
#Ange Lilian Tchomtchoua Tokam

#Boggle.py qui simulte le jeux de boggle à plusieurs joueurs
import random
import struct

def jouer():

    return 


def est_valide(grille, lettre_1, lettre_2):
    #est-ce que le mot est valide ? (3<= longeur <=taille)

    return #validite

def valeur(validité) :
    #validité = 1?
        #est-ce que le mot existe ?
            #valeur = 'ok'
        #sinon
            #valeur = 'rejete'
    #sinon
            #valeur = 'illegal'
    
    return #valeur

def calcul_point(grille, mots):
    point = 0
    return point

def lettre (alphabet, longeur):                                       #cette fonction retourne une lettre aléatoire de la chaine passée en paramètre
    rand = True
    while rand:
        position = int(10*random.random())
        if position < longeur:
            rand = False

    if position < (longeur//2):                                      #pour pouvoir couvrir l'autre moitié de la chaine
        position += position

    letter = alphabet[position]
    return letter

def generer_grille(taille):
    seperator = "-"*((taille*4) +1) 

    #on va faire des structures pour les différents dés et l'affichage aleatoires des elements pour chaque dé
    
    alphabet = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    Dés = []                                                        #la liste de tous les dés de la partie

    nombre_de = taille **2                                          #le nombre total de dés présents

    for _ in range(nombre_de):                                      #ittere sur les différents dés
        dé = []

        for face in range (4):                                      #ittere sur les différentes faces du dé
            dé.append(lettre(alphabet,26))                          #chaque face égale à une lettre aléatoire

        Dés.append(dé)

    #print (Dés)
    
    start = 0                                                       #the first line is made up of random letters from the first dices
    end = taille
    for y in range(taille):
        word = ""
        for x in range (start, end):
            D = Dés[x]
            letter = lettre(D,4)   
            if x == start:
                word += "| " + letter

            else:
                word += " | " + letter

        print (seperator)
        print (word,'|')
        start = start + taille
        end = start + taille          #we go to the next dices for following lines
        
    print (seperator)

    
    #point_affiche = '(' +str(calcul_point) + ')' 
    #valeur_affiche = "-- " + valeur                            #valeur est l'issu du mot (rejété ou illegal) retourné par une fonction qui test si le mot existe           
    #t_exit = [word, point_affiche, valeur_affiche] 
    #print(t_exit)
    #return word 

generer_grille(4)

#jouer()
#generer_grille(taille)
#est_valide(grille, lettre_1, lettre_2)
#calcul_point(grille, mots)

#test()