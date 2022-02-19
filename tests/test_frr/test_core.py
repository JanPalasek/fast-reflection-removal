# pylint: disable=redefined-outer-name

import os
import pytest
from frr.core import FastReflectionRemoval
import numpy as np
from matplotlib import image


@pytest.fixture(params=[0.11])
def h(request) -> int:
    """
    H parameter for `FastReflectionRemoval` class.
    """
    return request.param


@pytest.fixture
def input_img() -> np.ndarray:
    """
    Input image to the test.
    """
    return image.imread("tests/test_frr/fixtures/toy_example.jpg") / 255


@pytest.fixture
def expected_img():
    """
    Expected image to the test.
    """
    return image.imread("tests/test_frr/fixtures/toy_example_out.jpg") / 255


def test_remove_reflection(h: int, input_img: np.ndarray, expected_img: np.ndarray, tmpdir):
    """
    A simple integration test to test `FastReflectionRemoval` algorithm.

    Args:
        h (int): The main parameter of `FastReflectionRemoval`.
        input_img (np.ndarray): Input image.
        expected_img (np.ndarray): Expected img.
    """
    instance = FastReflectionRemoval(h=h)
    actual_img = instance.remove_reflection(input_img)

    # hack: store and load output - otherwise I couldn't make them equal
    tmp_out_path = os.path.join(tmpdir, "out.jpg")
    image.imsave(tmp_out_path, actual_img)
    actual_img = image.imread(tmp_out_path) / 255

    assert actual_img.shape == expected_img.shape
    np.testing.assert_almost_equal(actual=actual_img, desired=expected_img, decimal=7)
