import numpy as np

class BatchFloat64ArrayProxy:
    def __init__(self, batch, idx):
        self._batch = batch
        self._idx = idx
        self._lib = batch._api_util.lib

    def to_array(self):
        return self._batch._get_batch_float_prop(self._idx)

    def __call__(self):
        return self.to_array()

    def __len__(self):
        return len(self._batch)

    def __mul__(self, other):
        return self.to_array() * other

    def __truediv__(self, other):
        return self.to_array() / other

    def __floordiv__(self, other):
        return self.to_array() // other

    def __add__(self, other):
        return self.to_array() + other

    def __sub__(self, other):
        return self.to_array() - other

    def __array__(self):
        return self.to_array()

    def __iadd__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Float64(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Increment,
                other,
                0
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() + other
        data, data_ptr, _ = batch._prepare_float64_array(data)
        batch._lib.Batch_SetFloat64Array(
            *ptr_cnt,
            self._idx,
            data_ptr,
            0
        )
        batch._check_for_error()
        return self

    def __isub__(self, other):
        return self.__iadd__(-other)

    def __imul__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Float64(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Multiply,
                other,
                0
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() * other
        data, data_ptr, _ = batch._prepare_float64_array(data)
        batch._lib.Batch_SetFloat64Array(
            *ptr_cnt,
            self._idx,
            data_ptr,
            0
        )
        batch._check_for_error()
        return self

    def __idiv__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Float64(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Multiply,
                1 / other,
                0
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() / other
        data, data_ptr, _ = batch._prepare_float64_array(data)
        batch._lib.Batch_SetFloat64Array(
            *ptr_cnt,
            self._idx,
            data_ptr,
            0
        )
        batch._check_for_error()
        return self


class BatchInt32ArrayProxy:
    def __init__(self, batch, idx):#, kind):
        self._batch = batch
        self._idx = idx
        self._lib = batch._api_util.lib

    def to_array(self):
        return self._batch._get_batch_int32_prop(self._idx)

    def __call__(self):
        return self.to_array()

    def __len__(self):
        return len(self._batch)

    def __mul__(self, other):
        return self.to_array() * other

    def __truediv__(self, other):
        return self.to_array() / other

    def __floordiv__(self, other):
        return self.to_array() // other

    def __add__(self, other):
        return self.to_array() + other

    def __sub__(self, other):
        return self.to_array() - other

    def __array__(self):
        return self.to_array()

    def __iadd__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Int32(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Increment,
                other,
                0
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() + other
        data, data_ptr, _ = batch._api_util.prepare_int32_array(data)
        batch._lib.Batch_SetInt32Array(
            *ptr_cnt,
            self._idx,
            data_ptr,
            0
        )
        batch._check_for_error()
        return self

    def __isub__(self, other):
        return self.__iadd__(-other)

    def __imul__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Int32(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Multiply,
                other,
                0
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() * other
        data, data_ptr, _ = batch._prepare_int32_array(data)
        batch._lib.Batch_SetInt32Array(
            *ptr_cnt,
            self._idx,
            data_ptr,
            0
        )
        batch._check_for_error()
        return self

    def __idiv__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Int32(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Multiply,
                1 / other,
                0
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() / other
        data, data_ptr, _ = batch._prepare_int32_array(data)
        self._lib.Batch_SetInt32Array(
            *ptr_cnt,
            self._idx,
            data_ptr,
            0
        )
        batch._check_for_error()
        return self


__all__ = ('BatchFloat64ArrayProxy', 'BatchInt32ArrayProxy')