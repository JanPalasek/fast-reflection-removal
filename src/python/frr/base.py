import numpy as np
from typing import Tuple
from scipy.fftpack import dct, idct

def gradient(A: np.ndarray, append_zeros=False) -> Tuple[np.ndarray]:
    """
    Computes gradients of input numpy array. Returns tuple, where the first
    part is gradient in direction of axis 0 (rows), then axis 1 (columns),...

    Args:
        f (np.ndarray): Input numpy array.

    Returns:
        Returns tuple of numpy arrays denoting gradients in different directions.
    """
    
    rows, cols = A.shape
    
    grad_x = np.zeros_like(A)
    grad_x[:, 0: cols - 1] = np.diff(A, axis=1)

    grad_y = np.zeros_like(A)
    grad_y[0:rows - 1, :] = np.diff(A, axis=0)

    B = np.concatenate((grad_x[..., np.newaxis], grad_y[..., np.newaxis]), axis=-1)

    return B

def divergence(A):
    m, n, _ = A.shape
    B = np.zeros(shape=(m, n))

    T = A[:, :, 0]
    T1 = np.zeros(shape=(m, n))
    T1[:, 1:n] = T[:, 0:n-1]

    B = B + T - T1

    T = A[:, :, 1]
    T1 = np.zeros(shape=(m, n))
    T1[1:m, :] = T[0:m-1, :]

    B = B + T - T1
    return B


def laplacian(f, h: float = None):
    rows, cols = f.shape
    dims = 2

    grads = gradient(f)

    if h is not None:
        # remove edges (gradients) smaller than 0
        # norm = np.sqrt(np.sum(grads * grads, axis=-1))
        norm = np.linalg.norm(grads, axis=-1)
        
        mask = (norm < h)[..., np.newaxis].repeat(dims, axis=-1)
        grads[mask] = 0
    
    # and compute its divergence by summing the second-order gradients
    laplacian = divergence(grads)
    
    return laplacian


def dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

def idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')
