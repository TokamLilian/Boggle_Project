#Sarah Jolia Enombo Ngosso
#Ange Lilian Tchomtchoua Tokam

#Boggle.py qui simulte le jeux de boggle à plusieurs joueurs
import random

def jouer():

    return 

def generer_grille(taille):
    seperator = "-"*((taille*4) +1) 
    
    for line in range (taille):
        
        word = ""
        for column in range (taille):
            alphabet = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
            position = int(10*random.random())
            letter = alphabet[position]
            if column == 0:
                word += "| " + letter
                
            else:
                word += " | " + letter
            
        print (seperator)
        print (word,'|')
    print (seperator)

    return word 
generer_grille(5)

def est_adjacente(grille, lettre_1, lettre_2):

    return 

def calcul_point(grille, mots):

    return 

#jouer()
#generer_grille(taille)
#est_adjacente(grille, lettre_1, lettre_2)
#calcul_point(grille, mots)

#test()