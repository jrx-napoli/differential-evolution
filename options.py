import argparse


def get_args(argv):
    parser = argparse.ArgumentParser()

    # general
    parser.add_argument('--y_func', type=str, default="f8")
    parser.add_argument('--x_min', type=float, default=-100.0)
    parser.add_argument('--x_max', type=float, default=100.0)
    parser.add_argument('--x_dim', type=int, default=2)
    parser.add_argument('--pop_size', type=int, default=100)
    parser.add_argument('--n_iterations', type=int, default=100)
    parser.add_argument('--f', type=float, default=0.8)
    parser.add_argument('--cr', type=float, default=0.9)
    parser.add_argument('--max_f', type=float, default=1.0)

    # msr
    parser.add_argument('--msr', default=False, action='store_true')
    parser.add_argument('--msr_alpha', type=float, default=0.01)

    # tpa
    parser.add_argument('--tpa', default=False, action='store_true')
    parser.add_argument('--tpa_alpha', type=float, default=0.0001)

    # other
    parser.add_argument('--visualize_func', default=False, action='store_true')

    return parser.parse_args(argv)
