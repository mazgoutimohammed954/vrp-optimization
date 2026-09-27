import random


def population_initiale(instance, taille_population, tour_glouton=None):

    population = []

    if tour_glouton is not None:
        population.append(list(tour_glouton))

    while len(population) < taille_population:

        individu = list(range(1, instance.n_clients + 1))
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


def algorithme_genetique(instance, taille_population=50, nb_generations=200, taux_mutation=0.1, tour_glouton=None):

    # Population de départ
    population = population_initiale(instance, taille_population, tour_glouton)

    # On garde en mémoire le meilleur individu jamais trouvé (élitisme)
    meilleur_individu = min(population, key=lambda ind: instance.longueur_tour(ind))
    meilleure_longueur = instance.longueur_tour(meilleur_individu)

    for generation in range(nb_generations):

        nouvelle_population = []

        # On garde toujours le meilleur individu tel quel (élitisme)
        nouvelle_population.append(meilleur_individu)

        # On complète la nouvelle génération
        while len(nouvelle_population) < taille_population:

            # Sélection de 2 parents
            parent1 = selection_tournoi(instance, population)
            parent2 = selection_tournoi(instance, population)

            # Croisement
            enfant = croisement_ox(parent1, parent2)

            # Mutation
            enfant = mutation(enfant, taux_mutation)

            nouvelle_population.append(enfant)

        population = nouvelle_population

        # Mise à jour du meilleur individu trouvé
        meilleur_de_la_generation = min(population, key=lambda ind: instance.longueur_tour(ind))
        longueur_de_la_generation = instance.longueur_tour(meilleur_de_la_generation)

        if longueur_de_la_generation < meilleure_longueur:
            meilleur_individu = meilleur_de_la_generation
            meilleure_longueur = longueur_de_la_generation

    return meilleur_individu