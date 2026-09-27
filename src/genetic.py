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

