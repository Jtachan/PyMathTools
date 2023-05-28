"""
This module contains function related with temperature
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Takes a Celsius value and returns its equivalent in Fahrenheit.

    Parameters
    ----------
    celsius: float
        The given temperature in Celsius.

    Returns
    -------
    float:
        The equivalent of the given temperature in Fahrenheit.
    """
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Takes a Fahrenheit value and returns its equivalent in Celsius.

    Parameters
    ----------
    fahrenheit: float
        The given temperature in Fahrenheit.

    Returns
    -------
    float:
        The equivalent of the given temperature in Celsius.
    """
    return fahrenheit - 32 * 5 / 9

def celsius_to_kelvin(celsius: float) -> float:
    """
    Takes a Celsius value and returns its equivalent in Kelvin.

    Parameters
    ----------
    celsius: float
        The given temperature in Celsius.

    Returns
    -------
    float:
        The equivalent of the given temperature in Kelvin.
    """
    return celsius + 273.15

def kelvin_to_celsius(kelvin: float) -> float:
    """
    Takes a Kelvin value and returns its equivalent in Celsius.

    Parameters
    ----------
    kelvin: float
        The given temperature in Kelvin.

    Returns
    -------
    float:
        The equivalent of the given temperature in Celsius.
    """
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """
    Takes a Fahrenheit value and returns its equivalent in Kelvin.

    Parameters
    ----------
    fahrenheit: float
        The given temperature in Fahrenheit.

    Returns
    -------
    float:
        The equivalent of the given temperature in Kelvin.
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """
    Takes a Kelvin value and returns its equivalent in Fahrenheit.

    Parameters
    ----------
    kelvin: float
        The given temperature in Kelvin.

    Returns
    -------
    float:
        The equivalent of the given temperature in Fahrenheit.
    """
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))
