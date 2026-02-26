import numpy as np
try:
    import numpy.typing as npt
    # TODO: update after these are closed:
    # - https://github.com/numpy/numpy/issues/16544
    # - https://github.com/python/typing/issues/516

    ComplexMatrix = npt.NDArray[np.complex128]
    Float64Matrix = npt.NDArray[np.float64]
    Float32Matrix = npt.NDArray[np.float32]
    Int32Matrix = npt.NDArray[np.int32]
    ComplexArray = npt.NDArray[np.complex128]
    Float64Array = npt.NDArray[np.float64]
    Float32Array = npt.NDArray[np.float32]
    Int32Array = npt.NDArray[np.int32]
    Int8Array = npt.NDArray[np.int8]
    BoolArray = npt.NDArray[np.bool_]
except (ModuleNotFoundError, ImportError, AttributeError):
    from typing import List
    ComplexMatrix = List[complex]
    Float64Matrix = List[np.float64]
    Float32Matrix = List[np.float32]
    Int32Matrix = List[np.int32]
    ComplexArray = List[complex]
    Float64Array = List[np.float64]
    Float32Array = List[np.float32]
    Int32Array = List[np.int32]
    Int8Array = List[np.int8]
    BoolArray = List[bool]

Complex = complex
