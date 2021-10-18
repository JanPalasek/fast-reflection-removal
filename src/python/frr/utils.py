import os
import datetime
import matplotlib.pyplot as plt


class FileWriter:
    def __init__(self, path):
        self._path = path
        self._internal_counter = 0

        if not os.path.exists(path):
            os.makedirs(path)

    @property
    def path(self):
        return self._path

    def save_image(self, img, name=None, category="debug"):
        if name is None:
            # timestamp
            name = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S.%f') + str(self._internal_counter)

            self._internal_counter += 1

        dest = self._path + os.sep + f"{category}{'_' if name is not None and len(name) > 0 else ''}{name}.png"

        plt.imsave(dest, img)

    def save_plot(self, plot, name=None, category="debug", clean=False, dpi=200, extension="pdf"):
        if name is None:
            # timestamp
            name = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S.%f') + str(self._internal_counter)

            self._internal_counter += 1

        dest = self._path + os.sep + f"{category}{'_' if name is not None and len(name) > 0 else ''}{name}.{extension}"

        if clean:
            plot.axis("off")

        plot.savefig(dest, dpi=dpi, bbox_inches="tight")
        plot.clf()
