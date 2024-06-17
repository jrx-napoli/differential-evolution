import random
import sys
from argparse import Namespace

import cec2017.functions
import numpy as np

import utils
from differential_evolution import differential_evolution
from options import get_args
from visualize_func import visualize


def main(args: Namespace) -> None:
    random.seed(args.seed)
    np.random.seed(args.seed)

    y_func = cec2017.functions.__dict__[args.y_func]

    if args.visualize_func:
        visualize(y_func)

    h, h_y = differential_evolution(args, y_func)
    utils.generate_results(args, h, h_y)


if __name__ == "__main__":
    args = get_args(sys.argv[1:])
    main(args)
