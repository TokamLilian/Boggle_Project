#Sarah Jolia Enombo Ngosso
#Ange Lilian Tchomtchoua Tokam

#Boggle.py qui simulte le jeux de boggle à plusieurs joueurs
import random

def dans_grille(grille, mot):                               #verifie si toutes les lettre du mot propose sont dans la grille
    position_matrix = []                                    #contient toutes les positions où on trouve les lettre du mots propose, dans la grille
    found = 0                                               #le nombre de lettre trouvees

    for lettre_m in mot:                                    #on cherche si toutes les lettres du mot propose sont dans la grille
        grid_position = 0                                   #la position de la lettre dans la grille

        for lettre_g in grille:

            if lettre_m == lettre_g:
                found += 1
                position_matrix.append(grid_position)
                break

            grid_position += 1

            if grid_position == len(grille) - 1:            #si on est à la dernière lettre de la grille et toutes les lettres proposees n'ont pas ete 
                if found < len(mot):                        #trouves, alors on s'arrete
                    return False

            if found == len(mot):                           #si a toutes les lettres proposes figurent dans la grille, alors le mot est present
                return position_matrix
            
def get_neighboor(grille, lettre):
    neighboor = ""

    #trouver la position de la lettre sur la grille

    #les lettres de la premiere colonne 
    #position%taille = 0

    #les lettres de la deuxieme colonne 
    #position%taille = 1

    #les lettres de la troisieme colonne 
    #position%taille = 2

    #les lettres de la derniere colonne 
    #position%taille = taille-1

    return neighboor


def verification(grille, word):                                                 #cette fonction appel le teste pour deux lettres consecutives du mot propose

    lettres = [ None, None ]
    start = 0
    end = 2

    while end <= len(word):
        j = 0

        for i in range (start, end): 

            lettres [j] = word[i]
            j += 1    

        lettre_1 = lettres[0]
        lettre_2 = lettres[1]

        start += 1 
        end += 1

        if not est_adjacente(grille, lettre_1, lettre_2):
            return False
        
    
    return True


def est_adjacente(grille, lettre_1, lettre_2):

    #est-ce que les lettre! et lettre_2 sont adjacentes ?
    
    neighboor = get_neighboor(grille, lettre_1)
    #neighboor = [ 'F', 'A', ' G' ]                 #for debugging
    position = 0
    
    for sample in neighboor:
        position += 1

        if lettre_2 == sample:
            return True
        if position == len(neighboor):
            return False


def valeur(validite) :                                              #cette fonction retourne le message du resulat après la proposition du joueur
    #if validite :
        #est-ce que le mot existe ?
            #valeur = 'ok'
        #sinon
            #valeur = 'rejete'
    #else:
            #valeur = 'illegal'
    
    return #valeur


def affichage(word, point, valeur):

    point_affiche = '(' +str(point) + ')' 
    valeur_affiche = "-- " + valeur                                      #valeur est l'issu du mot (rejete ou illegal) retourne par une fonction qui test si le mot existe           
    exit_text = [word, point_affiche, valeur_affiche] 
    return exit_text


def calcul_point(letter_list, mot):                                      #cette fonction retourne le nombre de point pour chaque mots, en fontion de leur longueur
    pts = 0

    if len(letter_list) > 25 and len(mot) >= 7:                          #pour les grilles de taille 6x6 et plus, à partir d'une longeur de 7, les points sont attribues differenments
        pts += 7
            
        for longeur in range (7,9):                                      #on traitera uniquement la longeur 7 et 9 car pour les longeurs <7, l'attribution de points est la 
                                                                         #meme que pour une grille de taille 4x4 
            if len(mot) >= 9:                                                         
                point = 12                                               #pour cette grille, à partir d'une longeur 9, on a 12 points
                return point
            
            if len(mot) == longeur:
                point = pts
                return point
            else:
                pts += 3                                                 #pour un mot de taille 8, on a 10 points

    if len(mot) >= 8:
        point = 10                                                       #pour toutes les grilles de taille 5x5 en decendant, un mot de taille 8 donne 10 points 
        return point
    
    
    if len(letter_list) == 25 and len(mot) >= 6:                         #pour la grille de taille 5x5 à partir d'une longeur de 6, les points sont attribues differenments
        pts += 4
            
        for longeur in range (6,8):                                      #on traitera uniquement la longeur 6 et 7 car pour les longeurs < 6, l'attribution de points est la 
                                                                         #meme que pour une grille de taille 4x4
            if len(mot) == longeur:
                point = pts
                return point
            else:
                pts += 2                                                 #pour un mot de taille 7, on a 6 points

    else:                                                                #pour les grilles inferieures ou egales à la taille 4x4 ainsi que les mots de longeur 
        for longeur in range (3,10):                                     #inferieures à 6
            if longeur <=  5:
                pts += 1
            if longeur == 6:
                pts += 2
            if longeur == 7:
                pts += 3
            if len(mot) == longeur:
                point = pts

                return point 
            

