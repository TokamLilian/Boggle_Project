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
        grille = [ ['G', 'A', 'W'], ['H', 'G', 'D'], ['G', 'Z', 'I'] ]
        print(dans_grille(grille, 'GGHAGWIZ'))
    #test_dans_grille()

    def test_dans_grille():
        grille = [ ['G', 'A', 'W', 'P'], ['H', 'G', 'D', 'W'], ['K', 'G', 'Z', 'I'], ['H', 'V', 'Q', 'W']]
        print(dans_grille(grille, 'GGHAGVWIZ'))
    test_dans_grille()
    
    def test_dans_grille():
        p_word = 'RAVX'
        dans_grille(letter_list, p_word)

    #test_dans_grille()


    def test_generer_des():
        Des = generer_des(3)
        print(Des)

    #test_generer_des()

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