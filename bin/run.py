from frr.core import FastReflectionRemoval
from frr.utils import FileWriter
import matplotlib.pyplot as plt
import argparse

def main(args):
    frr = FastReflectionRemoval(h=args.h, debug_writer=FileWriter(path="logs") if args.debug else None)

    # read image and normalize it into [0, 1]
    img = plt.imread(args.input_path) / 255

    # remove reflection
    result_img = frr.remove_reflection(img)

    # store image
    plt.imsave(args.output_path, result_img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", default=None, type=str)
    parser.add_argument("--output_path", default=None, type=str)
    parser.add_argument("--debug", action="store_true", default=None)

    parser.add_argument("--h", default=0.03, type=float)
    args = parser.parse_args()

    main(args)