"""
This module contains the GenericMatrix class
"""
from __future__ import annotations

from typing import Iterator, Sequence, Tuple, Union

import numpy as np
import numpy.typing as npt


class GenericMatrix:
    """
    Class to work as a wrapper for numpy to work with 2-dimensional matrices
    """

    __slots__ = ["__matrix"]

    def __init__(self, matrix: npt.NDArray):
        """
        Inits the GenericMatrix

        Parameters
        ----------
        matrix: numpy N-dimensional array
            Matrix defined as a numpy array
        """
        if not isinstance(matrix, np.ndarray):
            raise TypeError(
                "The given matrix must be initially defined as a numpy array"
            )
        if len(matrix.shape) != 2:
            raise ValueError(
                "The given matrix does not specifies the dimension "
                "requirement. Please, confirm you have given an NxM matrix."
            )

        self.__matrix = np.asarray(matrix, dtype=float)

    def __str__(self) -> str:
        return str(self.__matrix)

    def __iter__(self) -> Iterator[float]:
        """
        Enables iteration over all matrix's elements
        """
        for element in self.__matrix:
            yield element

    def __add__(self, other: Union[GenericMatrix, npt.NDArray]) -> GenericMatrix:
        """
        Enables the sum through the '+' operand

        Parameters
        ----------
        other: GenericMatrix or numpy N-dimensional array
            Second matrix to which will take place at the sum

        Returns
        -------
        GenericMatrix:
            Matrix instance with the final sum value.
        """
        if isinstance(other, GenericMatrix):
            other = other.as_array
        elif not isinstance(other, np.ndarray):
            raise TypeError(f"Unsupported type '{type(other)}' for sum operator")

        if self.shape != other.shape:
            raise ValueError("Cannot sum matrices with different shape")

        return GenericMatrix(self.__matrix + other)

    def __sub__(self, other: Union[GenericMatrix, npt.NDArray]) -> GenericMatrix:
        """
        Enables the subtraction through the '-' character

        Parameters
        ----------
        other: GenericMatrix or numpy N-dimensional array
            Second matrix to which will take place at the subtraction

        Returns
        -------
        GenericMatrix:
            Matrix instance with the final subtracted value.
        """
        if isinstance(other, GenericMatrix):
            other = other.as_array
        elif not isinstance(other, np.ndarray):
            raise TypeError(f"Unsupported type '{type(other)}' for sum operator")

        if self.shape != other.shape:
            raise ValueError("Cannot sum matrices with different shape")

        return GenericMatrix(self.__matrix - other)

    def __mul__(
        self, other: Union[int, float, npt.NDArray, GenericMatrix]
    ) -> GenericMatrix:
        """
        Enables the multiplication operator '*' for GenericMatrix instances

        Parameters
        ----------
        other: int, float, numpy array or GenericMatrix
            Element to multiply the matrix.

        Returns
        -------
        GenericMatrix:
            Instance with the result of the multiplication
        """
        if not isinstance(other, (int, float, np.ndarray, GenericMatrix)):
            raise TypeError(
                f"Unsupported type '{type(other)}' for multiplication operator"
            )

        if isinstance(other, (int, float)):
            return GenericMatrix(matrix=self.__matrix * other)

        if self.shape[1] != other.shape[0]:
            raise ValueError(
                "Cannot multiply the given matrices, due their shapes are not "
                "(A, N) and (N, B)."
            )

        if isinstance(other, GenericMatrix):
            other = other.as_array

        return GenericMatrix(matrix=np.matmul(self.__matrix, other))

    def __truediv__(
        self, other: Union[npt.NDArray, GenericMatrix, float, int]
    ) -> GenericMatrix:
        """
        Enables division through the operand '/'

        Parameters
        ----------
        other
            Element to divide the matrix. It can be a number (float or int) or
            another matrix, stored as a numpy array or GenericMatrix instance.
        """
        if isinstance(other, (float, int)):
            return GenericMatrix(self.__matrix / other)
        elif isinstance(other, np.ndarray):
            # This will raise any error for any non-2D matrix
            other = GenericMatrix(other)

        return self * other.inverse

    def __eq__(self, other: Union[npt.NDArray, GenericMatrix]) -> bool:
        """
        Enables the rich comparison with other matrices

        Parameters
        ----------
        other: numpy array or GenericMatrix
            Element to be compared

        Returns
        -------
        bool:
            Weather if the matrices are the same or not
        """
        if (
            not isinstance(other, (np.ndarray, GenericMatrix))
            or self.shape != other.shape
        ):
            return False

        for self_row, other_row in zip(self, other):
            for self_element, other_element in zip(self_row, other_row):
                if abs(self_element - other_element) > 1e-6:
                    return False

        return True

    def __getitem__(
        self, item: Union[int, Tuple[int, int]]
    ) -> Union[npt.NDArray, float]:
        return self.__matrix[item]

    def __setitem__(
        self, key: Union[int, Tuple[int, int]], value: Union[npt.NDArray, float]
    ):
        if isinstance(key, int) and not isinstance(value, np.ndarray):
            raise ValueError(
                f"Type value '{type(value)}' was given, but expected "
                f"'np.ndarray' for coordinate '{key}'"
            )
        elif isinstance(key, Sequence) and not isinstance(value, (int, float)):
            raise ValueError(
                f"Type value '{type(value)}' was given, but expected "
                f"'float' for coordinate '{key}'"
            )

        self.__matrix[key] = value

    @property
    def as_array(self) -> npt.NDArray:
        """numpy array: Current matrix as a numpy array"""
        return self.__matrix

    @property
    def shape(self) -> Tuple[int, int]:
        """tuple: Matrix dimensions organized as [rows, cols]"""
        return self.__matrix.shape

    @property
    def inverse(self) -> GenericMatrix:
        """GenericMatrix: Inverse of the given matrix"""
        if self.shape[0] != self.shape[1]:
            raise ValueError("The inverse matrix is only valid for square matrices")

        return GenericMatrix(matrix=np.linalg.inv(self.__matrix))
