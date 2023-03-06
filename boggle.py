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

def generer_grille(taille):
    seperator = "-"*((taille*4) +1) 
    
    for line in range (taille):
        
        word = ""
        for column in range (taille):

            #alphabet = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
            #alphabet = [ 'V', 'O', 'I', 'T', 'U', 'R', 'E', 'M', 'A', 'R', 'M', 'I', 'T', 'E'  ]
            #position = int(10*random.random())
            #letter = alphabet[position]

            #on va faire des structures pour les différents dés et l'affichage aleatoires des elements pour chaque dé
            
            Dés = struct(   De1 = struct('q','q','e','r','t','t','t'),
                            De2 = struct('v','v','v','v','g','g','g'),
                            etc = "etc" )
                   
            nombre_de = taille **2
            for x in range (nombre_de):
                D = Dés[x]
                for y in taille:
                    letter = D[y]   
                    if column == 0:
                        word += "| " + letter

                    else:
                        word += " | " + letter
            
        print (seperator)
        print (word,'|')
    print (seperator)

    
    point_affiche = '(' +str(calcul_point) + ')' 
    valeur_affiche = "-- " + valeur                            #valeur est l'issu du mot (rejété ou illegal) retourné par une fonction qui test si le mot existe           
    t_exit = [word, point_affiche, valeur_affiche] 
    print(t_exit)
    return word 
generer_grille(6)

#jouer()
#generer_grille(taille)
#est_valide(grille, lettre_1, lettre_2)
#calcul_point(grille, mots)

#test()