def deux_opt(instance, tournee):

    # On part du principe qu'il y a une amélioration à chercher
    amelioration = True

    # Tant qu'on trouve des améliorations, on continue
    while amelioration:

        amelioration = False

        # On essaie toutes les paires de positions (i, j) dans la tournée
        for i in range(len(tournee) - 1):

            for j in range(i + 1, len(tournee)):

                # On construit une nouvelle tournée en inversant
                # le morceau entre les positions i et j
                nouvelle_tournee = tournee[:i] + tournee[i:j+1][::-1] + tournee[j+1:]

                # Longueur actuelle vs longueur avec l'inversion
                longueur_actuelle = instance.longueur_tour(tournee)
                longueur_nouvelle = instance.longueur_tour(nouvelle_tournee)

                # Si la nouvelle tournée est plus courte, on la garde
                if longueur_nouvelle < longueur_actuelle:
                    tournee = nouvelle_tournee
                    amelioration = True

    return tournee