import os
from argparse import Namespace
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np


def generate_results(args: Namespace, h: List[List[np.ndarray]], h_y: List[List[float]]) -> None:
    path = f"results/{args.y_func}"
    plot_name = args.y_func
    comp_entry_name = args.y_func

    if args.tpa:
        path += f"_tpa"
        plot_name += f"_tpa"
        comp_entry_name += f"_tpa"
    if args.msr:
        path += f"_msr"
        plot_name += f"_msr"
        comp_entry_name += f"_msr"

    path += f"_{args.seed}"
    comp_entry_name += f"_{args.seed}"

    if not os.path.exists(path):
        os.makedirs(path)

    best_point_idx, best_point_y_val = get_last_best_point(h, h_y)
    first_best_mean = get_first_best_iteration(h_y)
    f = open(f"{path}/best_point.txt", "w")
    f.write(f"Final best point:\nidx: {best_point_idx}\ny_val: {best_point_y_val}\nfound in: {first_best_mean}")

    f_comp = open(f"results/comparison.txt", "a")
    f_comp.write(f"{comp_entry_name}:\n{best_point_idx} {best_point_y_val} {first_best_mean}\n\n")

    f_args = open(f"{path}/args.txt", "w")
    f_args.write(args.__dict__.__str__())

    plot(h_y, path, plot_name)


def get_last_best_point(h: List[List[np.ndarray]], h_y: List[List[float]]) -> Tuple[np.ndarray, float]:
    p_last_iteration = h[-1]
    y_last_iteration = h_y[-1]
    min_y_idx = np.argmin(y_last_iteration)
    return p_last_iteration[min_y_idx], y_last_iteration[min_y_idx]


def get_first_best_iteration(h_y: List[List[float]]) -> int:
    min_value = float('inf')
    min_index = -1
    
    for i, sublist in enumerate(h_y):
        local_min = min(sublist)
        if local_min < min_value:
            min_value = local_min
            min_index = i
    
    return min_index


def plot(h_y: List[List[float]], path: str, plot_name: str) -> None:
    h_y_np = np.array(h_y)
    mean_y_for_each_iteration = np.mean(h_y_np, axis=1)
    indices_of_iterations = list(range(len(mean_y_for_each_iteration)))
    plt.plot(indices_of_iterations, mean_y_for_each_iteration, color="red")
    plt.xlabel("Numer iteracji")
    plt.ylabel("Średnia wartość funkcji celu")
    plt.title(f"{plot_name}")

    plt.savefig(f"{path}/plot_{plot_name}.png")
    plt.close()
