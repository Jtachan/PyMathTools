# Temperature

In this document are detailed all functionalities that **Pymath Tools** offers for solutions oriented to work with temperature in one or multiple scales.

**Content**
- [Functions](#pymathtoolsfunctionstemperature)
  - [Celsius to Fahrenheit](#celsiustofahrenheitcelsius-float---float)
  - [Celsius to Kelvin](#celsiustokelvincelsius-float---float)
  - [Fahrenheit to Celsius](#fahrenheittocelsiusfahrenheit-float---float)
  - [Fahrenheit to Kelvin](#fahrenheittokelvinfahrenheit-float---float)
  - [Kelvin to Celsius](#kelvintocelsiuskelvin-float---float)
  - [Kelvin to Fahrenheit](#kelvintofahrenheitkelvin-float---float)
- [Temperature class](#pymathtoolsinstancestemperature-)
  - [Class method: from_celsius()](#temperaturefromcelsiuscelsiusvalue-float---temperature)
  - [Class method: from_fahrenheit()](#temperaturefromfahrenheitfahrenheitvalue-float---temperature)
  - [Class method: from_kelvin()](#temperaturefromkelvinkelvinvalue-float---temperature)
  - [Property: celsius](#temperaturecelsius---float)
  - [Property: fahrenheit](#temperaturefahrenheit---float)
  - [Property: kelvin](#temperaturekelvin---float)
  - [Example code]

## `pymath_tools.functions.temperature`

The package provides multiple functions to convert temperature among all the [temperature scales](https://en.wikipedia.org/wiki/Scale_of_temperature): Celsius, Fahrenheit and Kelvin.

#### `celsius_to_fahrenheit(celsius: float) -> float`

Takes a temperature measurement in Celsius and returns its equivalent in the Fahrenheit scale. 

```python
from pymath_tools.functions import celsius_to_fahrenheit
print(celsius_to_fahrenheit(37.0))
# '98.6' is printed
```

#### `celsius_to_kelvin(celsius: float) -> float`

Takes a temperature measurement in Celsius and returns its equivalent in the Kelvin scale. 

```python
from pymath_tools.functions import celsius_to_kelvin
print(celsius_to_kelvin(37.0))
# '310.15' is printed
```

#### `fahrenheit_to_celsius(fahrenheit: float) -> float`

Takes a temperature measurement in Fahrenheit and returns its equivalent in the Celsius scale.

```python
from pymath_tools.functions import fahrenheit_to_celsius
print(fahrenheit_to_celsius(98.6))
# '37.0' is printed
```

#### `fahrenheit_to_kelvin(fahrenheit: float) -> float`

Takes a temperature measurement in Fahrenheit and returns its equivalent in the Kelvin scale.
The function is equivalent to converting the value first to Celsius and then to Kelvin.

```python
from pymath_tools.functions import fahrenheit_to_kelvin
print(fahrenheit_to_kelvin(98.6))
# '310.15' is printed
```

#### `kelvin_to_celsius(kelvin: float) -> float`

Takes a temperature measurement in Kelvin and returns its equivalent in the Celsius scale.

```python
from pymath_tools.functions import kelvin_to_celsius
print(kelvin_to_celsius(310.15))
# '37.0' is printed
```

#### `kelvin_to_fahrenheit(kelvin: float) -> float`

Takes a temperature measurement in Kelvin and returns its equivalent in the Fahrenheit scale.
The function is equivalent to converting the value first to Celsius and then to Fahrenheit.

```python
from pymath_tools.functions import kelvin_to_celsius
print(kelvin_to_celsius(310.15))
# '98.6' is printed
```

## `pymath_tools.instances.temperature` 

The package also provides a class to create instances and use an easy wrapper for the functions.

### `Temperature(value: float, scale: str)`

Class to be initialized for any temperature scale.

- `value` must hold the temperature measurement. 
- `scale` must be a string that defines to which scale the temperature has been measured. The string must be either the scale in lowercase ('celsius', 'kelvin', 'fahrenheit') or the initial of the scale, also in lowercase ('c', 'k', 'f').

#### `Temperature.from_celsius(celsius_value: float) -> Temperature`

Initializes the class from a Celsius value.

#### `Temperature.from_fahrenheit(fahrenheit_value: float) -> Temperature`

Initializes the class from a Fahrenheit value.

#### `Temperature.from_kelvin(kelvin_value: float) -> Temperature`

Initializes the class from a Kelvin value.

#### `Temperature.celsius -> float`

Property that returns the value within the Celsius scale of the measurement hold within the class.

#### `Temperature.fahrenheit -> float`

Property that returns the value within the Celsius scale of the measurement hold within the class.

#### `Temperature.kelvin -> float`

Property that returns the value within the Celsius scale of the measurement hold within the class.

### Example code

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
