from typing import Callable

from cec2017.functions import f8


FUNCTION: Callable = f8
X_MIN: float = -100
X_MAX: float = 100
X_DIM: int = 2

POPULATION_SIZE: int = 100

NUMBER_OF_ITERATIONS: int = 100

F: float = 0.8
CR: float = 0.9

MAX_F: float = 1.

USE_MSR: bool = True
MSR_F_ALPHA: float = 0.01

USE_TPA: bool = True
TPA_F_ALPHA: float = 0.0001
