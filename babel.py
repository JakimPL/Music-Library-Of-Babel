import base64

from .auxiliary import int_to_bytes
from .constants import a, b, c


class Babel:
    def __init__(self):
        self._l = 0xa17fc
        self._w = 0xa17fc0
        self._k = 0x50bfe0

        self._m = 2 << (self._w - 1)
        self._mask = (2 << (self._k - 1)) - 1

        self._a = a
        self._b = b
        self._c = c

    def mask(self, x: int) -> int:
        return x & self._mask

    def encode_int(self, x: int) -> int:
        return ((self._a * x) + self._c) & self._mask

    @staticmethod
    def encode_base64(x: int) -> bytes:
        return base64.b64encode(int_to_bytes(x))

    @staticmethod
    def decode_base64(data: bytes) -> int:
        return int.from_bytes(base64.b64decode(data), 'big')

    def decode_int(self, y: int) -> int:
        return (self._b * (y - self._c)) & self._mask
