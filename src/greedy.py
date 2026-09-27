def plus_proche_voisin(instance):

    # Nombre de clients
    n = instance.n_clients

    # Liste des clients pas encore visités (indices 1 à n)
    a_visiter = list(range(1, n + 1))

    # La tournée qu'on va construire
    tournee = []

    # On part du dépôt (indice 0)
    position_actuelle = 0

    # Tant qu'il reste des clients à visiter
    while len(a_visiter) > 0:

        # On initialise avec le premier client restant
        meilleur_client = a_visiter[0]
        meilleure_distance = instance.distance_matrix[position_actuelle][meilleur_client]

        # On compare avec tous les autres clients restants
        for client in a_visiter:

            distance = instance.distance_matrix[position_actuelle][client]

            # Si on trouve plus proche, on met à jour
            if distance < meilleure_distance:
                meilleure_distance = distance
                meilleur_client = client

        # On ajoute le meilleur client trouvé à la tournée
        tournee.append(meilleur_client)

        # On le retire des clients à visiter
        a_visiter.remove(meilleur_client)

        # La position actuelle devient ce client
        position_actuelle = meilleur_client

    return tournee