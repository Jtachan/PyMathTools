# PyMath Tools

`Pymath Tools` contains instances and functions for easy use and unit conversion at any script.
The following are the modules it contains:

* [GenericMatrix](#genericmatrix)
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
pip install -e .
```

Once it is installed, access the content by importing from `pymath_tools.functions` or `pymath_tools.instances`:

## Modules

### GenericMatrix

`GenericMatrix` allows easy 2D matrix usage as python instances.
A new matrix can be defined by feeding the class the numpy array as value.

The instance allows the **basic matrix operations**:
* Multiply and divide the matrix by and `int` or `float`
* Sum, subtract, multiply and divide operations by other matrices

It also contains the following properties:
* `GenericMatrix.inverse`: returns the inverse of the matrix (only available for squared matrices)
* `GenericMatrix.shape`: Analogous to `np.shape`
* `GenericMatrix.as_array`: Returns the numpy array representation of the matrix.
````python
import numpy as np
from pymath_tools.instances import GenericMatrix

mat_1 = GenericMatrix(matrix=np.array([[1, 2], [3, 4]]))
mat_2 = GenericMatrix(np.array([[6, 7], [8, 9]]))

print(mat_1 * 2)
# [[2. 4.]
#  [6. 8.]]

print(mat_1 * mat_2)
# [[22. 25.]
#  [50. 57.]]

print(mat_1 + mat_2)
# [[ 7.  9.]
#  [11. 13.]]

print(mat_2 - mat_1)
# [[5. 5.]
#  [5. 5.]]
````

### Temperature

The `temperature` module allows easy use and conversion among temperature scales. 
To do so, the `Temperature` class can be used by specifying its value and the scale in which the value is defined.

`pymath_tools.instances.Temperature(value: float, scale: Literal[str])`

* `value`: Value of the temperature to initialize.
* `scale`: Temperature scale for the value to be initialized. It must be either the scale's name in lowercase ("celsius", "kelvin" or "fahrenheit") or their initials ("c", "k" or "f").

Temperature instances can also be initialized by the following classmethods:

* `Temperature.from_celsius(celsius_value: float)`: Initializes a `Temperature` instance from the specified Celsius value.
* `Temperature.from_kelvin(kelvin_value: float)`: Initializes a `Temperature` instance from the specified Kelvin value.
* `Temperature.from_fahrenheit(fahrenheit_value: float)`: Initializes a `Temperature` instance from the specified Fahrenheit value.

At last, other scales from the same temperature can be obtained with the **properties**:

* `Temperature.celsius`: Returns the float value of the initialized temperature in Celsius.
* `Temperature.kelvin`: Returns the float value of the initialized temperature in Kelvin.
* `Temperature.fahrenheit`: Returns the float value of the initialized temperature in Fahrenheit.

```python
from pymath_tools.instances import Temperature

temperature = Temperature(value=100, scale="celsius")
print(temperature.celsius)  # This prints '100.0'
print(temperature.kelvin)  # This prints '373.15'
print(temperature.fahrenheit)  # This prints '212.0'

temperature = Temperature.from_celsius(24.0)
print(temperature.celsius)  # This prints '24.0'
temperature = Temperature.from_kelvin(297.15)
print(temperature.celsius)  # This prints '24.0'
temperature = Temperature.from_fahrenheit(75.2)
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
