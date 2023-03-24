#Sarah Jolia Enombo Ngosso
#Ange Lilian Tchomtchoua Tokam

#Boggle.py qui simulte le jeux de boggle à plusieurs joueurs

import random


def appearance(lettre, mot):                                                                 #cette fonction retourne le nombre de fois qu'une lettre est dans le mot
    lettre_m = lettre
    new_mot = ""
    appear = 0
    for rem in mot:
        if lettre_m == rem:
            appear += 1
            continue
        else:
            new_mot += rem                                                                   #le nombre de fois qu'il y a une lettre dans le mot est le nombre
    return appear                                                                            #de fois qu'on ecrira les differentes positions de cette lettre


def dans_grille(grille, word):                                                               #cette fonction verifie si toutes les lettres du mot propose sont dans la grille
    taille = len(grille)                 
    longueur = len(word)                 
        
    indices_matrix = []                                                                      #contient toutes les positions où on trouve les lettres du mots proposé, dans la grille
    found = 0                                                                                #le nombre de lettre trouvées
        
    for letter_position in range (longueur):                                                 #la position de la lettre dans le mot
        appear = 0                                                                           #le nombre de dois qu'on a trouve la lettre dans la grille
        letter_m = word[letter_position]                                                     #on prend une lettre du mot et a chaque fois on va tester si elle est dans la grille
                
        for line in range (taille):                                                          #itere sur toutes les lignes de la grille
                    
            for column in range(taille):                                                     #itere sur toutes les colonnes de la grille
                    
                letter_g = grille[line][column]                                              #on prend une lettre de la grille a la position (ligne, colonne)
                if letter_g == letter_m:                                                     #et on compare pour savoir si on a trouve une lettre du mot propose
                        
                    appear += 1                                                              #chaque fois qu'on trouve une lettre du mot dans la grille 
                    index = (taille * line) + column                                         #l'indice où est situé la lettre
        
                    if appear > 1:                                                           #si on trouve la lettre plus d'une fois, 
                        element = indices_matrix[letter_position]                            #on doit stocker toutes les positions de la meme lettre au meme en droit
        
                        if type(element) == int:                                             #si on n'a encore que juste une position,
                            element = [element, index]                                       #on la met avec la nouvelle position dans une liste
        
                        else:                                                                #si on a déjà plus d'une position, on ajoute 
                            element.append(index)                                            #la nouvelle position trouvée à la liste les positions de la lettre
                                                                                             
                        indices_matrix[letter_position] = element                            #on note les positions de la lettre 
        
                    else:                
                        found += 1                                                           #pour la première fois qu'on trouve une lettre, 
                        indices_matrix.append(index)                                         #alors on a trouvé une lettre du mot de plus on inscrit sa position
                            
        if letter_position >= len(indices_matrix):                                           #à la fin de la derniere ligne, si on a trouve d'indices que de lettres recherchées
            return False                                                                     #on s'arrete
        
    if letter_position >= (longueur - 1) and found < longueur :                              #si on a parcouru toutes les lettres du mot mais 
        return False                                                                         #on a pas pu trouver toutes les lettres, alors on s'arrete
            
    else:                                                                                    #sinon, lorsqu'on a trouvé toutes les lettres du mot 
        return indices_matrix                                                                #on retourne la matrice des positions des lettres du mot


def get_neighboor(grille, letter_position): 
#cette fonction retourne une liste d'indices adjacentes à l'indice la lettre passée en paramètre                                                 

    adjacent_indices = []                                                                    #contient les indices où se trouvent les lettres adjacentes

    taille = len(grille)
    nb_des = taille ** 2

    spot = taille - 1                                                                        #nous permet d'identifier le coin haut de la dernière colonne

    #cherchons les colonnes extremes gauches et droites
    if letter_position%taille == 0 or letter_position%(taille) == spot:

        #cherchons les coins
        if letter_position//taille == 0 or letter_position//taille == spot:

            if letter_position == 0 or letter_position == spot:                              #prendre l'indice situé en dessous
                adjacent_indices.append(letter_position + taille)    
                 
                if letter_position == 0 :                                                    #le premier coin sur une grille
                    adjacent_indices.append(letter_position + taille + 1)                    #prendre l'indice situé à la diagonale basse droite
     
                if letter_position == spot:                                                  #le deuxieme coin sur une grille
                    adjacent_indices.append(letter_position * 2)                             #prendre l'indice situé à la diagonale basse gauche
     
            if letter_position == 0 or letter_position == (taille*spot):                     
                adjacent_indices.append(letter_position + 1)                                 #prendre l'indice situé à la droite
     
            if letter_position == (taille*spot) or letter_position == (nb_des-1):            #le troisieme coin sur une grille ou le quatrieme coin sur une grille
                adjacent_indices.append(letter_position - taille)                            #prendre l'indice situé au dessus   
     
                if letter_position == (taille*spot):     
                    adjacent_indices.append(letter_position - spot)                          #prendre l'indice situé à la diagonale haute droite   
     
            if letter_position == spot or letter_position == (nb_des -1):    
                adjacent_indices.append(letter_position - 1)                                 #prendre l'indice situé à la gauche   
     
                if letter_position == (nb_des - 1):  
                    adjacent_indices.append(letter_position - taille - 1)                    #prendre l'indice situé à la diagonale haute gauche                                                                   
            
        #cherchons les elements restants de la colonne
        else:
                                                      
            index1 = letter_position - taille                                                #prendre l'indice situé au dessus
            index4 = letter_position + taille                                                #prendre l'indice situé en dessous

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


