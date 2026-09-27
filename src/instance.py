import numpy as np


class Instance:

    def __init__(self, depot, clients):

        # Le dépôt
        self.depot = np.array(depot)

        # Les clients
        self.clients = np.array(clients)

        # Nombre de clients
        self.n_clients = len(clients)

        # Calcul de la matrice des distances
        self.distance_matrix = self.calculer_distances()


    def calculer_distances(self):

        # Mettre le dépôt et les clients
        # dans un seul tableau
        points = np.vstack([self.depot, self.clients])

        # Nombre total de points
        n = len(points)

        # Créer une matrice remplie de 0
        distances = np.zeros((n, n))

        # Parcourir les points
        for i in range(n):

            # Comparer avec tous les autres points
            for j in range(n):

                # Coordonnées du point i
                x1 = points[i][0]
                y1 = points[i][1]

                # Coordonnées du point j
                x2 = points[j][0]
                y2 = points[j][1]

                # Formule de distance euclidienne
                distance = np.sqrt((x1 - x2) ** 2 +(y1 - y2) ** 2
                )

                # Stocker la distance
                distances[i][j] = distance

        return distances


    def longueur_tour(self, tour):

        # Commencer au dépôt
        trajet = [0]

        # Ajouter les clients
        trajet = trajet + tour

        # Retourner au dépôt
        trajet.append(0)

        # Distance totale
        distance_totale = 0

        # Parcourir le trajet
        for i in range(len(trajet) - 1):

            # Point de départ
            depart = trajet[i]

            # Point d'arrivée
            arrivee = trajet[i + 1]

            # Ajouter la distance
            distance_totale += self.distance_matrix[depart][arrivee]

        return distance_totale


# Création des données

depot = [0, 0]

clients = [
    [3, 4],
    [6, 8],
    [10, 0]
]


# Création de l'instance

instance = Instance(depot, clients)


# Afficher le nombre de clients

print("Nombre de clients :", instance.n_clients)


# Afficher la matrice


print("Matrice des distances :")
print(instance.distance_matrix)


# Créer une tournée

tour = [1, 2, 3]


# Calculer sa longueur

distance = instance.longueur_tour(tour)

print("Distance totale :", distance)