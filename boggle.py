#Sarah Jolia Enombo Ngosso
#Ange Lilian Tchomtchoua Tokam

#Boggle.py qui simulte le jeux de boggle à plusieurs joueurs
import random

def dans_grille(grille, mot):                               #verifie si toutes les lettre du mot proposé sont dans la grille
    position_matrix = []                                    #contient toutes les positions où on se trouve les lettre du mots proposé, dans la grille
    found = 0                                               #le nombre de lettre trouvées

    for lettre_m in mot:                                    #on cherche si toutes les lettres du mot proposé sont dans la grille
        grid_position = 0                                   #la position de la lettre dans la grille

        for lettre_g in grille:

            if lettre_m == lettre_g:
                found += 1
                position_matrix.append(grid_position)
                break

            grid_position += 1

            if grid_position == len(grille) - 1:            #si on est à la dernière lettre de la grille et toutes les lettres proposées n'ont pas été 
                if found < len(mot):                        #trouvés, alors on s'arrete
                    return False

            if found == len(mot):                           #si a toutes les lettres proposés figurent dans la grille, alors le mot est présent
                return position_matrix

    #print(position_matrix)

def est_valide(grille, lettre_1, lettre_2):

    #est-ce que les lettres sont adjacentes ? (on evalu cela sur la chaine letter_list passée en paramètre)
    
    #trouver la position de la lettre sur la grille

    #les lettres de la premiere colonne 
    #position%taille = 0

    #les lettres de la deuxieme colonne 
    #position%taille = 1

    #les lettres de la troisieme colonne 
    #position%taille = 2

    #les lettres de la derniere colonne 
    #position%taille = taille-1    




    validité = True

    return validité

def valeur(validité) :                                              #cette fonction retourne le message du resulat après la proposition du joueur
    #if validité :
        #est-ce que le mot existe ?
            #valeur = 'ok'
        #sinon
            #valeur = 'rejete'
    #else:
            #valeur = 'illegal'
    
    return #valeur

def affichage(word, point, valeur):

    point_affiche = '(' +str(point) + ')' 
    valeur_affiche = "-- " + valeur                                 #valeur est l'issu du mot (rejété ou illegal) retourné par une fonction qui test si le mot existe           
    exit_text = [word, point_affiche, valeur_affiche] 
    print(exit_text)
    return

def calcul_point(grille, mot):                                      #cette fonction retourne le nombre de point pour chaque mots, en fontion de leur longueur
    if len(mot) == 3:
        point = 1

    if len(mot) == 4:
        point = 2

    if len(mot) == 5:
        point = 3

    if len(mot) == 6:
        point = 5

    return point
#score = ['jouer1', '13', 'joueur2', '15', 'jouer3', '13', 'joueur4', '15', 'jouer5', '13', 'joueur6', '15'] 

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
        
        position = int(30*random.random())                            #pour pouvoir couvrir l'autre moitié de la chaine
        if position < longeur:
            rand = False

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
    return letter_list

def jouer():
    taille = int(input('Entrer le nombre de lignes souhaité: '))
    nombre_parties = int(input('Combien de parties souhaitez vous jouer ? '))
    manches = int(input('En combien de manches souhaitez vous jouer ? '))
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

                    if p_word == " " or p_word == "":                           #les essais s'arretent s'il n'y a aucune entrée
                        break

                    else:
                        letter_list = generer_grille
                        validité = False

                        if len(p_word) >= 3:                                                    #est-ce que le mot est de la bonne taille ? (3<= longeur <=taille)

                            present = dans_grille(letter_list, p_word)                          #est-ce qut toutes les lettres du mot proposé sont sur la grille ?
                            if present != 'False':
                                validité = est_valide(letter_list, lettre_1, lettre_2)          #on veut savoir si le mot propossé est valide ou pas

                        #if validité : 
                        #    point = calcul_point(letter_list, p_word)

                        #message = valeur(validité)

                        #affichage(p_word, point, message)
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


#une grille 4x4
#-----------------
#| C | Q | D | J |
#-----------------
#| A | A | E | K |
#-----------------
#| I | K | S | V |
#-----------------
#| J | T | F | U |
#-----------------

#grille = 'CQDJAAEKIKSVJTFU'
#positi = '0'1'2'3'4'5'6'7'8'9'10'11'12'13'14'15'

#p_word = 'CAST'

#present = dans_grille(grille, p_word)
