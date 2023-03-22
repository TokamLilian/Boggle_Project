#Sarah Jolia Enombo Ngosso
#Ange Lilian Tchomtchoua Tokam

#Boggle.py qui simulte le jeux de boggle à plusieurs joueurs

import random


def appearance(lettre, mot):                                                        #cette fonction retourne le nombre de fois qu'une lettre est dans le mot
    lettre_m = lettre
    new_mot = ""
    appear = 0
    for rem in mot:
        if lettre_m == rem:
            appear += 1
            continue
        else:
            new_mot += rem                                                          #le nombre de fois qu'il y a une lettre dans le mot est le nombre
    return appear                                                                   #de fois qu'on ecrira les differentes positions de cette lettre


def dans_grille(grille, mot):                                                       #verifie si toutes les lettres du mot propose sont dans la grille
    position_matrix = []                                                            #contient toutes les positions où on trouve les lettres du mots propose, dans la grille
    found = 0                                                                       #le nombre de lettre trouvees
    letter_position = 0

    taille = len(grille)**2

    for lettre_m in mot:                                                            #on cherche si toutes les lettres du mot propose sont dans la grille
        appear = appearance(lettre_m, mot)                                          #est-ce qu'il y a des lettre qui se repentent dans le mot?                
        grid_position = 0                                                           #la position de la lettre dans la grille
        lettre_g = ""

        for row_g in grille:   

            for lettre_g in row_g:
                if lettre_m == lettre_g:
                    
                    if grid_position in position_matrix:                           #si on a déjà trouvé cette lettre à la meme position, on va la chercher dans une autre position de la grille
                        grid_position += 1
                        continue

                    if grid_position%(taille-1) == 0 and appear >= 2:
                        length_position_matrix = len(position_matrix) + appear              #la taille de la liste qui contient les positions de la lettre egale au nombre de fois qu'il y a la lettre
                    else: 
                        length_position_matrix = len(position_matrix)

                    #if (letter_position+1) == length_position_matrix or grid_position%length_position_matrix == 0 :               #si on a déjà inscrit la première position de la lettre trouvée ou si la lettre est encore presente ailleurs sur la meme ligne
                    #if grid_position%(taille-1) == 0 and appear >= 2:                                                             #ceci traite le cas d'une lettre qui est au moins deux fois dans le meme mot et au moins deux fois sur la meme ligne de la grille

                    if (letter_position+1) == length_position_matrix  or (grid_position%(taille-1) == 0 and appear >= 2) :            #on jumelle les deux conditions ci-dessus
                        element = position_matrix[letter_position]                          #on va à l'endroit où les indices de la lettre sont écrits, pour pouvoir ajouter les nouvelles indices

                        if type(element) == int:                                            #pour la premiere position de la lettre
                            element = [element, grid_position]                           #on note les positions de cette lettre
                        else:
                            element.append(grid_position)

                        position_matrix[letter_position] = element                          #on ecrit les positions où se trouve la lettre

                    else:
                        found += 1
                        position_matrix.append(grid_position)

                        if found == len(mot) and grid_position >= len(grille)**2 :           #si a toutes les lettres proposes figurent dans la grille, alors le mot est present
                            return position_matrix                                           #on sait que len(position_matrix) == len(mot)
                
                    grid_position += 1

                else: grid_position += 1                                                           #lorsqu'on passe a la prochaine lettre sur la grille

                if letter_position > len(mot) + 1 and found < len(mot):                      #si on est à la dernière lettre du mot
                                                                                             #et toutes les lettres proposees n'ont pas ete trouvees, alors on s'arrete
                    return False
                
                if grid_position >= (len(grille)**2) and found == len(mot):                   #si on est à la dernière lettre de la grille et on a trouvé toutes les lettres du mot dans la grille
                    return position_matrix

        letter_position += 1


#may be a useful shortcut for get_neighboor: whenever we find a neighboor of lettre_1 which is adjacetn to lettre_2 that is
#index_i == letter_indices[1], then we can stop

