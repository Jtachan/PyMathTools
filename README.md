# Pymath Instances

`pymath` offers python classes, to be used as instances, for math purposes. The instances presented at the package are:

- [`GenericMatrix`](#genericmatrix): 2-Dimensional matrix usage

## Why should I use pymath?

**Sanity checks**
<br/>Each class contains sanity checks to be performed in the background for math operators as well as for the class definition.

**Cleaner code**
<br/>By the use of these instances, the math operations result in shorter and cleaner code. Take the following example:
````python
# Matrix multiplication: numpy approach
import numpy as np
mat_a = np.array(...)
mat_b = np.array(...)
mat_c = np.array(...)

result = np.matmul(mat_a, np.matmul(mat_b, mat_c))

# Matrix multiplication: pymath approach
from pymath import GenericMatrix
mat_a = GenericMatrix(...)
mat_b = GenericMatrix(...)
mat_c = GenericMatrix(...)

result = mat_a * mat_b * mat_c
````

**Compatibility**
<br/>All classes contain code compatibility to each other through the call of inner instances.
Compatibility with `numpy` is also present, containing all classes the property `as_array`, which returns its numpy representation.

## Classes/Instances

### GenericMatrix

`GenericMatrix` allows easy 2D matrix usage as python instances.
A new matrix can be defined by feeding the class the numpy array as value.

The instance allows the **basic matrix operations**:
* Multiply the matrix by and `int` or `float`
* Sum, subtract and multiply operations by other matrices

It also contains the following properties:
* ``GenericMatrix.inverse``: returns the inverse of the matrix (only available for squared matrices)
* `GenericMatrix.shape`: Analogous to `np.shape`
* `GenericMatrix.as_array`: Returns the numpy array representation of the matrix.
````python
import numpy as np
from pymath import GenericMatrix

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
