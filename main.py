from src.instance import Instance
from src.greedy import plus_proche_voisin
from src.local_search import deux_opt

depot = [0, 0]
clients = [[3, 4], [6, 8], [10, 0], [2, 9], [7, 2]]

instance = Instance(depot, clients)

tour = plus_proche_voisin(instance)
tour_ameliore = deux_opt(instance, tour)

print("Tournée gloutonne :", tour)
print("Tournée améliorée :", tour_ameliore)
print("Longueur avant :", instance.longueur_tour(tour))
print("Longueur après :", instance.longueur_tour(tour_ameliore))