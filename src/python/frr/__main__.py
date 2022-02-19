
import click

from frr import FastReflectionRemoval
import matplotlib.pyplot as plt


@click.command()
@click.argument("input-path", type=click.Path())
@click.argument("output-path", type=click.Path())
@click.option("-h", default=0.03, type=click.FloatRange(0, 1), help="Measures how strong reflection removal is going to be. Higher h means stronger dereflection.")
@click.option("--debug", is_flag=True, help="If True, then the debug outputs are printed into out/.")
def main(input_path, output_path, h, debug):
    debug_writer = None
    if debug:
        from frr.utils import FileWriter
        debug_writer=FileWriter(path="logs")
    frr = FastReflectionRemoval(h=h, debug_writer=debug_writer)

    # read image and normalize it into [0, 1]
    img = plt.imread(input_path) / 255

    # remove reflection
    result_img = frr.remove_reflection(img)

    # store image
    plt.imsave(output_path, result_img)



if __name__ == "__main__":
    main()
