"""
Démo — Étape 1 : modélisation et affichage du réseau.

Usage :
    python3 main.py
"""
from __future__ import annotations

import os

import matplotlib.pyplot as plt

from src.instance import generate_random_instance
from src.visualization import plot_instance

OUTPUT_DIR = "output"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    instance = generate_random_instance(
        n_clients=20, seed=42, with_demands=True, vehicle_capacity=30
    )
    print(f"Étape 1 — {instance.n_clients} clients générés autour d'un dépôt.")
    print(f"Matrice des distances : {instance.distance_matrix.shape}")

    fig, ax = plt.subplots(figsize=(6, 6))
    plot_instance(instance, ax=ax)
    fig.savefig(f"{OUTPUT_DIR}/01_instance.png", dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  → {OUTPUT_DIR}/01_instance.png")


if __name__ == "__main__":
    main()
