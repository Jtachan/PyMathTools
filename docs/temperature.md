# Temperature

In this document are detailed all functionalities that **Pymath Tools** offers for solutions oriented to work with temperature in one or multiple scales.

## Functions

The package provides multiple functions to convert temperature among all the [temperature scales](https://en.wikipedia.org/wiki/Scale_of_temperature): Celsius, Fahrenheit and Kelvin.

#### `celsius_to_fahrenheit(celsius: float)`

Takes a temperature measurement in Celsius and returns its equivalent in the Fahrenheit scale.

```python
from src.pymath_tools.functions import celsius_to_fahrenheit

print(celsius_to_fahrenheit(37.0))
# '98.6' is printed
```

#### `celsius_to_kelvin(celsius: float)`

Takes a temperature measurement in Celsius and returns its equivalent in the Kelvin scale.

```python
from src.pymath_tools.functions import celsius_to_kelvin

print(celsius_to_kelvin(37.0))
# '310.15' is printed
```

#### `fahrenheit_to_celsius(fahrenheit: float)`

Takes a temperature measurement in Fahrenheit and returns its equivalent in the Celsius scale.

```python
from src.pymath_tools.functions import fahrenheit_to_celsius

print(fahrenheit_to_celsius(98.6))
# '37.0' is printed
```

#### `fahrenheit_to_kelvin(fahrenheit: float)`

Takes a temperature measurement in Fahrenheit and returns its equivalent in the Kelvin scale.
The function is equivalent to converting the value first to Celsius and then to Kelvin.

```python
from src.pymath_tools.functions import fahrenheit_to_kelvin

print(fahrenheit_to_kelvin(98.6))
# '310.15' is printed
```

#### `kelvin_to_celsius(kelvin: float)`

Takes a temperature measurement in Kelvin and returns its equivalent in the Celsius scale.

```python
from src.pymath_tools.functions import kelvin_to_celsius

print(kelvin_to_celsius(310.15))
# '37.0' is printed
```

#### `kelvin_to_fahrenheit(kelvin: float)`

Takes a temperature measurement in Kelvin and returns its equivalent in the Fahrenheit scale.
The function is equivalent to converting the value first to Celsius and then to Fahrenheit.

```python
from src.pymath_tools.functions import kelvin_to_celsius

print(kelvin_to_celsius(310.15))
# '98.6' is printed
```

## Temperature instance

The `Temperature` instances work as a wrapper for the functions, providing a continuous simple and easy usage of them.

It also provides the **operations** of sum and subtraction among other Temperature instances.
It is not allowed to add scalars as not all scales contain linearity among each other.

### `Temperature(value: float, scale: Literal['celsius', 'c', 'kelvin', 'k', 'fahrenheit', 'f'])`

Class to be initialized for any temperature scale.

- `value` must hold the temperature measurement. 
- `scale` must be a string that defines to which scale the temperature has been measured. The string must be either the scale in lowercase ('celsius', 'kelvin', 'fahrenheit') or the initial of the scale, also in lowercase ('c', 'k', 'f').

#### `Temperature.from_celsius(celsius_value: float)`

Initializes the class from a Celsius value.

#### `Temperature.from_fahrenheit(fahrenheit_value: float)`

Initializes the class from a Fahrenheit value.

#### `Temperature.from_kelvin(kelvin_value: float)`

Initializes the class from a Kelvin value.

#### `Temperature.celsius`

Property that returns the value within the Celsius scale of the measurement hold within the class.

#### `Temperature.fahrenheit`

Property that returns the value within the Celsius scale of the measurement hold within the class.

#### `Temperature.kelvin`

Property that returns the value within the Celsius scale of the measurement hold within the class.

### Example code

```python
from src.pymath_tools.instances import Temperature

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
