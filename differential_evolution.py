from copy import deepcopy
import random
from typing import List, Tuple

import numpy as np

from differential_evolution_config import *


def differential_evolution() -> Tuple[List[List[np.ndarray]], List[List[float]]]:
    # Inicjalizacja
    _F: float = F

    p: List[np.ndarray] = [np.random.uniform(X_MIN, X_MAX, (X_DIM, )) for _ in range(POPULATION_SIZE)]
    y: List[float] = [FUNCTION(p_i[np.newaxis, ...]).item() for p_i in p]

    # Historia wygenerowanych punktów i ich wartości funkcji celu w każdej iteracji
    h: List[List[np.ndarray]] = []
    h_y: List[List[float]] = []
    h.append(deepcopy(p))
    h_y.append(deepcopy(y))

    # Algorytm ewolucji różnicowej rand/1/bin
    for _ in range(NUMBER_OF_ITERATIONS):
        new_p: List[np.ndarray] = [None for _ in range(POPULATION_SIZE)]
        new_y: List[float] = [None for _ in range(POPULATION_SIZE)]

        for i in range(POPULATION_SIZE):
            [p_j] = random.sample(p, k=1)
            p_k, p_l = random.sample(p, k=2)
            if USE_TPA:
                smaller_F = _F - (TPA_F_ALPHA * _F)
                larger_F = min(_F + (TPA_F_ALPHA * _F), MAX_F)
                m_i_smaller_F = p_j + (smaller_F * (p_k - p_l))
                m_i_larger_F = p_j + (larger_F * (p_k - p_l))
                # Odbicie, jeśli wyjdzie poza ograniczenia
                m_i_smaller_F = reflection(m_i_smaller_F)
                m_i_larger_F = reflection(m_i_larger_F)
                o_i_smaller_F = crossover(p[i], m_i_smaller_F, CR)
                o_i_larger_F = crossover(p[i], m_i_larger_F, CR)
                # Wybór lepszego punktu i strojenie zasięgu mutacji za pomocą TPA
                o_i, _F = tpa(F=_F, smaller_F=smaller_F, larger_F=larger_F, point_smaller_F=o_i_smaller_F, point_larger_F=o_i_larger_F)
                new_p[i], new_y[i] = tournament(p[i], o_i)
            else:
                m_i = p_j + (_F * (p_k - p_l))
                # Odbicie, jeśli wyjdzie poza ograniczenia
                m_i = reflection(m_i)
                o_i = crossover(p[i], m_i, CR)
                new_p[i], new_y[i] = tournament(p[i], o_i)
        
        # Strojenie zasięgu mutacji za pomocą MSR
        if USE_MSR:
            _F = msr(F=_F, previous_y=y, y=new_y)

        p = deepcopy(new_p)
        y = deepcopy(new_y)

        h.append(deepcopy(p))
        h_y.append(deepcopy(y))

    return h, h_y

def reflection(point: np.ndarray) -> np.ndarray:
    for point_coordinate_idx in range(X_DIM):
        point_coordinate_to_reflect_upper = np.clip(point[point_coordinate_idx] - X_MAX, a_min=0., a_max=X_MAX)
        if point_coordinate_to_reflect_upper != 0.:
            point[point_coordinate_idx] = X_MAX - point_coordinate_to_reflect_upper
        point_coordinate_to_reflect_lower = np.clip(point[point_coordinate_idx] - X_MIN, a_min=X_MIN, a_max=0.)
        if point_coordinate_to_reflect_lower != 0.:
            point[point_coordinate_idx] = X_MIN - point_coordinate_to_reflect_lower
    return point


def crossover(point_1: np.ndarray, point_2: np.ndarray, cr: float) -> np.ndarray:
    mutant = np.zeros_like(point_1)
    for dim in range(X_DIM):
        a = random.uniform(0, 1)
        if a < cr:
            mutant[dim] = point_2[dim]
        else:
            mutant[dim] = point_1[dim]
    return mutant


def tournament(point_1: np.ndarray, point_2: np.ndarray) -> Tuple[np.ndarray, float]:
    # Zwraca punkt, dla którego wartość funkcji celu jest większa, więc maksymalizujemy
    point_1_y = FUNCTION(point_1[np.newaxis, ...]).item()
    point_2_y = FUNCTION(point_2[np.newaxis, ...]).item()
    if point_1_y >= point_2_y:
        return point_1, point_1_y
    return point_2, point_2_y


def msr(F: float, previous_y: List[float], y: List[float]) -> float:
    previous_y_median = np.median(previous_y)
    # Zlicza punkty, których wartość funkcji celu jest większa lub równa medianie, więc maksymalizujemy
    number_of_points_better_than_previous_y_median = len(list(filter(lambda y_item: y_item >= previous_y_median, y)))
    if number_of_points_better_than_previous_y_median > (POPULATION_SIZE / 2):
        new_F = F - (MSR_F_ALPHA * F)
    else:
        new_F = min(F + (MSR_F_ALPHA * F), MAX_F)
    return new_F


def tpa(F: float, smaller_F: float, larger_F: float, point_smaller_F: np.ndarray, point_larger_F: np.ndarray) -> Tuple[np.ndarray, float]:
    point_smaller_F_y = FUNCTION(point_smaller_F[np.newaxis, ...]).item()
    point_larger_F_y = FUNCTION(point_larger_F[np.newaxis, ...]).item()
    if point_larger_F_y > point_smaller_F_y:
        return point_larger_F, larger_F
    else:
        return point_smaller_F, smaller_F