def get_neighboor(grille, letter_position):                                                  #cette fonction retourne une liste des lettres adjacentes a la lettre passée en paramètre

    adjacent_indices = []                                                                    #contient les indices où se trouvent les lettres adjacentes

    taille = len(grille)
    nb_des = taille ** 2

    spot = taille - 1

    #cherchons les colonnes extremes gauches et droites
    if letter_position%taille == 0 or letter_position%(taille) == spot:

        #cherchons les coins
        if letter_position//taille == 0 or letter_position//taille == spot:

            if letter_position == 0 or letter_position == spot:                         #prendre l'indice situé en dessous
                adjacent_indices.append(letter_position + taille)
            
                if letter_position == 0 :                                               #le premier coin sur une grille
                    adjacent_indices.append(letter_position + taille + 1)               #prendre l'indice situé à la diagonale basse droite

                if letter_position == spot:                                             #le deuxieme coin sur une grille
                    adjacent_indices.append(letter_position * 2)                        #prendre l'indice situé à la diagonale basse gauche

            if letter_position == 0 or letter_position == (taille*spot):                
                adjacent_indices.append(letter_position + 1)                            #prendre l'indice situé à la droite

            if letter_position == (taille*spot) or letter_position == (nb_des-1):       #le troisieme coin sur une grille ou le quatrieme coin sur une grille
                adjacent_indices.append(letter_position - taille)                       #prendre l'indice situé au dessus   

                if letter_position == (taille*spot):
                    adjacent_indices.append(letter_position - spot)                     #prendre l'indice situé à la diagonale haute droite   

            if letter_position == spot or letter_position == (nb_des -1):
                adjacent_indices.append(letter_position - 1)                            #prendre l'indice situé à la gauche   

                if letter_position == (nb_des - 1):
                    adjacent_indices.append(letter_position - taille - 1)               #prendre l'indice situé à la diagonale haute gauche                                                                   
            
        #cherchons les elements restants de la colonne
        else:
                                                      
            index1 = letter_position - taille                                            #prendre l'indice situé au dessus
            index4 = letter_position + taille                                            #prendre l'indice situé en dessous

            if letter_position%taille == 0:                                                  #pour les indices de la première colonne
                index2 = index1 + 1                                                          #prendre l'indice situé à la diagonale haute droite
                index3 = letter_position + 1                                                 #prendre l'indice situé à droite
                index5 = index4 + 1                                                          #prendre l'indice situé à la diagonale basse droite
                adjacent_indices = [index1, index2, index3, index4, index5]

            else:                                                                            #pour les indices de la dernière colonne
                index2 = index1 - 1                                                          #prendre l'indice situé à la diagonale haute gauche
                index3 = letter_position - 1                                                 #prendre l'indice situé à gauche
                index5 = index4 - 1                                                          #prendre l'indice situé à la diagonale basse gauche
                adjacent_indices = [index2, index1, index3, index5, index4]

    #cherchons les elements restants de la ligne
    else:

        #cherchons ce qui est au centre de la grille (pas sur la derniere ni premiere ligne)  
        if letter_position > taille and letter_position < (nb_des) - spot:
            index1 = letter_position - taille                                            #prendre l'indice situé au dessus
            index2 = letter_position + taille                                            #prendre l'indice situé en dessous
            index3 = letter_position - 1                                                 #prendre l'indice situé à gauche
            index4 = letter_position + 1                                                 #prendre l'indice situé à droite

            index5 = index1 - 1                                                          #prendre l'indice situé à la diagonale haute gauche
            index6 = index1 + 1                                                          #prendre l'indice situé à la diagonale haute droite

            index7 = index2 - 1                                                          #prendre l'indice situé à la diagonale basse gauche
            index8 = index2 + 1                                                          #prendre l'indice situé à la diagonale basse droite

            adjacent_indices = [ index1, index2, index3, index4, index5, index6, index7, index8 ]
            return adjacent_indices 
        
        #cherchons ce qui est au milieu de la ligne') 
        else: 
            index1 = letter_position - 1                                                 #prendre l'indice situé à gauche
            index2 = letter_position + 1                                                 #prendre l'indice situé à droite

            if letter_position < taille:                                                 #pour la première ligne de la grille
                index3 = letter_position + taille                                        #prendre l'indice situé en dessous
                index4 = index3 - 1                                                      #prendre l'indice situé à la diagonale basse gauche
                index5 = index3 + 1                                                      #prendre l'indice situé à la diagonale basse droite

            else:                                                                        #pour la toute dernière ligne
                index3 = letter_position - taille                                        #prendre l'indice situé au dessus
                index4 = index3 - 1                                                      #prendre l'indice situé à la diagonale haute gauche
                index5 = index3 + 1                                                      #prendre l'indice situé à la diagonale haute droite

        adjacent_indices = [ index1, index2, index3, index4, index5 ]        
    
    return adjacent_indices


def est_adjacente(grille, letter_indices):

    #est-ce que les lettre1 et lettre_2 sont adjacentes ?
    
    neighboor = get_neighboor(grille, letter_indices[0])                                #on va chercher les toutes les lettres adjacentes à lettre_1

    for position in neighboor:                                                          #on se sert de la liste qui contiendra les index adjacents à l'index de la lettre 1

        if type (letter_indices[1]) == int:                                             #dans le cas où a la lettre deux n'apparait qu'une seule fois dans la grille

            if position == letter_indices[1]:                                           #on verifie si l'index de la lettre 2 est parmi les index adjacents à l'index de la lettre 1
                return position                                                         #ainsi on trouvera que l'index de la lettre 2 est adjacent à l'index de la lettre 1

        else:
            for index in letter_indices[1]:                                             #il se pourrait que la lettre 2 apparaisse plus d'une fois dans la grille, alors on verifie
                if position == index:                                                   #si aumoins une de ses positions est adjacente à l'indice de la lettre 1, 
                    return position                                                     #on retourne l'index de cette position pour la prochaine verification
                
    return False                                                                        #si il n'y a pas l'index de la lettre 2 au bout des indices adjacents à l'index de la lettre 1
                                                                                        #alors les deux lettres ne sont pas adjacentes dans la grille


