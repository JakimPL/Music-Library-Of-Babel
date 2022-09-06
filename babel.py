import base64

from .auxiliary import int_to_bytes
from .constants import a, b, c


class Babel:
    def __init__(self):
        self._k = 0x50bfe0
        self._mask = (2 << (self._k - 1)) - 1

        self._a = a
        self._b = b
        self._c = c

        self._q = self._k // 8
        self._s = 4 * self._q
        self._w = (2 << (self._s - 1)) - 1
        self._z = self._w << self._s

    def swap(self, x: int) -> int:
        return ((x & self._w) << self._s) + ((x & self._z) >> self._s)

    def lcg(self, x: int) -> int:
        return ((self._a * x) + self._c) & self._mask

    def rlcg(self, y: int) -> int:
        return (self._b * (y - self._c)) & self._mask

    def mask(self, x: int) -> int:
        return x & self._mask

    def encode_int(self, x: int) -> int:
        return self.lcg(self.swap(x))

    @staticmethod
    def encode_base64(x: int) -> bytes:
        return base64.b64encode(int_to_bytes(x))

    @staticmethod
    def decode_base64(data: bytes) -> int:
        return int.from_bytes(base64.b64decode(data), 'big')

    def decode_int(self, y: int) -> int:
        return self.swap(self.rlcg(y))
