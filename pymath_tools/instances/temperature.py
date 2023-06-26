"""
This module contains the 'Temperature' instance
"""
from __future__ import annotations

from typing import Literal

import pymath_tools.functions.temperature as temp_functions


class Temperature:
    """
    This class stores allows easy initialization from any temperature unit and provides
    properties to also read it at any unit.
    """

    __slots__ = ("__celsius",)

    def __init__(
        self,
        value: float,
        scale: Literal["celsius", "c", "kelvin", "k", "fahrenheit", "f"],
    ):
        """
        Initializes the class from the value of a temperature. The scale of the
        temperature must also be defined.

        Parameters
        ----------
        value: float
            The temperature value.
        scale: str
            The temperature scale in which the value is defined. It should be the
            full name of the scale in lowercase ('celsius', 'kelvin' or 'fahrenheit')
            or their initials ('c', 'k', 'f')
        """
        if scale in ("kelvin", "k"):
            self.__celsius = temp_functions.kelvin_to_celsius(value)
        elif scale in ("fahrenheit", "f"):
            self.__celsius = temp_functions.fahrenheit_to_celsius(value)
        else:
            self.__celsius = value

    @classmethod
    def from_celsius(cls, celsius_value: float) -> Temperature:
        """
        Initializes the class from the value of a Celsius temperature.

        Parameters
        ----------
        celsius_value: float
            The temperature specified in Kelvin.
        """
        return cls(value=celsius_value, scale="c")

    @classmethod
    def from_fahrenheit(cls, fahrenheit_value: float) -> Temperature:
        """
        Initializes the class from the value of a Fahrenheit temperature.

        Parameters
        ----------
        fahrenheit_value: float
            The temperature specified in Fahrenheit.
        """
        return cls(value=fahrenheit_value, scale="f")

    @classmethod
    def from_kelvin(cls, kelvin_value: float) -> Temperature:
        """
        Initializes the class from the value of a Kelvin temperature.

        Parameters
        ----------
        kelvin_value: float
            The temperature specified in Kelvin.
        """
        return cls(value=kelvin_value, scale="k")

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

    def __repr__(self) -> str:
        return f"{self.celsius} °C, {self.fahrenheit} °F, {self.kelvin} °K"
