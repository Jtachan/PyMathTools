# Matrix tools

`PymathTools` provides multiple classes to easily work with matrices.
Each class is named after the main case for what it is created.

## Generic Matrix

This class is intended for working with 2D matrices.
It is a quick wrapper to the `numpy.array()` function, providing an easy use for multiple solutions.

The class is available at the `pymath.instances.generic_matrix` module.

### `GenericMatrix(matrix: [np.NDArray | Tuple[Sequence[float], Sequence[float]])`

Class to be initialized for the desired 2-dimensional matrix.
The parameter `matrix` must hold either a 2D numpy array or a 2D matrix defined as a tuple.

```python
from src.pymath_tools.instances import GenericMatrix

mat = GenericMatrix(matrix=([1, 2], [3, 4]))
```

The resulting matrix supports the following math operations to other `GenericMatrix` instances:
* Sum and subtraction.
* Multiplication and division (also with float numbers).
* Comparison with a difference of `1e-6`.

#### `GenericMatrix.as_array`

Property that returns the matrix values as a numpy array.

#### `GenericMatrix.shape`

Property that returns the dimensions of the matrix, as `[rows, cols]`.
Analogous to `numpy.NDArray.shape`. 

#### `GenericMatrix.determinant`

Property that returns the determinant of the matrix.
The property raises a `DimensionError` if the matrix is not square.
Analogous to `numpy.linalg.det()`

#### `GenericMatrix.is_singular`

Property that returns a boolean, defining whether the matrix instance is or not singular.
A matrix is defined as singular if their determinant is 0.
Singular matrices do not have inverse.

#### `GenericMatrix.inverse`

Property that returns a new `GenericMatrix` instance, holding the inverse value of the matrix.
The property raises a `DimensionError` if the matrix is not square or a `SingularMatrixError` if the matrix is singular.
