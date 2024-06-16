import sys
from argparse import Namespace

import cec2017.functions

import utils
from visualize_func import visualize
from differential_evolution import differential_evolution
from options import get_args


def main(args: Namespace) -> None:
    y_func = cec2017.functions.__dict__[args.y_func]

    if args.visualize_func:
        visualize(y_func)

    h, h_y = differential_evolution(args, y_func)
    utils.generate_results(args, h, h_y)


if __name__ == "__main__":
    args = get_args(sys.argv[1:])
    main(args)
