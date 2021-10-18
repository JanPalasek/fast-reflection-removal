from datetime import datetime
import pytest
from frr.core import FastReflectionRemoval
import numpy as np
import scipy
from matplotlib import image

@pytest.mark.parametrize(["instance", "input", "expected"],
[
    pytest.param(
        FastReflectionRemoval(h=0.11),
        image.imread("tests/test_frr/toy_example.jpg"),
        None,
        id="toy_example.jpg"
    ),
])
def test_remove_reflection(instance: FastReflectionRemoval, input: np.ndarray, expected):
    input = (input / 255)
    image.imsave("tests/test_frr/input.jpg", input)
    actual = instance.remove_reflection(input)

    assert actual.shape == input.shape
    image.imsave("tests/test_frr/output.jpg", actual)