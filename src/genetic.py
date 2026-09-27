import random


def population_initiale(instance, taille_population):

    population = []

    for i in range(taille_population):

        # Liste des clients (indices 1 à n)
        individu = list(range(1, instance.n_clients + 1))

        # Mélange au hasard
        random.shuffle(individu)

        population.append(individu)

    return population

def selection_tournoi(instance, population, taille_tournoi=3):

    participants = random.sample(population, taille_tournoi)

    meilleur = participants[0]
    meilleure_longueur = instance.longueur_tour(meilleur)

    for individu in participants:
        longueur = instance.longueur_tour(individu)
        if longueur < meilleure_longueur:
            meilleur = individu
            meilleure_longueur = longueur

    return meilleur

def croisement_ox(parent1, parent2):

    n = len(parent1)

    # On choisit 2 points de coupe au hasard
    a = random.randint(0, n - 1)
    b = random.randint(0, n - 1)

    debut = min(a, b)
    fin = max(a, b)

    # L'enfant, vide au départ (None = pas encore rempli)
    enfant = [None] * n

    # On copie le morceau du parent1 tel quel
    enfant[debut:fin+1] = parent1[debut:fin+1]

    # On complète avec les clients du parent2, dans leur ordre,
    # en sautant ceux déjà présents dans l'enfant
    position = 0

    for client in parent2:

        if client not in enfant:

            # On cherche la prochaine case vide dans l'enfant
            while enfant[position] is not None:
                position += 1

            enfant[position] = client

    return enfant

def mutation(individu, taux_mutation=0.1):

    # Avec une petite probabilité, on échange 2 clients de place
    if random.random() < taux_mutation:

        n = len(individu)

        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)

        individu[i], individu[j] = individu[j], individu[i]

    return individu

