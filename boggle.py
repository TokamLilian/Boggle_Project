#Sarah Jolia Enombo Ngosso
#Ange Lilian Tchomtchoua Tokam

#Boggle.py qui simulte le jeux de boggle à plusieurs joueurs
import random

def dans_grille(grille, mot):                                        #verifie si toutes les lettres du mot propose sont dans la grille
    position_matrix = []                                             #contient toutes les positions où on trouve les lettre du mots propose, dans la grille
    found = 0                                                        #le nombre de lettre trouvees

    for lettre_m in mot:                                             #on cherche si toutes les lettres du mot propose sont dans la grille
        grid_position = 0                                            #la position de la lettre dans la grille
        lettre_g = ""

        for row_g in grille:
           if lettre_g == lettre_m:                                  #on veut s'assurer qu'on ne cherche pas une lettre qui a déjà été trouvée
               break
           
           for lettre_g in row_g:
                if lettre_m == lettre_g:
                    
                    if grid_position in position_matrix:            #si on a déjà trouvé cette lettre à la meme position, on va la chercher dans une autre position de la grille
                        grid_position += 1
                        continue
                    else:
                        found += 1
                        position_matrix.append(grid_position)
                        grid_position += 1

                        if found == len(mot):                                #si a toutes les lettres proposes figurent dans la grille, alors le mot est present
                            return position_matrix                           #on sait que len(position_matrix) == len(mot)
                        
                        break

                if grid_position == (len(grille)**2) - 1:            #si on est à la dernière lettre de la grille et toutes les lettres proposees n'ont pas ete 
                    if found < len(mot):                             #trouvees, alors on s'arrete
                        return False
                
                grid_position += 1                                   #lorsqu'on passe a la prochaine lettre
    return False                                                     #pour tout cas où au moins une lettre du mot n'a pas été trouvée dans la grille


def get_neighboor(grille, lettre):                                   #cette fonction retourne une liste des lettres adjacentes a la lettre passée en paramètre
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
    first = 0
    last = 2

    while last <= len(word):
        j = 0

        for i in range (first, last): 

            lettres [j] = word[i]
            j += 1    

        lettre_1 = lettres[0]
        lettre_2 = lettres[1]

        first += 1 
        last += 1

        if not est_adjacente(grille, lettre_1, lettre_2):
            return False
        
    
    return True


def est_adjacente(grille, lettre_1, lettre_2):

    #est-ce que les lettre! et lettre_2 sont adjacentes ?
    
    neighboor = get_neighboor(grille, lettre_1)
    #neighboor = [ 'F', 'A', ' G' ]                 #for debugging
    position = 0
    return True                                     #JUST for hot debigging

    for sample in neighboor:
        position += 1

        if lettre_2 == sample:
            return True
        if position == len(neighboor):
            return False


def valeur(validite) :                                              #cette fonction retourne le message du resulat après la proposition du joueur
    if validite :
        #est-ce que le mot existe ?
            valeur = 'ok'
        #sinon
            #valeur = 'rejete'
    else:
            valeur = 'illegal'
    
    return valeur


def affichage(word, point, valeur):

    point_affiche = '(' +str(point) + ')' 
    valeur_affiche = "-- " + str(valeur)                                   #valeur est l'issu du mot (rejete ou illegal) retourne par une fonction qui test si le mot existe           
    exit_text = [word, point_affiche, valeur_affiche] 
    return exit_text


def calcul_point(taille, mot):                                      #cette fonction retourne le nombre de point pour chaque mots, en fontion de leur longueur
    pts = 0

    if (taille**2) > 25 and len(mot) >= 7:                          #pour les grilles de taille 6x6 et plus, à partir d'une longeur de 7, les points sont attribues differenments
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
    
    if (taille**2) == 25 and len(mot) >= 6:                              #pour la grille de taille 5x5 à partir d'une longeur de 6, les points sont attribues differenments
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


def lettre (alphabet):                                                #cette fonction retourne une lettre aleatoire de la chaine passee en paramètre
    longeur = len(alphabet)
    position = int(longeur*random.random())                           #une position aleatoire sur la longueur de la chaine passée en paramètre

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
            de.append(lettre(alphabet))                             #chaque face egale à une lettre aleatoire

        Des.append(de)

    return Des


def generer_grille(taille, Des):
    grille = [None] * taille                                        #les lignes de la grille

    for i in range (taille):                                        #les colonnes de chaques lignes
        grille[i] = [None] * taille                     

    for j in range (taille ** 2 ):                                  #le nombre total de des

        row = j // taille                                           #division par la largeur de la grille pour avoir le numero de la ligne
        col = j % taille                                            #l'indice modulo la taille de grille nous situe sur la colonne

        letter = lettre(Des[j])                                     #pour retourner une lettre aleatoire du jieme Dé et pour le nombre de faces d'un dé

        grille[row][col] = letter

    return grille


def dessiner_grille(taille, grille):
    seperator = "-"* ((taille*4) +1)                                #la ligne separatrice entre les lignes de la grille

    for ligne in range(taille):                                     #les lignes de la grille
        word = "" 

        row = ligne % taille
        
        for colonne in range(taille):

            col = colonne % taille 
            letter = grille[row][col]

            if col == 0:                                            #pour la première colonne de chaque lignes
                word += "| " + letter

            else:
                word += " | " + letter

        print (seperator)
        print (word,'|')

    print(seperator)


def jouer():
    taille = int(input('Entrer le nombre de lignes souhaite: '))
    nombre_parties = int(input('Combien de parties souhaitez vous jouer ? '))
    manches = int(input('En combien de manches souhaitez vous jouer ? '))
    joueurs = int(input('Combien de joueurs sont presents ? '))

    total_points = 0

    for partie in range(nombre_parties): 
        score = []
        if partie == 0:     #and taille >= 6 : pour generer les des des grilles de taille 6 en montant, 
                            #car pour les grilles de taille inferieures à 6, l'enoncé a fourni les dés

            Des = generer_des(taille)                                           #pour les prochaine parties, les des ne doivent pas etre changes

        print('Partie', partie+1)
        print(" ")   

        grille = generer_grille(taille, Des)                                    #pour toutes les parties, on a une nouvelle grille                              
        dessiner_grille(taille, grille) 

        for manche in range(manches):
            x = 1                                                               #nous permettra de stocker au meme endroit les points d'un jouer pour une toutes les parties

            for player in range(joueurs):                                       #itere sur tous les joueurs presents
                player_name = "Joueur" + str(player + 1 )
                print(player_name)
                print(" ") 

                for chances in range(6):                                        #itere sue les differentes tentatives pour chaque joueur
                    p_word = input('Proposer un mot: ')
                    point = 0

                    if p_word == " " or p_word == "":                           #les essais s'arretent s'il n'y a aucune entree
                        break

                    else:
                        validite = False

                        if len(p_word) >= 3:                                                    #est-ce que le mot est de la bonne taille ? (3<= longeur <=taille)

                            present = dans_grille(grille, p_word)                               #est-ce qut toutes les lettres du mot propose sont sur la grille ?
                            if present != False :
                                validite = verification(grille, p_word)                         #on veut savoir si le mot proposse est valide ou pas
                                pass

                            if validite : 
                                point = calcul_point(taille, p_word)                           #si le mot est valide, alors on calcul le nombre de points correspondants

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