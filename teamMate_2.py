import boggle
from boggle import 

def verification(grille,mot):
    if not est_valide(grille, mot):
        mots_refuses(joueur_actuel, mot, "Mot non présent sur la grille")

    elif mot in mots_acceptes:
                mots_refuses(joueur_actuel, mot, "Mot déjà proposé")

    elif len(mot) < 3:
                mots_refuses(joueur_actuel, mot, "Mot trop court")
    else:
          mots_acceptes(mot)
            if joueur_actuel == 1
            mots_joueur1(mot)
            else:
                mots_joueur2(mot)
                
def test_validite()
    assert validite(mot) == mots_refuses, joueur_actuel, mot, "false"
    assert validite(grille) == mot_refuses, joueur_actuel, mot, "mot non present sur la grille"
    assert validite(mot) == mot_refuses, joeur_actuel, mot, "Mot déjà proposé"
    
def test_taille(mot)
    assert taille len(mot) < 3, joueur_actuel, mot, "Mot trop court"
           

           


      
