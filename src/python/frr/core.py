from frr.base import dct2, idct2, laplacian
from frr.utils import FileWriter
import numpy as np
import scipy
import matplotlib.pyplot as plt


class FastReflectionRemoval():
    """
    An instance of this class is able to remove reflections from specified image.
    """

    def __init__(self, h: float, lmbd: float = 0, mu: float = 1, epsilon: float = 1e-8, debug_writer: FileWriter = None):
        if not (0 <= h <= 1):
            raise ValueError(f"Value of 'h' must be between 0 and 1 (included). Recommended values are between 0 and 0.13.")
        if not (0 <= lmbd <= 1):
            raise ValueError(f"Value of 'lmbd' must be between 0 and 1 (included). Recommended value is 0.")
        if not (0 <= mu <= 1):
            raise ValueError(f"Value of 'mu' must be between 0 and 1 (included). Recommended value is 1.")

        self.h = h
        self.lmbd = lmbd
        self.epsilon = epsilon
        self.mu = mu

        self.debug_writer = debug_writer

    def remove_reflection(self, image: np.ndarray) -> np.ndarray:
        """
        Removes reflection from specified image.

        Args:
            image (np.ndarray): Image represented as numpy array of shape (H, W, C), where H is height, W is width and C is channels.
            The image is expected to have values in the interval [0, 1].

        Returns:
            np.ndarray: Returns image with removed reflections with values between 0 and 1.
        """
        if not np.all((0 <= image) & (image <= 1)):
            raise ValueError("Input image doesn't have all values between 0 and 1.")
        if len(image.shape) != 3:
            raise ValueError("Input image must have 3 dimensions.")
        
        channels = image.shape[-1]

        # iteratively compute for each channel individually
        # L(div(\delta_h(\grad Y)))
        # from eq (7)
        laplacians = np.zeros(shape=image.shape)
        for c in range(channels):
            lapl1 = laplacian(image[..., c], h=self.h)
            lapl2 = laplacian(lapl1)
            laplacians[:, :, c] = lapl2

            if self.debug_writer:
                plt.gray()
                self.debug_writer.save_image(lapl2, name=f"{c}", category="laplacian")

        
        if self.debug_writer:
            lapl_out = np.interp(laplacians, (laplacians.min(), laplacians.max()), (0, +1))
            plt.gray()
            self.debug_writer.save_image(lapl_out, name="all", category="laplacian")

        # computes right-hand side of equation (7)
        # L(...) + \epsilon * Y
        rhs = laplacians + self.epsilon * image

        if self.debug_writer:
            rhs_out = np.interp(rhs, (rhs.min(), rhs.max()), (0, 1))
            self.debug_writer.save_image(rhs_out, name="", category="rhs")

        T = np.zeros(shape=image.shape)

        # perform Poisson DCT to solve partial differential eq
        for c in range(channels):
            rhs_slice = rhs[..., c]

            M, N = rhs_slice.shape

            # create matrix kappa, where kappa_{mn} = 2 * [cos((pi * m) / M) + cos((pi * n) / N) - 2]
            m = np.cos((np.pi * np.arange(M)) / M)
            n = np.cos((np.pi * np.arange(N)) / N)
            kappa = 2 * (np.add.outer(m, n) - 2)

            if self.debug_writer:
                self.debug_writer.save_image(kappa, name=f"{c}", category="kappa")

            const = self.mu * (kappa ** 2) - self.lmbd * kappa + self.epsilon

            if self.debug_writer:
                self.debug_writer.save_image(const, name=f"{c}", category="denominator")

            u = dct2(rhs_slice)

            u = u / const
            u = idct2(u)

            T[..., c] = u

            if self.debug_writer:
                self.debug_writer.save_image(const, name=f"{c}", category=f"T")

        # scale back to the interval [0, 1]
        T = np.interp(T, (T.min(), T.max()), (0, +1))

        if self.debug_writer:
            self.debug_writer.save_image(T, name="", category="out")

        return T