def lettre_adjacente(grille, letter_indices):

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


#def est_adjacente(grille, position_matrix, word):                                        #cette fonction appel le teste pour deux lettres consecutives du mot propose
def est_adjacente(grille, word):
    indices_matrix = dans_grille(grille, word)
    if not indices_matrix :                                                              #est-ce qut toutes les lettres du mot propose sont sur la grille ?
        return False
    
    lettres = [ None, None ]
    first = 0
    last = 2
    adjacence = False

    while last <= len(word):
        j = 0
        letter_indices = []

        for i in range (first, last):                                                   #on ecrit deux les lettre consecutives du mot dans une liste 
            lettres [j] = word[i]                                                       #pour les appels de la fonction lettre_adjacente
                                                                                        
            if first > 0 and adjacence != False:                                        #si on est déjà au moins à la deuxième lettre du mot, et on sait
                letter_indices = [adjacence, indices_matrix[i]]                         #déjà la position de lettre 1 adjacente à lettre 2, on verifie juste si la 
                                                                                        #prochaine lettre sera ajacente à cette position là

            else: letter_indices.append(indices_matrix[i])
            j += 1    

        lettre_1 = lettres[0]
        lettre_2 = lettres[1]

        first += 1 
        last += 1

        if type (letter_indices[0]) != int:
            
            for position in range (len(letter_indices[0])):
                if adjacence == False:
                    letter_index = [ letter_indices[0][position], letter_indices[1] ]               #on cherche à quelle position de la lettre 1 est-ce que la lettre2 est adjacente
                    adjacence = lettre_adjacente(grille, letter_index)

                else:                                                                               #aussi tot qu'on trouve une position de la lettre 1 adjacentte à la lettre 2
                    return True                                                                     #on retourne la position de lettre 1 adjacente à lettre 2

            if adjacence == False:                          
                return False                                                                        #si la lettre 2 n'est adjacente à aucune position de la lettre 1, on s'arrete                                                  
            
            else: 
                return True

        else:
            adjacence = lettre_adjacente(grille, letter_indices)

            if adjacence == False:
                return False                                                                        #si les deux lettres ne sont pas adjacentes, on s'arrete
                                                                                                    #sinon, on continue de verifier si la prochaine est adjacente aussi
    return True


def affichage(word, point, valeur):

    point_affiche = ' (' +str(point) + ')' 
    valeur_affiche = " -- " + str(valeur)                                #valeur est l'issu du mot (rejete ou illegal) retourne par une fonction qui test si le mot existe           
     
    exit_text = str(word) + str(point_affiche) + str(valeur_affiche)
    return exit_text


def calcul_point(taille, mot):                                           #cette fonction retourne le nombre de point pour chaque mots, en fontion de leur longueur
    pts = 0

    if (taille**2) > 25 and len(mot) >= 7:                               #pour les grilles de taille 6x6 et plus, à partir d'une longueur de 7, 
        pts += 7                                                         #les points sont attribues differenments
            
        for longueur in range (7,9):                                     #on traitera uniquement la longueur 7 et 9 car pour les longeurs <7, l'attribution de points est la 
                                                                         #meme que pour une grille de taille 4x4 
            if len(mot) >= 9:                                                         
                point = 12                                               #pour cette grille, à partir d'une longueur 9, on a 12 points
                return point
            
            if len(mot) == longueur:
                point = pts
                return point
            else:
                pts += 3                                                 #pour un mot de taille 8, on a 10 points

    if len(mot) >= 8:
        point = 10                                                       #pour toutes les grilles de taille 5x5 en decendant, un mot de taille 8 donne 10 points 
        return point
    
    if (taille**2) == 25 and len(mot) >= 6:                              #pour la grille de taille 5x5 à partir d'une longueur de 6, les points sont attribues differenments
        pts += 4
            
        for longueur in range (6,8):                                     #on traitera uniquement la longueur 6 et 7 car pour les longeurs < 6, l'attribution de points est la 
                                                                         #meme que pour une grille de taille 4x4
            if len(mot) == longueur:
                point = pts
                return point
            else:
                pts += 2                                                 #pour un mot de taille 7, on a 6 points

    else:                                                                #pour les grilles inferieures ou egales à la taille 4x4 ainsi que les mots de longueur 
        for longueur in range (3,10):                                    #inferieures à 6
            if longueur <=  5:
                pts += 1
            if longueur == 6:
                pts += 2
            if longueur == 7:
                pts += 3
            if len(mot) == longueur:
                point = pts

                return point 
            

