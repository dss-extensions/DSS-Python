import numpy as np
from typing import Union
try:
    import numpy.typing as npt
    ComplexArray = npt.NDArray[np.complex128]
    Float64Array = npt.NDArray[np.float64]
    Float32Array = npt.NDArray[np.float32]
    Int32Array = npt.NDArray[np.int32]
    Int8Array = npt.NDArray[np.int8]
    BoolArray = npt.NDArray[np.bool_]
except (ModuleNotFoundError, ImportError, AttributeError):
    from typing import List
    ComplexArray = List[complex]
    Float64Array = List[np.float64]
    Float32Array = List[np.float32]
    Int32Array = List[np.int32]
    Int8Array = List[np.int8]
    BoolArray = List[bool]

Float64ArrayOrComplexArray = Union[Float64Array, ComplexArray]
Float64ArrayOrSimpleComplex = Union[Float64Array, complex]
