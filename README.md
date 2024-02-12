# Status note

The project is currently frozen. I have other projects to finish first.

The following changes are to be performed to bring this project back to life:

- [ ] Update package files to use '.toml' instead of 'setup.py'
- [ ] Simplify usage & docs
- [ ] Use Sphinx instead of mkdocs
- [ ] Update logic of classes/functions to use CPython

# Pymath Tools

This is a personal project to generate functions and classes using as much CPython as possible.
The goal of the project is to obtain proficiency with:

- CPython
- Sphinx
- GitHub actions

# Pymath Tools Documentation

![Badge](https://github.com/Jtachan/PyMathTools/actions/workflows/unittests.yml/badge.svg)

`PymathTools` provides functions and instances for simple and easy use of math at any python code.

## Why should I use Pymath Tools?

**Simple usage**

The tool is very simple to use due to:
* Very clear functions, named as their purpose
* Instances providing elementary usage and/or magnitude conversions

Due to those reasons, `PymathTools` is also perfect for academic/learning purposes.

```python
from pymath_tools.instances import Temperature

measure = Temperature.from_fahrenheit(365)
print(f"Preheat the oven to {measure.fahrenheit} °F ({measure.celsius} °C) for baking the cake")
# Preheat the oven to 365.0 °F (185.0 °C) for baking the cake
```

## Content

* [Matrix](matrix.md)
* [Temperature](temperature.md)
