import numpy as np
from scipy import signal
from scipy.io import wavfile

from .auxiliary import int_to_bytes
from .constants import l


class Audio:
    def __init__(self, samplerate: int = 44100, length: int = l):
        self._samplerate = samplerate
        self._length = length

    def to_int(self, array: np.array) -> int:
        return int.from_bytes(array.tobytes(), 'big')

    def from_int(self, x: int) -> np.array:
        byte_data = int_to_bytes(x)
        array = np.array([byte for byte in byte_data], dtype=np.uint8)
        return self.pad(self.clamp(array))

    def save(self, array: np.array, path: str):
        wavfile.write(path, self._samplerate, array)

    def resample(self, array: np.array, samplerate: int) -> np.array:
        dtype = array.dtype
        samples = int(round((len(array) / samplerate) * self._samplerate))
        return signal.resample(array, samples).astype(dtype)

    def clamp(self, array: np.array) -> np.array:
        if len(array) > self._length:
            return array[:self._length]

        return array

    def convert(self, array: np.array) -> np.array:
        dtype = array.dtype
        if dtype == np.int16:
            return np.rint(array / 256).astype(np.uint8) + 128
        if dtype == np.int32:
            return np.rint((array / 16777216)).astype(np.uint8) + 128
        if dtype == np.float32:
            return np.rint(((array + 1.0) / 2.0) * 256).astype(np.uint8)

        return array

    def pad(self, array: np.array, value: int = 0, left: bool = True) -> np.array:
        padding = (self._length - len(array), 0) if left else (0, self._length - len(array))
        return np.pad(array, padding, 'constant', constant_values=value)

    def load(self, path: str) -> np.array:
        samplerate, array = wavfile.read(path)
        array = self.resample(array, samplerate)
        array = self.clamp(array)
        array = self.convert(array)
        array = self.pad(array, 128, left=False)
        return array
