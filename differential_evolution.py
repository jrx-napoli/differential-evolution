import random
from copy import deepcopy
from typing import Callable
from typing import List, Tuple

import numpy as np
from cec2017.functions import f8


def differential_evolution(args) -> Tuple[List[List[np.ndarray]], List[List[float]]]:
    # Inicjalizacja
    _F: float = args.f
    FUNCTION: Callable = f8

    p: List[np.ndarray] = [np.random.uniform(args.x_min, args.x_max, (args.x_dim,)) for _ in range(args.pop_size)]
    y: List[float] = [FUNCTION(p_i[np.newaxis, ...]).item() for p_i in p]

    # Historia wygenerowanych punktów i ich wartości funkcji celu w każdej iteracji
    h: List[List[np.ndarray]] = []
    h_y: List[List[float]] = []
    h.append(deepcopy(p))
    h_y.append(deepcopy(y))

    # Algorytm ewolucji różnicowej rand/1/bin
    for _ in range(args.n_iterations):
        new_p: List[np.ndarray] = [None for _ in range(args.pop_size)]
        new_y: List[float] = [None for _ in range(args.pop_size)]

        for i in range(args.pop_size):
            [p_j] = random.sample(p, k=1)
            p_k, p_l = random.sample(p, k=2)
            if args.tpa:
                smaller_F = _F - (args.tpa_alpha * _F)
                larger_F = min(_F + (args.tpa_alpha * _F), args.max_f)
                m_i_smaller_F = p_j + (smaller_F * (p_k - p_l))
                m_i_larger_F = p_j + (larger_F * (p_k - p_l))
                # Odbicie, jeśli wyjdzie poza ograniczenia
                m_i_smaller_F = reflection(args, m_i_smaller_F)
                m_i_larger_F = reflection(args, m_i_larger_F)
                o_i_smaller_F = crossover(args, p[i], m_i_smaller_F, args.cr)
                o_i_larger_F = crossover(args, p[i], m_i_larger_F, args.cr)
                # Wybór lepszego punktu i strojenie zasięgu mutacji za pomocą TPA
                o_i, _F = tpa(FUNCTION, F=_F, smaller_F=smaller_F, larger_F=larger_F, point_smaller_F=o_i_smaller_F,
                              point_larger_F=o_i_larger_F)
                new_p[i], new_y[i] = tournament(FUNCTION, p[i], o_i)
            else:
                m_i = p_j + (_F * (p_k - p_l))
                # Odbicie, jeśli wyjdzie poza ograniczenia
                m_i = reflection(args, m_i)
                o_i = crossover(args, p[i], m_i, args.cr)
                new_p[i], new_y[i] = tournament(FUNCTION, p[i], o_i)

        # Strojenie zasięgu mutacji za pomocą MSR
        if args.msr:
            _F = msr(args, F=_F, previous_y=y, y=new_y)

        p = deepcopy(new_p)
        y = deepcopy(new_y)

        h.append(deepcopy(p))
        h_y.append(deepcopy(y))

    return h, h_y


def reflection(args, point: np.ndarray) -> np.ndarray:
    for point_coordinate_idx in range(args.x_dim):
        point_coordinate_to_reflect_upper = np.clip(point[point_coordinate_idx] - args.x_max, a_min=0., a_max=args.x_max)
        if point_coordinate_to_reflect_upper != 0.:
            point[point_coordinate_idx] = args.x_max - point_coordinate_to_reflect_upper
        point_coordinate_to_reflect_lower = np.clip(point[point_coordinate_idx] - args.x_min, a_min=args.x_min, a_max=0.)
        if point_coordinate_to_reflect_lower != 0.:
            point[point_coordinate_idx] = args.x_min - point_coordinate_to_reflect_lower
    return point


def crossover(args, point_1: np.ndarray, point_2: np.ndarray, cr: float) -> np.ndarray:
    mutant = np.zeros_like(point_1)
    for dim in range(args.x_dim):
        a = random.uniform(0, 1)
        if a < cr:
            mutant[dim] = point_2[dim]
        else:
            mutant[dim] = point_1[dim]
    return mutant


def tournament(func, point_1: np.ndarray, point_2: np.ndarray) -> Tuple[np.ndarray, float]:
    # Zwraca punkt, dla którego wartość funkcji celu jest większa, więc maksymalizujemy
    point_1_y = func(point_1[np.newaxis, ...]).item()
    point_2_y = func(point_2[np.newaxis, ...]).item()
    if point_1_y >= point_2_y:
        return point_1, point_1_y
    return point_2, point_2_y


def msr(args, F: float, previous_y: List[float], y: List[float]) -> float:
    previous_y_median = np.median(previous_y)
    # Zlicza punkty, których wartość funkcji celu jest większa lub równa medianie, więc maksymalizujemy
    number_of_points_better_than_previous_y_median = len(list(filter(lambda y_item: y_item >= previous_y_median, y)))
    if number_of_points_better_than_previous_y_median > (args.pop_size / 2):
        new_F = F - (args.msr_alpha * F)
    else:
        new_F = min(F + (args.msr_alpha * F), args.max_f)
    return new_F


def tpa(func, F: float, smaller_F: float, larger_F: float, point_smaller_F: np.ndarray, point_larger_F: np.ndarray) -> Tuple[np.ndarray, float]:
    point_smaller_F_y = func(point_smaller_F[np.newaxis, ...]).item()
    point_larger_F_y = func(point_larger_F[np.newaxis, ...]).item()
    if point_larger_F_y > point_smaller_F_y:
        return point_larger_F, larger_F
    else:
        return point_smaller_F, smaller_F
