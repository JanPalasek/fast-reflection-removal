from datetime import datetime
import pytest
from frr.base import divergence, gradient, laplacian
import numpy as np

@pytest.mark.parametrize(["input", "expected"],
[
    pytest.param(
        np.array([
            [1, 2, 4, 5],
            [4, 8, 16, 14],
            [5, 12, 10, 3],
            [3, 5, 2, 3]
        ]),
        (
            # axis 0
            np.array([
                [ 1.,  2.,  1.,  0.],
                [ 4.,  8., -2.,  0.],
                [ 7., -2., -7.,  0.],
                [ 2., -3.,  1.,  0.]
            ]),
            # axis 1
            np.array([
                [  3.,   6.,  12.,   9.],
                [  1.,   4.,  -6., -11.],
                [ -2.,  -7.,  -8.,   0.],
                [  0.,   0.,   0.,   0.]
            ])
        ),
        id="basic 2D"
    )
])
def test_gradient(input, expected):
    actual = gradient(input)

    np.testing.assert_almost_equal(actual[..., 0], expected[0])
    np.testing.assert_almost_equal(actual[..., 1], expected[1])

@pytest.mark.parametrize(["input", "expected"],
[
    pytest.param(
        np.array((
            # axis 0
            np.array([
                [ 1.,  2.,  1.,  0.],
                [ 4.,  8., -2.,  0.],
                [ 7., -2., -7.,  0.],
                [ 2., -3.,  1.,  0.]
            ]),
            # axis 1
            np.array([
                [  3.,   6.,  12.,   9.],
                [  1.,   4.,  -6., -11.],
                [ -2.,  -7.,  -8.,   0.],
                [  0.,   0.,   0.,   0.]
            ])
        )).transpose(1, 2, 0),
        np.array([
            [  4.,   7.,  11.,   8.],
            [  2.,   2., -28., -18.],
            [  4., -20.,  -7.,  18.],
            [  4.,   2.,  12.,  -1.]
        ]),
        id="basic 2D"
    ),
])
def test_divergence(input, expected):
    actual = divergence(input)
    np.testing.assert_almost_equal(actual, expected)


@pytest.mark.parametrize(["input", "h", "expected"],
[
    pytest.param(
        np.array([
            [1, 2],
            [4, 8]
        ]),
        None,
        np.array([
            [  4.,   5.],
            [  1., -10.]
        ]),
        id="basic 2D"
    )
])
def test_laplacian(input, h, expected):
    actual = laplacian(input, h=h)

    np.testing.assert_almost_equal(actual, expected)
