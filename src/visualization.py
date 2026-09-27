"""Étape 1 — Visualisation du réseau (dépôt + clients) avec Matplotlib."""
from __future__ import annotations

import matplotlib.pyplot as plt


def plot_instance(instance, ax=None, title: str = "Clients et dépôt"):
    """Affiche le dépôt et les clients, sans tournée."""
    ax = ax or plt.gca()
    ax.scatter(*instance.depot, c="red", s=150, marker="s", label="Dépôt", zorder=3)
    ax.scatter(
        instance.clients[:, 0], instance.clients[:, 1],
        c="steelblue", s=60, label="Clients", zorder=3,
    )
    for i, (x, y) in enumerate(instance.clients, start=1):
        ax.annotate(str(i), (x, y), textcoords="offset points", xytext=(4, 4), fontsize=8)
    ax.set_title(title)
    ax.legend()
    ax.set_aspect("equal")
    return ax
