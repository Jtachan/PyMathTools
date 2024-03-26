"""
This module contains exceptions and errors to be raised among the instances.
These errors are not to be added to __init__.py
"""


class DimensionError(ValueError):
    """Invalid dimensions"""


class SingularMatrixError(ValueError):
    """Raised for invalid matrix properties in singular matrices"""
