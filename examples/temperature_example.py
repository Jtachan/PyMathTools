"""
Small example code on how to work with the Temperature class
"""

import random

from src.pymath_tools.instances import Temperature

if __name__ == "__main__":
    t1 = Temperature(value=random.randint(0, 100), scale="celsius")
    print(f"This is the first initialized temperature:\n{t1}\n")

    t2 = Temperature.from_fahrenheit(random.randint(0, 100))
    print(f"The second temperature is {t2.fahrenheit} °F")
    print(f"The second temperature in Celsius is {t2.celsius} °C")

    t_diff = t2 - t1
    print(
        "\nThe difference among both temperatures (t2 - t1) is "
        f"{t_diff.celsius} °C  or {t_diff.fahrenheit} °F"
    )
    print(f"\nThe sum of both temperatures (t1 + t2) is:\n{t1 + t2}")
