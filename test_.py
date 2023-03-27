import boggle
from boggle import *

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
    #test_max_points()
    
    def test_dans_grille():
        grille = [ ['G', 'A', 'W'], ['H', 'G', 'D'], ['G', 'Z', 'I'] ]
        print(dans_grille(grille, 'HGAWIZ'))
    #test_dans_grille()

    def test_dans_grille():
        grille = [ ['G', 'A', 'W', 'P'], ['H', 'G', 'D', 'W'], ['K', 'G', 'Z', 'I'], ['H', 'V', 'Q', 'W']]
        print(dans_grille(grille, 'GGHAGVWIZ'))
    #test_dans_grille()
    
    def test_dans_grille():
        grille = [ ['G', 'A', 'W'], ['H', 'G', 'H'], ['G', 'Z', 'I'] ]
        assert(dans_grille(grille, 'HH' )) == [[3,5],[3,5]], 'the indices..'
    #test_dans_grille()

    def test_dans_grille():
        #assert dans_grille(grille = [['A', 'D', 'N'], ['W', 'A', 'I'], ['A', 'L', 'E']], mot = 'DANIEL') == [1, [0, 4, 6], 2, 5, 8, 7]
        #assert dans_grille(grille = [['A', 'D', 'N'], ['L', 'A', 'I'], ['A', 'L', 'E']], mot = 'DANIEL') == [1, [0, 4, 6], 2, 5, 8, [3,7]]
        print(dans_grille(grille = [['A', 'D', 'N'], ['L', 'A', 'I'], ['A', 'L', 'E']], mot = 'DANIEL'))

    #test_dans_grille()

    def test_dans_grille():
        grille = [['T', 'M', 'U', 'J' ], ['G', 'D', 'S', 'P'], [ 'Q', 'O', 'E', 'J'], ['J', 'O', 'N', 'J']]
        mot = 'MUSJ'
        assert(dans_grille(grille, mot)) == [1, 2, 6, [3, 11, 12, 15]]

    #test_dans_grille()


    def test_generer_des():
        Des = generer_des(3)
        print(Des)

    #test_generer_des()


    def test_est_adjacente():
        grille = [['M', 'W', 'F', 'Z'], ['J', 'M', 'Q', 'D'], ['I', 'X', 'N', 'W'], ['S', 'L', 'I', 'I']]
        word = 'ZDWI'
        #position_matrix = dans_grille(grille, word)
        #assert(position_matrix) == [3, 7, [1, 11], [8, 14, 15]]
        assert(est_adjacente(grille, word)) == True

    test_est_adjacente()

    def test_est_adjacente():
        grille = [['D', 'X', 'M', 'B'], ['M', 'E', 'P', 'E'], ['J', 'W', 'H', 'T'], ['W', 'V', 'A', 'E']]
        #assert (dans_grille(grille, 'DEHE')) == [0, [5, 7, 15], 10, [5, 7, 15]], 'check'

        #dessiner_grille(4, grille)
        words = ['MXME', 'MXMB']
        for word in words:
            #position_matrix = dans_grille(grille, word)
            #print(position_matrix)
            assert(est_adjacente(grille, word)) == True, 'Check that out!!'
            #print(est_adjacente(grille, word))

    test_est_adjacente()

    def test_est_adjacente():
        grille = [['K', 'V', 'U', 'D'], ['U', 'X', 'P', 'N'], ['C', 'M', 'H', 'Q'], ['X', 'N', 'Z', 'M']]
        word = 'KUCXNZM'      
        #print(est_adjacente(grille, word))
        assert(est_adjacente(grille, word)) == True

    test_est_adjacente()

    def test_est_adjacente():
        grille = [['U', 'M', 'L', 'C'], ['Z', 'C', 'Z', 'C'], ['L', 'R', 'F', 'L'], ['D', 'E', 'O', 'O']]
        word = 'ZCZC'
        assert(est_adjacente(grille, word)) == True, 'Because two same letters reapeat themself in a line'

    test_est_adjacente()

    def test_est_adjacente():
        grille = [['B', 'H', 'H', 'Q'], ['F', 'Z', 'Y', 'D'], ['X', 'T', 'U', 'V'], ['K', 'J', 'Z', 'M']]
        word = 'BHHQ'
        assert(est_adjacente(grille, word)) == True, 'Because two same letters are adjacent'

    test_est_adjacente()

    def test_est_adjacente():
        grille = [['C', 'Z', 'V', 'T', 'X'], ['S', 'P', 'A', 'B', 'U'], ['P', 'R', 'P', 'L', 'O'], ['D', 'K', 'B', 'B', 'N'], ['K', 'Z', 'N', 'M', 'C']]
        word = 'CNOUX'
        assert(est_adjacente(grille, word)) == True, 'check that'
        #print(est_adjacente(grille, word))

    test_est_adjacente()

    def test_est_adjacente():
        grille = [['O', 'V', 'C', 'L', 'F'], ['L', 'T', 'A', 'A', 'I'], ['Y', 'B', 'B', 'U', 'S'], ['H', 'O', 'I', 'A', 'L'], ['S', 'J', 'E', 'A', 'U']]
        word = 'OTCLF'
        assert(est_adjacente(grille, word)) == True
        #print(est_adjacente(grille, word))

    test_est_adjacente()

    def test_est_adjacente():
        grille = [['K', 'T'], ['A', 'U']]
        word = 'AUTK'
        assert(est_adjacente(grille, word)) == True ,'Because 0 as an index was considered as False so we take the string of adjacence'
        #print(est_adjacente(grille, word))

    test_est_adjacente()

    def test_get_neighboor():
        def test_coins():
            grid5 = [0, 4, 20, 24]
            for i in grid5:
                print(i, 'has indices', get_neighboor('ABCDE', i))

            grid4 = [0, 3, 15, 12]
            for i in grid4:
                print(i, 'has indices', get_neighboor('ABCD', i))

            grid3 = [0, 2, 6, 8]
            for i in grid3:
                print(i, 'has indices', get_neighboor('ABC', i))

        def test_millieu_colonne():
            grid5 = [5, 9, 10, 14, 15, 19]
            for i in grid5:
                print(i, 'has indices', get_neighboor('ABCDE', i))

            grid4 = [4, 8, 7, 11]
            for i in grid4:
                print(i, 'has indices', get_neighboor('ABCD', i))

            grid3 = [3, 5]
            for i in grid3:
                print(i, 'has indices', get_neighboor('ABC', i))
            return
        
        def test_centre():
            grid5 = [6, 7, 8, 11, 12, 13, 16, 17, 18]
            #for i in grid5:
                #print(i, 'has indices', get_neighboor('ABCDE', i))

            grid4 = [5, 6, 9, 10]
            for i in grid4:
                print(i, 'has indices', get_neighboor('ABCD', i))

            grid3 = [4]
            for i in grid3:
                print(i, 'has indices', get_neighboor('ABC', i))
            return
            return
        
        def test_milieu_ligne():
            grid5 = [1, 2, 3, 21, 22, 23]
            for i in grid5:
                print(i, 'has indices', get_neighboor('ABCDE', i))

            grid4 = [13, 14]
            for i in grid4:
                print(i, 'has indices', get_neighboor('ABCD', i))

            grid3 = [1, 7]
            for i in grid3:
                print(i, 'has indices', get_neighboor('ABC', i))
            return
        
        #test_coins()
        #test_millieu_colonne()
        #test_centre()
        #test_milieu_ligne()

    #test_get_neighboor()

        
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