def max_points(score, joueurs):

    max_point = score[1]                                              #de base, on pose le meilleur score comme etant celui du premier joueur

    for current_point in range (1,joueurs*2, 2):                      #les differents points sont ecris en position impaires dans la liste "score"

        if score[current_point] > max_point :                         #on compare les points pour avoir le plus grand
            max_point = score[current_point]

    player = score[current_point-1]                                   #le nom du joueur est ecris juste avant ses points, dans la liste "score"

    return max_point, player


def lettre (alphabet, longeur):                                       #cette fonction retourne une lettre aleatoire de la chaine passee en paramètre
    rand = True
    while rand:                                                       #on veut aumoins une valeur de position inferieure à la longeur de la chaine
        
        position = int(30*random.random())                            #pour pouvoir couvrir l'autre moitie de la chaine
        if position < longeur:
            rand = False

    letter = alphabet[position]
    return letter


def generer_des(taille):
    #on va faire des structures pour les differents des et l'affichage aleatoires des elements pour chaque de
    
    alphabet = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    Des = []                                                        #la liste de tous les des de la partie

    nombre_de = taille **2                                          #le nombre total de des presents

    for _ in range(nombre_de):                                      #ittere sur les differents des
        de = []

        for face in range (6):                                      #ittere sur les differentes six faces du de
            de.append(lettre(alphabet, 26))                         #chaque face egale à une lettre aleatoire

        Des.append(de)

    return Des


def dessiner_grille (taille, Des):

    seperator = "-"* ((taille*4) +1) 

    start = 0                                                       #the first line is made up of random letters from the first dices
    end = taille
    spot = []                                                       #the set of coordinates of every letter on the grid

    letter_list = []

    for ligne in range(taille):                                     #les lignes de la grille
        word = ""                                                   #la chaine qui sera imprimee pour chaque ligne     

        for colonne in range (start, end):                          #les colonnes de la grille
            D = Des[colonne] 

            letter = lettre(D,6)                                    #choisir un caractère aleatoire dans le de encours
            #letter_list += letter                                  #we use this if we want to use letter_list = ""
            letter_list.append(letter)
            
            spot.append(colonne)                                    #current_spot

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


def generer_grille(taille, letter_list):            
    grille = [None] * taille

    for i in range (taille):
        grille[i] = [None] * taille                                 #creation de la grille

    for j in range (len(letter_list)):                              #parcourir tous les elements de la liste

        row = j // taille                                           #division par la largeur de la grille pour avoir le numero de la ligne

        col = j % taille                                            #le reste de la division de la position de la lettre et la taille de la grille, donne le numero de la colonne

        grille[row][col] = letter_list[j]

    return grille


def jouer():
    taille = int(input('Entrer le nombre de lignes souhaite: '))
    nombre_parties = int(input('Combien de parties souhaitez vous jouer ? '))
    manches = int(input('En combien de manches souhaitez vous jouer ? '))
    joueurs = int(input('Combien de joueurs sont presents ? '))

    total_points = 0

    for partie in range(nombre_parties): 
        score = []
        if partie == 0:
            Des = generer_des(taille)                                           #pour les prochaine parties, les des ne doivent pas etre changes

        print('Partie', partie+1)
        print(" ")                                    

        for manche in range(manches):
            x = 1                                                               #nous permettra de stocker au meme endroit les points d'un jouer pour une toutes les parties

            for player in range(joueurs):                                       #itere sur tous les joueurs presents
                player_name = "Joueur" + str(player + 1 )
                print(player_name)

                for chances in range(6):                                        #itere sue les differentes tentatives pour chaque joueur
                    p_word = input('Proposer un mot: ')
                    point = 0

                    if p_word == " " or p_word == "":                           #les essais s'arretent s'il n'y a aucune entree
                        break

                    else:
                        letter_list = dessiner_grille(taille, Des)              #pour une nouvelle partie, les des precedents ne sont pas changes mais la grille est modifiee
                        grille = generer_grille(taille, letter_list)
                        validite = False

                        if len(p_word) >= 3:                                                    #est-ce que le mot est de la bonne taille ? (3<= longeur <=taille)

                            present = dans_grille(letter_list, p_word)                          #est-ce qut toutes les lettres du mot propose sont sur la grille ?
                            if present != 'False':
                                validite = verification(grille, p_word)                         #on veut savoir si le mot proposse est valide ou pas
                                pass

                            if validite : 
                                point = calcul_point(letter_list, p_word)                           #si le mot est valide, alors on calcul le nombre de points correspondants

                        message = valeur(validite)

                        print(affichage(p_word, point, message))
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


#jouer()
