import base64

from auxiliary import int_to_bytes
from constants import a, b, c


class Babel:
    def __init__(self):
        self._l = 0xa17fc
        self._w = 0xa17fc0
        self._k = self._w // 2

        self._m = 2 << (self._w - 1)
        self._mask = (2 << (self._k - 1)) - 1

        self._a = a
        self._b = b
        self._c = c

    def mask(self, x: int) -> int:
        return x & self._mask

    def lcg(self, x: int):
        return ((self._a * x) + self._c) % self._m

    def encode_int(self, seed: int) -> int:
        return self.mask(self.lcg(seed))

    @staticmethod
    def encode_base64(x: int) -> str:
        return base64.b64encode(int_to_bytes(x))

    @staticmethod
    def decode_base64(string: str) -> int:
        return int.from_bytes(base64.b64decode(string), 'big')

    def decode_int(self, y: int) -> int:
        return self.mask(b * (y - c))
