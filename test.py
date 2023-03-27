import boggle
from boggle import *

def test():

    def test_generer_grille():
        grille_1 = generer_grille(4, Des)
        grille_2 = generer_grille(4, Des)

        assert(grille_1 != grille_2)                                        #deux appelles de grille ne doivent pas retourner la meme valeur

        longueur_de_lignes = len(grille_1[2]) == len(grille_2[3])
        assert(longueur_de_lignes) == True                                  #chaque lignes d'une grille doivent etre de longueur egales

        lettres_sur_ligne = grille_2[0] != grille_2[1]                      #les lettres contenus par deux differentes lignes sont différentes
        assert(lettres_sur_ligne) == True

        def test_longuer_ligne():
            grille = generer_grille(5, Des)
            for i in range(5): 
                assert(len(grille[i])) == 5                                 #toutes les lignes d'une grille sont de taille égale à la taille de la grille

        assert(generer_grille(-4, Des)) == None                             #pour une valeur de taille non valide, on ne retourne rien

    test_generer_grille()
    

    def test_est_adjacente():

        def test_est_adjacente_1():                     #un cas ou les lettres d'un mot se repttent
            grille = [['U', 'M', 'L', 'C'], ['Z', 'C', 'Z', 'C'], ['L', 'R', 'F', 'L'], ['D', 'E', 'O', 'O']]
            word = 'ZCZC'
            assert(est_adjacente(grille, word)) == True
        
        def test_est_adjacente_2():                     #un cas où il y a la lettre 'x' adjacente à plusieurs lettre du mot 
            grille = [['K', 'V', 'U', 'D'], ['U', 'X', 'P', 'N'], ['C', 'M', 'H', 'Q'], ['X', 'N', 'Z', 'M']]
            word = 'KUCXNZM'      
            assert(est_adjacente(grille, word)) == True

        def test_est_adjacente_3():                     #un cas où deux lettres du mot sont les memes
            grille = [['B', 'H', 'H', 'Q'], ['F', 'Z', 'Y', 'D'], ['X', 'T', 'U', 'V'], ['K', 'J', 'Z', 'M']]
            word = 'BHHQ'
            assert(est_adjacente(grille, word)) == True
        
        def test_est_adjacente_4():                     #un cas où le mot est formé sur une colonne du haut vers le bas
            grille = [['C', 'Z', 'V', 'T', 'X'], ['S', 'P', 'A', 'B', 'U'], ['P', 'R', 'P', 'L', 'O'],
                       ['D', 'K', 'B', 'B', 'N'], ['K', 'Z', 'N', 'M', 'C']]
            word = 'CNOUX'
            assert(est_adjacente(grille, word)) == True

        def test_est_adjacente_5():                     #un cas du le mot qui couvre toute la grille (en serpent)
            grille = [['E', 'E', 'P', 'I', 'F', 'C'], ['O', 'X', 'A', 'O', 'G', 'M'],
                       ['A', 'S', 'A', 'E', 'S', 'R'], ['H', 'N', 'U', 'R', 'V', 'H'], 
                       ['U', 'I', 'D', 'V', 'E', 'D'], ['O', 'Z', 'O', 'L', 'N', 'U']]
            word = 'EOAHUOZOLNUDHRMCFIPEXSNIDVEVSGOAAURE'
            assert(est_adjacente(grille, word)) == True

        test_est_adjacente_1()
        test_est_adjacente_2()
        test_est_adjacente_3()
        test_est_adjacente_4()
        test_est_adjacente_5()
    

    test_est_adjacente()


    def test_calcul_point():

        assert(calcul_point(4, 'MAISON'))       == 5                     #dans une grille de taille 4, un mot de 6 lettres donne 5 points
        assert(calcul_point(5, 'MAISON'))       == 4                     #dans une grille de taille 5, un mot de 6 lettres donne 4 points
        assert(calcul_point(4, 'VOITURE'))      == 8                     #dans une grille de taille 4, un mot de 7 lettres donne 8 points
        assert(calcul_point(6, 'VOITURE'))      == 7                     #dans une grille de taille 6, un mot de 7 lettres donne 7 points
        assert(calcul_point(6, 'INDEPENDENT'))  == 12                    #dans une grille de taille 6, un mot de plus que 9 lettres donne 12 points
        
    test_calcul_point()


test()