def verification(grille, position_matrix, word):                                        #cette fonction appel le teste pour deux lettres consecutives du mot propose

    lettres = [ None, None ]
    first = 0
    last = 2
    adjacence = False

    while last <= len(word):
        j = 0
        letter_indices = []

        for i in range (first, last): 
            lettres [j] = word[i]                                               #on ecrit deux les lettre consecutives du mot dans une liste pour les appels de la fonction est_adjacente

            if first > 0 and adjacence != False:                                #si on est déjà au moins à la deuxième lettre du mot, et on sait
                letter_indices = [adjacence, position_matrix[i]]                #déjà la position de lettre 1 adjacente à lettre 2, on verifie juste si la 
                                                                                #prochaine lettre sera ajacente à cette position là

            else: letter_indices.append(position_matrix[i])
            j += 1    

        lettre_1 = lettres[0]
        lettre_2 = lettres[1]

        first += 1 
        last += 1

        if type (letter_indices[0]) != int:
            
            for position in range (len(letter_indices[0])):
                if adjacence == False:
                    letter_index = [ letter_indices[0][position], letter_indices[1] ]               #on cherche à quelle position de la lettre 1 est-ce que la lettre2 est adjacente
                    adjacence = est_adjacente(grille, letter_index)

                else:                                                                               #aussi tot qu'on trouve une position de la lettre 1 adjacentte à la lettre 2
                    return True                                                                #on retourne la position de lettre 1 adjacente à lettre 2

            if adjacence == False:                          
                return False                                                                            #si la lettre 2 n'est adjacente à aucune position de la lettre 1, on s'arrete                                                  
            
            else: 
                return True

        else:
            #if not est_adjacente(grille, letter_indices):
            adjacence = est_adjacente(grille, letter_indices)

            if adjacence == False:
                return False                                                                        #si les deux lettres ne sont pas adjacentes, on s'arrete
                                                                                                    #sinon, on continue de verifier si la prochaine est adjacente aussi
    return True


def valeur(validite) :                                                                          #cette fonction retourne le message du resulat après la proposition du joueur
    if validite :
        #est-ce que le mot existe ?
            valeur = 'ok'
        #sinon
            #valeur = 'rejete'
    else:
            valeur = 'illegal'
    
    return valeur


def affichage(word, point, valeur):

    point_affiche = ' (' +str(point) + ')' 
    valeur_affiche = " -- " + str(valeur)                                   #valeur est l'issu du mot (rejete ou illegal) retourne par une fonction qui test si le mot existe           
    #exit_text = [word, point_affiche, valeur_affiche] 
    exit_text = str(word) + str(point_affiche) + str(valeur_affiche)
    return exit_text


def calcul_point(taille, mot):                                           #cette fonction retourne le nombre de point pour chaque mots, en fontion de leur longueur
    pts = 0

    if (taille**2) > 25 and len(mot) >= 7:                               #pour les grilles de taille 6x6 et plus, à partir d'une longeur de 7, les points sont attribues differenments
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

    for partie in range(nombre_parties): 
        score = []
        if partie == 0:                                                         #and taille >= 6 : pour generer les des des grilles de taille 6 en montant, 
                                                                                #car pour les grilles de taille inferieures à 6, l'enoncé a fourni les dés

            Des = generer_des(taille)                                           #pour les prochaine parties, les des ne doivent pas etre changes

        print('Partie', partie+1)
        print(" ")   

        grille = generer_grille(taille, Des)                                    #pour toutes les parties, on a une nouvelle grille      
        print(grille)                                                           #just for further debugging
        dessiner_grille(taille, grille) 

        for manche in range(manches):
            total_points = 0
            x = 1                                                               #nous permettra de stocker au meme endroit les points d'un jouer pour une toutes les parties

            for player in range(joueurs):                                       #itere sur tous les joueurs presents
                total_points = 0
                player_name = "Joueur" + str(player + 1 )
                print(player_name)
                print(" ") 

                for chances in range(10):                                        #itere sur les differentes tentatives pour chaque joueur
                    p_word = input('Proposer un mot: ')
                    point = 0

                    if p_word == " " or p_word == "":                            #les essais s'arretent s'il n'y a aucune entree
                        break

                    else:
                        #validite = False
                        validite = True

                        if len(p_word) >= 3 and len(p_word) <= (taille**2) :                         #est-ce que le mot est de la bonne taille ? (3<= longeur <=taille**2)

                            #present = dans_grille(grille, p_word)                                    #est-ce qut toutes les lettres du mot propose sont sur la grille ?
                            
                            #if present != False :
                            #    validite = verification(grille, present, p_word)                     #on veut savoir si le mot proposse est valide ou pas

                            if validite : 
                                point = calcul_point(taille, p_word)                                 #si le mot est valide, alors on calcul le nombre de points correspondants

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
                print("")

    meilleur_score  = max_points(score, joueurs)[0]
    meilleur_joueur = max_points(score, joueurs)[1]

    print("Le meilleur joueur est", meilleur_joueur, "avec un score de: ", meilleur_score)
        
    return 


#jouer()