import boggle
from boggle import *

taille = 4
#Des = generer_des(taille)
#letter_list = dessiner_grille(taille, Des)
#print(letter_list)

letter_list = ['I', 'R', 'J', 'S', 'A', 'W', 'Z', 'Y', 'H', 'V', 'C', 'D', 'J', 'L', 'X', 'P']

def test():

    def test_calcul_point():
        ma_grille = input("Nth size grid: ")
        for i in range (4):
            mot = input('Word: ')
            point = calcul_point(ma_grille, mot)
            taille_mot = len(mot)
            taille_grille = len(ma_grille)

            print("le mot de taille", taille_mot, 'donne', point, 'point(s)', 'pour une grille de taille', taille_grille)
    #test_calcul_point()


    def test_max_points():
        score = ['jouer1', '13', 'joueur2', '15', 'jouer3', '13', 'joueur4', '15', 'jouer5', '13', 'joueur6', '15']
        print(max_points(score, 6))

    
    def test_dans_grille():
        grille = 'CQDJAAEKIKSVJTFU'
        p_word = 'CAST'
        present = dans_grille(grille, p_word)
        print(present)

    
    def test_dans_grille():
        p_word = 'RAVX'
        dans_grille(letter_list, p_word)

    #test_dans_grille()


    def test_generer_des():
        Des = generer_des(3)
        print(Des)

    #test_generer_des()


    def generer_grille1(taille, letter_list):            #par Lilian
        grille = [None] * taille

        start = 0
        end = taille
        for i in range (taille):
        
            end = taille * (i+1)

            grid = []
            for j in range (start, end):
                grid.append(letter_list[j])
                start = j + 1

            grille[i] = grid
        return grille


    def generer_grille(taille, letter_list):            #par Papa
        grille = [None] * taille

        for i in range (taille):
            grille[i] = [None] * taille                 #creation de la grille

        for j in range (len(letter_list)):              #parcourir tous les elements de la liste

            row = j // taille                           #division par la largeur de la grille pour avoir le numero de la ligne

            col = j % taille                            #le reste de la division de la position de la lettre et la taille de la grille, donne le numero de la colonne

            grille[row][col] = letter_list[j]

        print(grille)
        return grille
    

    def test_verification():
        grille = generer_grille(taille, letter_list)
        word = 'HARTARFEDE'
       
        print(verification(grille, word))

    #test_verification()

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