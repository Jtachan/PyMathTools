# PyMath Tools

`Pymath Tools` contains instances and functions for easy use and unit conversion at any script.
The following are the modules it contains:

* [Temperature](#temperature)

## Setup and usage

The package's latest release can be installed via pip.
```commandline
pip install git+https://github.com/Jtachan/py-coding-hints.git
```

The `develop` branch, containing all the latest unreleased changes, can also be installed with the following command:
```commandline
pip install git+https://github.com/Jtachan/py-coding-hints.git@develop
```

As an alternative, the repository can be cloned and locally installed.
```commandline
pip install -e
```

Once it is installed, access the content by importing from `pymath_tools.functions` or `pymath_tools.instances`:

## Modules
### Temperature

The `temperature` module allows easy use and conversion among temperature. 
To do so, the `Temperature` class can be used:

```python
from pymath_tools.instances import Temperature

temperature = Temperature(celsius=100)
print(temperature.kelvin)  # This prints '373.15'
print(temperature.fahrenheit)  # This prints '212.0'
```

While the instance is mainly initialized with Celsius degrees, it also allows the initialization from Fahrenheit and Kelvin:

```python
from pymath_tools.instances import Temperature

temperature = Temperature.from_kelvin(kelvin=297.15)
print(temperature.celsius)  # This prints '24.0'
temperature = Temperature.from_fahrenheit(fahrenheit=75.2)
print(temperature.celsius)  # This prints '24.0'
```

As an alternative, functions to convert among magnitudes can also be imported from `pymath_tools.functions`.
The available functions are:
- `celsius_to_fahrenheit(celsius: float)`: Converts a Celsius value into its equivalent in Fahrenheit.
- `celsius_to_kelvin(celsius: float)`: Converts a Celsius value into its equivalent in Kelvin.
- `fahrenheit_to_celsius(fahrenheit: float)`: Converts a Fahrenheit value into its equivalent in Celsius.
- `fahrenheit_to_kelvin(fahrenheit: float)`: Converts a Fahrenheit value into its equivalent in Kelvin.
- `kelvin_to_celsius(kelvin: float)`: Converts a Kelvin value into its equivalent in Celsius.
- `kelvin_to_fahrenheit(kelvin: float)`: Converts a Kelvin value into its equivalent in Fahrenheit.
