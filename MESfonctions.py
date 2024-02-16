import numpy as np
import copy
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


def repetition_retangulaire(objet, nx=0, ny=0, nz=0, dx=0, dy=0, dz=0):
    
    """
    Fonction qui effectue une répétition rectangulaire sur un objet.

    'objet' est l'objet sur lequel on effectue la répétition rectangualire.

    'nx', 'ny', 'nz' sont le nombre de fois qu'on répète l'objet en x, y ou/et z.

    'dx', 'dy', 'dz' sont les distances entre chaque répétition.
    """
    
    objet_repeter = copy.deepcopy(objet)
    objet_final = copy.deepcopy(objet)

    if nx != 0:
        for i in range(1, nx):
            objet_translater = copy.deepcopy(Translation(objet_repeter, np.array([dx, 0, 0]))) # Effectue une translation sur l'objet
            objet_final = copy.deepcopy(Groupe(objet_final, objet_translater)) # Groupe l'objet translaté et le groupe déjà fait

    objet_finalx = copy.deepcopy(objet_final) # Garde en mémoire le groupe fait en x pour l'utiliser en y ou z
    
    # La même logique est applquée en y et en z.
    
    if ny != 0:
        for j in range(1, ny):
            objet_translater = copy.deepcopy(Translation(objet_finalx, np.array([0, dy, 0])))
            objet_final = copy.deepcopy(Groupe(objet_final, objet_translater))

    objet_finaly = copy.deepcopy(objet_final)

    if nz != 0:
        if ny != 0:
            for k in range(1, nz):
                objet_translater = copy.deepcopy(Translation(objet_finaly, np.array([0, 0, dz])))
                objet_final = copy.deepcopy(Groupe(objet_final, objet_translater))
        
        elif nx != 0:
             for k in range(1, nz):
                objet_translater = copy.deepcopy(Translation(objet_finalx, np.array([0, 0, dz])))
                objet_final = copy.deepcopy(Groupe(objet_final, objet_translater))

    F, V, N = objet_final[0], objet_final[1], objet_final[2]

    return [F, V, N]

def centrer(objet):
    
    """
    Fonction qui centre un objet sur le plan xy selon l'axe z.

    'objet' est l'objet qu'on veut centrer
    """
    F, V, N = objet[0], objet[1], objet[2]

    centre_x = (min(V[:,0]) + max(V[:,0])) / 2 # Trouve le centre de l'objet en x

    centre_y = (min(V[:,1]) + max(V[:,1])) / 2 # Trouve le centre de l'objet en y

    min_z = min(V[:,2]) # Trouve la coordonnée mimimale en z pour situer la base de l'objet

    F, V, N = Translation(objet, np.array([-centre_x, -centre_y, -min_z]))

    return [F, V, N]
    

def repetition_rotative():
    """
    À faire
    """
    return


def repetition_sur_courbe():
    """
    À faire
    """
    return   

def etirement():
    """
    À faire
    """
    return

def miseechelle()
    """
    À faire
    """
    return