def max_points(score, joueurs):

    max_point = score[1]                                                    #de base, on pose le meilleur score comme etant celui du premier joueur
    
    for current_point in range (1,joueurs*2, 2):                            #les differents points sont ecris en position impaires dans la liste "score"
        
        if score[current_point] >= max_point :                              #on compare les points pour avoir le plus grand ou est au point actuel
            max_point = score[current_point]       
        
            best_player = score[current_point-1]                            #le nom du joueur est ecrit juste avant ses points, dans la liste "score"

    return max_point, best_player


def lettre (alphabet):                                                     #cette fonction retourne une lettre aleatoire de la chaine passee en paramètre
    longueur = len(alphabet)
    position = int(longueur*random.random())                               #une position aleatoire sur la longueur de la chaine passée en paramètre

    letter = alphabet[position]
    return letter


def generer_des(taille):
    #on va faire des structures pour les differents des et l'affichage aleatoires des elements pour chaque de
    
    alphabet = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    Des = []                                                               #la liste de tous les des de la partie
       
    nombre_de = taille **2                                                 #le nombre total de des presents
       
    for _ in range(nombre_de):                                             #ittere sur les differents des
        de = []    
       
        for face in range (6):                                             #ittere sur les differentes six faces du de
            de.append(lettre(alphabet))                                    #chaque face egale à une lettre aleatoire

        Des.append(de)

    return Des


def generer_grille(taille, Des):
    grille = [None] * taille                                               #les lignes de la grille
       
    for i in range (taille):                                               #les colonnes de chaques lignes
        grille[i] = [None] * taille                            
       
    for j in range (taille ** 2 ):                                         #le nombre total de des
           
        row = j // taille                                                  #division par la largeur de la grille pour avoir le numero de la ligne
        col = j % taille                                                   #l'indice modulo la taille de grille nous situe sur la colonne
       
        letter = lettre(Des[j])                                            #pour retourner une lettre aleatoire du jieme Dé et pour le nombre de faces d'un dé

        grille[row][col] = letter

    return grille


def dessiner_grille(taille, grille):
    seperator = "-"* ((taille*4) +1)                                       #la ligne separatrice entre les lignes de la grille

    for ligne in range(taille):                                            #les lignes de la grille
        word = "" 

        row = ligne % taille
        
        for colonne in range(taille):

            col = colonne % taille 
            letter = grille[row][col]

            if col == 0:                                                   #pour la première colonne de chaque lignes
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
        total_points = 0                                                        #à chaque nouvelle paritie, on a un nouveau nombre de points
        if partie == 0:                                                         #and taille >= 6 : pour generer les des des grilles de taille 6 en montant, 
                                                                                #car pour les grilles de taille inferieures à 6, l'enoncé a fourni les dés

            Des = generer_des(taille)                                           #pour les prochaine parties, les des ne doivent pas etre changes

        print('Partie', partie+1)
        print(" ")   

        grille = generer_grille(taille, Des)                                    #pour toutes les parties, on a une nouvelle grille      
        print(grille)                                                           #just for further debugging
        dessiner_grille(taille, grille) 

        for manche in range(manches):
                                                                                #les points sont cumulés pour chaque manches
            x = 1                                                               #nous permettra de stocker au meme endroit les points d'un jouer pour une toutes les parties

            for player in range(joueurs):                                       #itere sur tous les joueurs presents
                total_points = 0
                player_name = "Joueur" + str(player + 1 )   
                print(player_name)
                print(" ") 

                for chances in range(10):                                        #itere sur les differentes tentatives pour chaque joueur
                    p_word = input('Proposez un mot: ')
                    point = 0

                    if p_word == " " or p_word == "":                            #les essais s'arretent s'il n'y a aucune entree
                        break

                    else:
                        validite = False

                        if len(p_word) >= 3 and len(p_word) <= (taille**2) :                    #est-ce que le mot est de la bonne taille ? (3<= longueur <=taille**2)                                    
                        
                            validite = est_adjacente(grille, p_word)                            #on veut savoir si le mot proposse est valide ou pas

                            if validite :                                                       #si le mot est valide, alors on calcul le nombre
                                message = 'ok'
                                point = calcul_point(taille, p_word)                            #de points correspondants au mot proposé

                            else:
                                message = 'Illegal'                                             #le message qu'on imprimera pour le mot non valide                                                          

                        print(affichage(p_word, point, message))
                        total_points += point

                if manche == 0 :
                    score.append(player_name)                                                   #cette liste stocke à la fois les noms des joueurs 
                    score.append(total_points)                                                  #et le nombre total de points, pour d'autres utilisations
                else:               
                    score[player + x] += total_points                                           #le nombre total de points du joueur actuel dans la liste "score"
                    x += 1

                print(player_name, 'Score: ', total_points )
                print("")

    meilleur_score  = max_points(score, joueurs)[0]
    meilleur_joueur = max_points(score, joueurs)[1]

    print("Le meilleur joueur est", meilleur_joueur, "avec un score de: ", meilleur_score)
        
    return 


#jouer()