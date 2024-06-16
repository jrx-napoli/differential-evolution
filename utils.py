import os
from argparse import Namespace
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np


def generate_results(args: Namespace, h: List[List[np.ndarray]], h_y: List[List[float]]) -> None:
    path = f"results/{args.y_func}"
    if args.tpa: path += f"_tpa"
    if args.msr: path += f"_msr"

    if not os.path.exists(path):
        os.makedirs(path)

    best_point_idx, best_point_y_val = get_last_best_point(h, h_y)
    f = open(f"{path}/best_point.txt", "w")
    f.write(f"Final best point:\nidx: {best_point_idx}\ny_val: {best_point_y_val}")

    f_args = open(f"{path}/args.txt", "w")
    f_args.write(args.__dict__.__str__())

    plot(h_y, path)


def get_last_best_point(h: List[List[np.ndarray]], h_y: List[List[float]]) -> Tuple[np.ndarray, float]:
    p_last_iteration = h[-1]
    y_last_iteration = h_y[-1]
    max_y_idx = np.argmax(y_last_iteration)
    return p_last_iteration[max_y_idx], y_last_iteration[max_y_idx]


def plot(h_y: List[List[float]], path: str) -> None:
    h_y_np = np.array(h_y)
    mean_y_for_each_iteration = np.mean(h_y_np, axis=1)
    indices_of_iterations = list(range(len(mean_y_for_each_iteration)))
    plt.plot(indices_of_iterations, mean_y_for_each_iteration, color="red")
    plt.xlabel("Numer iteracji")
    plt.ylabel("Średnia wartość funkcji celu")
    plt.title("Zależność średniej wartości funkcji celu od numeru iteracji")

    plt.savefig(f"{path}/plot.png")
    plt.close()
