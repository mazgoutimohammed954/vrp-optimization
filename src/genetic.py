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

