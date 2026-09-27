from src.instance import Instance
from src.greedy import plus_proche_voisin
from src.local_search import deux_opt
from src.genetic import algorithme_genetique
from src.vrp import comparer_methodes
from src.visualization import afficher_tournee


# Création de l'instance
depot = [50, 50]

clients = [
    [10, 20], [80, 90], [30, 40], [70, 10], [20, 80],
    [90, 30], [40, 60], [60, 20], [15, 55], [85, 65],
    [35, 15], [55, 85], [25, 35], [75, 45], [45, 75]
]

instance = Instance(depot, clients)


# Glouton (plus proche voisin)
tour_glouton = plus_proche_voisin(instance)

# 2-opt à partir du glouton
tour_2opt = deux_opt(instance, list(tour_glouton))

# Algorithme génétique
tour_genetique = algorithme_genetique(instance, taille_population=50, nb_generations=200, tour_glouton=tour_glouton)


# Comparaison des 3 méthodes
comparer_methodes(instance, tour_glouton, tour_2opt, tour_genetique)


# Affichage des tournées
afficher_tournee(instance, tour_glouton, "Glouton (plus proche voisin)")
afficher_tournee(instance, tour_2opt, "Glouton + 2-opt")
afficher_tournee(instance, tour_genetique, "Algorithme génétique")