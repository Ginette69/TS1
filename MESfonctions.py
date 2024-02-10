import numpy as np
from MEC1315_STL import *

def rotation(objet, axe, theta, matrice_de_translation=np.array([0, 0, 0])):
    
    """
    Fonction qui effectue une rotations en x, y ou z.
    
    'objet' est l'objet sur lequel vous voulez effectuer la rotation.
    
    'axe' est l'axe de rotation. IL faut préciser 'x', 'y' ou 'z'.
    
    'theta' est l'angle de rotion de l'objet. Il doit être en radian. 
    Numpy à une fonction de conversion degré/radian : deg2rad()
    
    'matrice de translation' est la matrice de translation 1x3. Elle est optionnelle.
    """
    
    F, V, N = objet[0], objet[1], objet[2]
    matrice_de_translation = np.array(matrice_de_translation).reshape(1,3)
    
    if axe == 'x':
        U = matrice_de_translation + V.dot(RxT(theta))
    
    elif axe == 'y':
        U = matrice_de_translation + V.dot(RyT(theta))

    elif axe == 'z':
        U = matrice_de_translation + V.dot(RyT(theta))    
        
    else:
        return print("Argument invalide ou manquant")
    
    return [F, U, N]


def Groupe(objet1, objet2):
    
    """
    Fonction qui groupe deux objets stl dans une seul liste.
    
    "objet1" est le premier objet à grouper.
    
    "objet2" est le deuxième objet à grouper.
    
    Attention, la fonction prend en input uniquement des listes. 
    """
    
    objet2[0] += len(objet1[1])
    
    F = np.vstack((objet1[0],objet2[0])) 
    
    V = np.vstack((objet1[1],objet2[1]))
   
    N = np.vstack((objet1[2],objet2[2]))
    
    return [F, V, N]


def Translation(objet, matrice_de_translation):
    
    """
    Fonction qui effectue une translation dans un direction x, y ou z.
    
    "objet" est l'objet sur lequel vous souhaitez effectuer la rotation.
    
    "matrice de tranlation" est la matrice 1x3  qui va permettre d'effectuer la translation. Les coéficients sont des distances.
    """
    
    F, V, N = objet[0], objet[1], objet[2]
    
    matrice_de_translation = np.array(matrice_de_translation).reshape(1,3)
   
    U = matrice_de_translation + V
    
    return [F, U, N]


def Homothétie(objet, position_centre_homothetie, facteur_de_grossissement):
    
    """
    Fonction qui effectue un grossisement ou un raptissement d'un facteur f.
    
    'objet' est l'objet sur lequel vous souhaitez effectuer l'homothétie.
    
    'position_centre_homothetie' est la  position de base pour effectuer l'homotétie.
    
    'facteur_de_grossissement' est le facteur de grossisement. Il peut être de 0 à l'infinie.
    """
    
    F, V, N = objet[0], objet[1], objet[2]
    
    position_centre_homothetie = np.array(position_centre_homothetie).reshape(1,3)
    
    U = facteur_de_grossissement * V + (1-facteur_de_grossissement) * position_centre_homothetie
    
    return [F, U, N]


def repetition_retangulaire(objet, matrice_de_translation, matrice_de_repetition):
    
    """
    Fonction qui effectue une répétition rectangulaire sur un objet.

        
    """
    
    copie_objet = objet
    
    if matrice_de_repetition[0] != 0:
        for rep in range(matrice_de_repetition[0] + 1):
            copie_objet = Groupe(copie_objet, Translation(copie_objet, np.array([matrice_de_translation[0], 0, 0])))
                           
    if matrice_de_repetition[1] != 0:
        for rep in range(matrice_de_repetition[1] + 1):
            copie_objet = Groupe(copie_objet, Translation(copie_objet, np.array([0, matrice_de_translation[1], 0])))
    
    if matrice_de_repetition[2] != 0:
        for rep in range(matrice_de_repetition[2] + 1):
            copie_objet = Groupe(copie_objet, Translation(copie_objet, np.array([0, 0, matrice_de_translation[2]])))
    
    F, V, N = copie_objet
    
    return [F, V, N]
            







