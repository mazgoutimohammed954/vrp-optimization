def comparer_methodes(instance, tour_glouton, tour_2opt, tour_genetique):

    longueurs = {
        "Glouton": instance.longueur_tour(tour_glouton),
        "2-opt": instance.longueur_tour(tour_2opt),
        "Génétique": instance.longueur_tour(tour_genetique),
    }

    print("=== Comparaison des méthodes ===")
    for nom, longueur in longueurs.items():
        print(f"{nom:12s} : {longueur:.2f}")

    return longueurs