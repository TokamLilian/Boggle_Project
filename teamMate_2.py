
#Sarah Jolia Enombo Ngosso
#Ange Lilian Tchomtchoua Tokam

#Boggle.py qui simulte le jeux de boggle à plusieurs joueurs
import random


def affichage(word, point, valeur):

    point_affiche = '(' +str(point) + ')' 
    valeur_affiche = "-- " + valeur                                      #valeur est l'issu du mot (rejete ou illegal) retourne par une fonction qui test si le mot existe           
    exit_text = [word, point_affiche, valeur_affiche] 
    return exit_text

                                  #pour toutes les grilles de taille 5x5 en decendant, un mot de taille 8 donne 10 points 
    return point

def lettre (alphabet, longeur):                                       #cette fonction retourne une lettre aleatoire de la chaine passee en paramètre
    rand = True
    while rand:                                                       #on veut aumoins une valeur de position inferieure à la longeur de la chaine
        
        position = int(30*random.random())                            #pour pouvoir couvrir l'autre moitie de la chaine
        if position < longeur:
            rand = False

    letter = alphabet[position]
    return letter

def verification(grille,mot):
    if not est_valide(grille, mot):
        mots_refuses(joueur_actuel, mot, "Mot non présent sur la grille")

    elif mot in mots_acceptes:
                mots_refuses(joueur_actuel, mot, "Mot déjà proposé")

    elif len(mot) < 3:
                mots_refuses(joueur_actuel, mot, "Mot trop court")
    else:
          mots_acceptes(mot)
          if joueur_actuel == 1
                mots_joueur1(mot)
          else:
                mots_joueur2(mot)
    
def test generer_grille():
    assert affichage(point) == "(' +str(point) + ')", point
    assert affichage(valeur) == "-- " + valeur, valeur
    assert affichage(point,valeur) == "(' +str(point) + ')","-- " + valeur, exit_text
                  
def test_validite():
    assert (validite(mot,joueur_actuel,valeur, "ok"))
         assert (validite(mot,joueur_actuel,valeur, "rejete"))
        assert ((validite(mot,joueur_actuel,valeur, "illegal"))
         
def test_calcul_point():
    assert (calcul_point(4, "ABCD") == 2)
        assert (calcul_point(5, "ABCDE") == 3)
        assert (calcul_point(6, "ABCDEF") == 4)
        assert (calcul_point(7, "ABCDEFG") ==7)
        
def test_est_adjacente():
         grille = [ ['T', 'I', 'M', 'E'], ['W', 'O', 'R', 'D'], ['F', 'A', 'C', 'T'], ['G', 'A', 'M', 'E']] 
         assert (est_adjacente(grille, 'TIME') == True
         assert (est_adjacente(grille, 'TOCE') == True
         assert ((est_adjacente(grille, 'TODE') == False
           

      
