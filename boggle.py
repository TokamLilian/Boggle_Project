#Sarah Jolia Enombo Ngosso
#Ange Lilian Tchomtchoua Tokam

#Boggle.py qui simulte le jeux de boggle à plusieurs joueurs
import random

def est_valide(grille, lettre_1, lettre_2):

    #est-ce que le mot est de la bonne taille ? (3<= longeur <=taille)
    #est-ce que les lettres sont adjacentes ? (on evalu cela sur la chaine letter_list passée en paramètre)
    #validité = True

    return #validité

def valeur(validité) :                                              #cette fonction retourne le message du resulat après la proposition du joueur
    #validité est vraie?
        #est-ce que le mot existe ?
            #valeur = 'ok'
        #sinon
            #valeur = 'rejete'
    #sinon
            #valeur = 'illegal'
    
    return #valeur

def affichage(word, point, valeur):

    point_affiche = '(' +str(point) + ')' 
    valeur_affiche = "-- " + valeur                                 #valeur est l'issu du mot (rejété ou illegal) retourné par une fonction qui test si le mot existe           
    exit_text = [word, point_affiche, valeur_affiche] 
    print(exit_text)
    return

def calcul_point(grille, mot):                                      #cette fonction retourne le nombre de point pour chaque mots, en fontion de leur longueur
    if len(mot) <= 3:
        point = 1

    if len(mot) >= 4:
        point = 2

    if len(mot) <= 5:
        point = 3

    if len(mot) >= 6:
        point = 5

    return point

def max_points(score, joueurs):

    max_point = score[1]                                              #de base, on pose le meilleur score comme étant celui du premier joueur

    for current_point in range (1,joueurs*2, 2):                      #les différents points sont écris en position impaires dans la liste "score"

        if score[current_point] > max_point :                         #on compare les points pour avoir le plus grand
            max_point = score[current_point]

    player = score[current_point-1]                                   #le nom du joueur est écris juste avant ses points, dans la liste "score"

    return max_point, player

def lettre (alphabet, longeur):                                       #cette fonction retourne une lettre aléatoire de la chaine passée en paramètre
    rand = True
    while rand:                                                       #on veut aumoins une valeur de position inférieure à la longeur de la chaine
        position = int(10*random.random())
        if position < longeur:
            rand = False

    if position < (longeur//2):                                       #pour pouvoir couvrir l'autre moitié de la chaine
        position += position

    letter = alphabet[position]
    return letter


def generer_des(taille):
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
    return Dés

def generer_grille(taille, Dés):

    seperator = "-"*((taille*4) +1) 

    start = 0                                                       #the first line is made up of random letters from the first dices
    end = taille
    spot = []                                                       #the set of coordinates of every letter on the grid

    letter_list = ""

    for ligne in range(taille):                                     #les lignes de la grille
        word = ""                                                   #la chaine qui sera imprimée pour chaque ligne     

        for colonne in range (start, end):                          #les colonnes de la grille
            D = Dés[colonne] 

            letter = lettre(D,4)                                    #choisir un caractère aléatoire du dé encours
            letter_list += letter
            
            spot.append(colonne)  #current_spot

            if colonne == start:                                    #pour la prmière colonne de chaque lignes
                word += "| " + letter

            else:
                word += " | " + letter

        print (seperator)
        print (word,'|')
        start = start + taille
        end = start + taille                                        #we go to the next dices for following lines
        
    print (seperator)
    return letter_list, Dés

def jouer():
    taille = int(input('Entrer le nombre de lignes souhaité: '))
    nombre_parties = int(input('Combien de parties souhaitez vous jouer ? '))
    manches = input('En combien de manches souhaitex vous jouer ? ')
    joueurs = int(input('Combien de joueurs sont présents ? '))

    
    total_points = 0

    for partie in range(nombre_parties): 
        score = []
        if partie == 0:
            Dés = generer_des(taille)                                           #pour les prochaine parties, les dés ne doivent pas etre changés

        print('Partie', partie+1)
        print(" ")                                    
        generer_grille(taille, Dés)                                             #pour une nouvelle partie, les dés précédents ne sont pas changés mais la grille est modifiée
        print(" ")

        for manche in range(manches):
            x = 1

            for player in range(joueurs):                                       #itere sur tous les joueurs présents
                player_name = "Joueur" + str(player + 1 )
                print(player_name)

                for chances in range(6):                                        #itere sue les différentes tentatives pour chaque joueur
                    p_word = input('Proposer un mot: ')
                    point = 0
                    letter_list = generer_grille[0]

                    #validité = est_valide(grille, lettre_1, lettre_2) :        #on veut savoir si le mot propossé est valide ou pas

                    #if validité : 
                    #    point = calcul_point(letter_list, p_word)

                    #message = valeur(validité)

                    #affichage(p_word, point, valeur)
                    total_points += point

                if manche == 0 :
                    score.append(player_name)                                   #this list stores both the player names and the total number of points, for further uses
                    score.append(total_points)
                else:
                    score[player + x] += total_points                           #the total number of points of the current player in the list "score"
                    x += 1

                print(player_name, 'Score: ', total_points )

    meilleur_score  = max_points(score, joueurs)[0]
    meilleur_joueur = max_points(score, joueurs)[1]

    print("Le meilleur joueur est", meilleur_joueur, "avec un score de: ", meilleur_score)
        
    return 
jouer()

def test():

    pass

test()

