"""
Étape 1 — Modélisation du problème.

On représente le dépôt et les clients comme les sommets d'un graphe complet,
et on calcule la matrice des distances euclidiennes entre eux. Cette matrice
est calculée une seule fois à la création de l'instance.

Convention : l'indice 0 désigne toujours le dépôt ; les indices 1..n
désignent les n clients.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


@dataclass
class Instance:
    """Une instance de problème de tournées de livraison."""

    depot: np.ndarray
    clients: np.ndarray
    demands: np.ndarray = field(default=None)
    vehicle_capacity: float | None = None

    _distance_matrix: np.ndarray = field(default=None, init=False, repr=False)

    def __post_init__(self) -> None:
        self.depot = np.asarray(self.depot, dtype=float)
        self.clients = np.asarray(self.clients, dtype=float)

        if self.demands is None:
            self.demands = np.zeros(len(self.clients))
        else:
            self.demands = np.asarray(self.demands, dtype=float)

        coords = np.vstack([self.depot, self.clients])
        diff = coords[:, None, :] - coords[None, :, :]
        self._distance_matrix = np.sqrt((diff ** 2).sum(axis=-1))

    @property
    def n_clients(self) -> int:
        return len(self.clients)

    @property
    def coords(self) -> np.ndarray:
        """Toutes les coordonnées, dépôt inclus en position 0."""
        return np.vstack([self.depot, self.clients])

    @property
    def distance_matrix(self) -> np.ndarray:
        return self._distance_matrix

    def tour_length(self, tour: list[int]) -> float:
        """Longueur d'une tournée partant du dépôt, visitant `tour`, et y revenant."""
        d = self._distance_matrix
        full = [0, *tour, 0]
        return float(sum(d[full[i], full[i + 1]] for i in range(len(full) - 1)))


def generate_random_instance(
    n_clients: int,
    width: float = 100.0,
    height: float = 100.0,
    seed: int | None = None,
    with_demands: bool = False,
    demand_range: tuple[int, int] = (1, 10),
    vehicle_capacity: float | None = None,
) -> Instance:
    """Génère une instance aléatoire : un dépôt et n_clients clients
    uniformément répartis dans un rectangle width x height.
    """
    rng = np.random.default_rng(seed)
    depot = rng.uniform([0, 0], [width, height], size=2)
    clients = rng.uniform([0, 0], [width, height], size=(n_clients, 2))

    demands = None
    if with_demands:
        demands = rng.integers(demand_range[0], demand_range[1] + 1, size=n_clients)

    return Instance(
        depot=depot,
        clients=clients,
        demands=demands,
        vehicle_capacity=vehicle_capacity,
    )
