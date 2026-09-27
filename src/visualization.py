def afficher_tournee(instance, tournee, titre="Tournée"):

    import matplotlib.pyplot as plt
    import numpy as np

    ordre = [0] + tournee + [0]
    points = np.vstack([instance.depot, instance.clients])

    xs = [points[i][0] for i in ordre]
    ys = [points[i][1] for i in ordre]

    plt.figure()
    plt.plot(xs, ys, "o-", color="blue", markersize=6)
    plt.scatter(points[0][0], points[0][1], color="red", marker="s", s=120, zorder=5)

    for i in range(1, len(points)):
        plt.text(points[i][0] + 0.3, points[i][1] + 0.3, str(i), fontsize=9)

    plt.title(f"{titre} — Longueur = {instance.longueur_tour(tournee):.2f}")
    plt.axis("equal")
    plt.grid(True)

    nom_fichier = titre.lower().replace(" ", "_").replace("(", "").replace(")", "")
    plt.savefig(f"output/{nom_fichier}.png")
    plt.close()