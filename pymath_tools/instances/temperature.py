"""
This module contains the 'Temperature' instance
"""
from __future__ import annotations

import pymath_tools.functions.temperature as temp_functions


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
