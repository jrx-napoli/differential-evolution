from typing import List, Tuple

from matplotlib import pyplot as plt
import numpy as np

from differential_evolution import differential_evolution


def main() -> None:
    h, h_y = differential_evolution()

    # Wypisanie do konsoli informacji o najlepszym punkcie wygenerowanym w ostatniej iteracji
    best_point_last_iteration, best_point_last_iteration_y = get_best_point_from_last_iteration(h, h_y)
    print("Najlepszy punkt wygenerowany w ostatniej iteracji:")
    print(f"Punkt: {best_point_last_iteration}")
    print(f"Wartość funkcji celu: {best_point_last_iteration_y}")

    # Wygenerowanie i wyświetlenie wykresu zależności średniej wartości funkcji celu wygenerowanych punktów od numeru iteracji
    create_and_show_plot_of_mean_y_for_each_iteration(h_y)


def get_best_point_from_last_iteration(h: List[List[np.ndarray]], h_y: List[List[float]]) -> Tuple[np.ndarray, float]:
    p_last_iteration = h[-1]
    y_last_iteration = h_y[-1]
    max_y_idx = np.argmax(y_last_iteration)
    return p_last_iteration[max_y_idx], y_last_iteration[max_y_idx]


def create_and_show_plot_of_mean_y_for_each_iteration(h_y: List[List[float]]) -> None:
    h_y_np = np.array(h_y)
    mean_y_for_each_iteration = np.mean(h_y_np, axis=1)
    indices_of_iterations = list(range(len(mean_y_for_each_iteration)))
    plt.plot(indices_of_iterations, mean_y_for_each_iteration, color="red")
    plt.xlabel("Numer iteracji")
    plt.ylabel("Średnia wartość funkcji celu\nwygenerowanych punktów")
    plt.title("Zależność średniej wartości funkcji celu\nwygenerowanych punktów od numeru iteracji")
    plt.show()


if __name__ == "__main__":
    main()
