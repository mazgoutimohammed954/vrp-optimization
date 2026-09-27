"""Tests unitaires — Étape 1 : modélisation."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.instance import generate_random_instance


def test_instance_has_correct_number_of_clients():
    inst = generate_random_instance(n_clients=15, seed=1)
    assert inst.n_clients == 15


def test_distance_matrix_shape_and_diagonal():
    inst = generate_random_instance(n_clients=15, seed=1)
    assert inst.distance_matrix.shape == (16, 16)  # dépôt + 15 clients
    assert (inst.distance_matrix.diagonal() == 0).all()


def test_distance_matrix_is_symmetric():
    inst = generate_random_instance(n_clients=10, seed=2)
    d = inst.distance_matrix
    assert (abs(d - d.T) < 1e-9).all()


def test_tour_length_round_trip_to_depot():
    inst = generate_random_instance(n_clients=5, seed=3)
    tour = [1, 2, 3, 4, 5]
    length = inst.tour_length(tour)
    assert length > 0


def test_demands_default_to_zero_without_with_demands():
    inst = generate_random_instance(n_clients=5, seed=4, with_demands=False)
    assert (inst.demands == 0).all()
