"""
Test module for GenericMatrix
"""
from random import randint

import numpy as np
import pytest
from pymath import GenericMatrix


@pytest.mark.parametrize(
    "np_matrix",
    (
        np.array([[1, 2], [3, 4]]),
        np.array([[0.3, 0.7], [3, 4]]),
    ),
)
def test_equal_method(np_matrix):
    """
    Testing non-math operators, such as 'iter()' or '=='
    """
    pymath_matrix = GenericMatrix(matrix=np_matrix)

    # Check all elements (one by one) are initialized correctly
    for np_element, pymath_element in zip(np_matrix, pymath_matrix):
        assert pymath_element == pytest.approx(np_element)

    # Check operand '==' works for numpy array and GenericMatrix classes
    assert pymath_matrix == np_matrix
    twin_matrix = GenericMatrix(matrix=np_matrix)
    assert pymath_matrix == twin_matrix


@pytest.mark.parametrize(
    "mat_a, mat_b",
    [
        (
            np.array(
                [[randint(-5, 5), randint(-5, 5)], [randint(-5, 5), randint(-5, 5)]]
            ),
            np.array(
                [[randint(-5, 5), randint(-5, 5)], [randint(-5, 5), randint(-5, 5)]]
            ),
        )
    ],
)
def test_assert_math_operands(mat_a, mat_b):
    """
    Test for all valid math operands, that is:
        * Sum and subtraction
        * Matrix multiplication
        * number multiplication (by the right)
    """
    gen_mat_a = GenericMatrix(mat_a)
    gen_mat_b = GenericMatrix(mat_b)

    assert gen_mat_a + gen_mat_b == mat_a + mat_b
    assert gen_mat_a - gen_mat_b == mat_a - mat_b

    assert gen_mat_a * 1.5 == mat_a * 1.5
    assert gen_mat_a * gen_mat_b == np.matmul(mat_a, mat_b)
