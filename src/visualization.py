import matplotlib.pyplot as plt


def afficher_instance(instance):

    # Récupérer le dépôt
    depot = instance.depot

    # Récupérer les clients
    clients = instance.clients

    # Coordonnées du dépôt
    x_depot = depot[0]
    y_depot = depot[1]

    # Afficher le dépôt
    plt.scatter(
        x_depot,
        y_depot,
        color="red",
        marker="s",
        s=150
    )

    # Afficher les clients
    for i in range(len(clients)):

        x = clients[i][0]
        y = clients[i][1]

        plt.scatter(
            x,
            y,
            color="blue",
            s=60
        )

        # Afficher le numéro du client
        plt.text(
            x + 0.2,
            y + 0.2,
            str(i + 1)
        )

    # Titre
    plt.title("Clients et dépôt")

    # Nom des axes
    plt.xlabel("X")
    plt.ylabel("Y")

    # Garder les mêmes proportions
    plt.axis("equal")

    # Afficher le graphique
    plt.show()