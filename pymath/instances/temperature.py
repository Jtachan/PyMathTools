"""
This module contains the 'Temperature' instance
"""
from __future__ import annotations

from typing import Union

import pymath.functions.temperature as temp_functions


class Temperature:
    """
    This class stores allows easy initialization from any temperature unit and provides
    properties to also read it at any unit.
    """

    __slots__ = "__celsius"

    def __init__(self, celsius: float):
        """
        Initializes the class from the value of a Celsius temperature.

        Parameters
        ----------
        celsius: float
            The temperature specified in Celsius degrees.
        """
        self.__celsius = celsius

    @classmethod
    def from_kelvin(cls, kelvin: float) -> Temperature:
        """
        Initializes the class from the value of a Kelvin temperature.

        Parameters
        ----------
        kelvin: float
            The temperature specified in Kelvin.
        """
        return cls(temp_functions.kelvin_to_celsius(kelvin))

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> Temperature:
        """
        Initializes the class from the value of a Fahrenheit temperature.

        Parameters
        ----------
        fahrenheit: float
            The temperature specified in Fahrenheit.
        """
        return cls(temp_functions.fahrenheit_to_celsius(fahrenheit))

    @property
    def celsius(self) -> float:
        """float: The value of the measurement in Celsius"""
        return self.__celsius

    @property
    def fahrenheit(self) -> float:
        """float: The value of the measurement in Fahrenheit"""
        return temp_functions.celsius_to_fahrenheit(self.__celsius)

    @property
    def kelvin(self) -> float:
        """float: The value of the measurement in Kelvin"""
        return temp_functions.celsius_to_kelvin(self.__celsius)

    def __add__(self, other: Union[Temperature, float]) -> Temperature:
        """
        Allows addition to other values, which must be specified in Celsius.

        Parameters
        ----------
        other: Temperature or float
            Celsius degrees to add to the original class.

        Returns
        -------
        Temperature:
            New instance with the final value.
        """
        if isinstance(other, Temperature):
            other = Temperature.celsius

        return Temperature(self.__celsius + other)
