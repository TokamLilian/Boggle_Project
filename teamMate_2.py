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
                
def test_verification()
    assert verification(grille,mot) != mots_refuses,joueur_actuel, mot, "true"
    assert verification(grille,mot) != mots_acceptes,joueur_actuel, mot, "mot non present sur la grille"
    assert verification(grille,len(mot)) < 3, joueur_actuel, mot, "Mot trop court"
           


      
