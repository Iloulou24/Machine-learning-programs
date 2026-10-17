from math import sqrt
"""FONCTIONNEMENT DE MON KNN:
1 calcul de la distance euclidienne entre le nouveau point et chaque points

2 chaque distance est enregistré dans un tuple avec son point correspondant
(coordonées,classe) dans une liste de tuples:
[(distance,([x1,y1],classe)),...

3 tri de la liste (distance minimum au maximum) et recup
des k premiers points de la liste de tuples : [([xmin,ymin],classe),...]

4 analyse de la classe en majorité dans la liste récupéré
{nom_class1:nb_points,nom_class2:nb_point,...}

5 déduction de la classe du nouveau point avec la classe majoritaire
    
"""


def même_longueur(point, liste_de_points):
    '''
    modifie les coordonnées d'un point en rajoutant des dimensions(0)
    Arguments :
        point:liste [1,2]
        liste de points : liste de tuples avec leur classe et les coordonnées
        [
        ([1,2,3,4],"A"),
        ([4,3,2,1],"B")]

    Retourne :
        le point (en tuple) est la liste de point de même dimension
    '''
    while len(point) != len(liste_de_points[1][0]):
        if len(point) < len(liste_de_points[1][0]):
            point.append(0)
        else:
            for i in range(len(liste_de_points)):
                liste_de_points[i][0].append(0)
    return tuple(point), liste_de_points


def distance_euclidienne(point_a, point_b):
    ''' Retourne la distance euclidienne entre deux points.
        Les points sont représentés par des tuples ou des listes de nombres.
        Le nombre de dimensions doit être le même pour les deux points.
        Arguments :
            point_a (tuple ou list) : Premier point.
            point_b (tuple ou list) : Deuxième point.
        Retourne :
            float : La distance euclidienne entre point_a et point_b.
    '''
    somme_carre = 0
    for i in range(len(point_a)):  # le nombre de boucle est égal au nombre de coordonnées
        # point[i] est une des coordonnées du points
        difference_au_carre = (point_a[i]-point_b[i])**2
        somme_carre += difference_au_carre
    return sqrt(somme_carre)


def trouver_k_plus_proches_voisins(point_cible, donnees_entrainement, k):
    '''trouve les k points les plus proches du point cible en fonction
       d'une liste de points donnée et leur distance
       Argument:
           point_cible: tuple d'entiers
           donnees_entrainement : liste de point avec leur classe
           k: nombre de voisins à trouver
       Retourne:
            list: Une liste des k tuples (point, classe) représentant les voisins les plus proches.
    '''
    liste_distance = []
    for i in range(len(donnees_entrainement)):
        # compare la distance du point choisi au points déja existants
        # ajoute dans la liste la distance entre les deux points et le point utilisé dans les données
        liste_distance.append((distance_euclidienne(
            point_cible, donnees_entrainement[i][0]), donnees_entrainement[i]))

    liste_distance.sort()  # arrange la liste de la distance min au max
    # recupère les k premiers points de la liste
    liste_k_voisins = [liste_distance[i][1] for i in range(k)]
    return liste_k_voisins


def vote(voisins):
    ''' trouve le nombre de fois qu'une classe est dans la liste
        et déterminer laquelle est majoritaire
        Argument:
            voisins : liste de tuples coordonnées classes [([1,2,3,4],"A"),
                                                        ([3,9,4,5],"C"),]                                
        Retourne:
            classe majoritaire : caractère
    '''
    dico_voisin: dict["str", int] = {}
    for voisin in voisins:
        # voisin[1] correspond à la classe du point
        if voisin[1] in dico_voisin:
            dico_voisin[voisin[1]] += 1
        else:
            dico_voisin[voisin[1]] = 1
    return max(dico_voisin)


def determiner_classe(point_cible, donnees_entrainement, nombre_voisins):
    voisins = trouver_k_plus_proches_voisins(
        point_cible, donnees_entrainement, nombre_voisins)
    return vote(voisins), nombre_voisins
