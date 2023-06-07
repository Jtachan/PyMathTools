"""
This unit test file checks the correct behavior of the functions and instances related
with temperature. As all the functions are used within the 'Temperature' class, only
that class is being directly tested.
"""
import pytest

from pymath_tools.instances import Temperature


@pytest.mark.parametrize(
    "celsius, kelvin, fahrenheit",
    ([0.0, 273.15, 32.0], [-273.15, 0.0, -459.67], [-17.78, 255.37, 0]),
)
def test_temperature_conversion(celsius: float, kelvin: float, fahrenheit: float):
    """
    Basic tests on creation and conversion of the temperature using the instance.
    The used values refer to 0 degrees in each temperature.
    """
    temp = Temperature.from_celsius(celsius_value=celsius)
    assert temp.kelvin == pytest.approx(
        kelvin, abs=1e-2
    ), "Failed conversion Celsius to Kelvin"
    assert temp.fahrenheit == pytest.approx(
        fahrenheit, abs=1e-2
    ), "Failed conversion Celsius to Fahrenheit"

    temp = Temperature.from_kelvin(kelvin_value=kelvin)
    assert temp.celsius == pytest.approx(
        celsius, abs=1e-2
    ), "Failed conversion Kelvin to Celsius"
    assert temp.fahrenheit == pytest.approx(
        fahrenheit, abs=1e-2
    ), "Failed conversion Kelvin to Fahrenheit"

    temp = Temperature.from_fahrenheit(fahrenheit_value=fahrenheit)
    assert temp.celsius == pytest.approx(
        celsius, abs=1e-2
    ), "Failed conversion Fahrenheit to Celsius"
    assert temp.kelvin == pytest.approx(
        kelvin, abs=1e-2
    ), "Failed conversion Fahrenheit to Kelvin"
