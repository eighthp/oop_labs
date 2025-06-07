from typing import Self, Generator
import math
from point2d import Point2D, ScreenLimits

class Vector2D:

    __slots__ = ('_x', '_y')

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @classmethod
    def from_points(cls, start: Point2D, end: Point2D) -> Self:
        return cls(end.x - start.x, end.y - start.y)

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        self._y = value

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self._x
        elif index == 1:
            return self._y
        raise IndexError("Индекс может быть только 0 или 1")

    def __setitem__(self, index: int, value: float) -> None:
        if index == 0:
            self._x = value
        elif index == 1:
            self._y = value
        else:
            raise IndexError("Индекс может быть только 0 или 1")

    def __iter__(self) -> Generator[float, None, None]:
        yield self._x
        yield self._y

    def __len__(self) -> int:
        return 2

    def __abs__(self) -> float:
        return math.hypot(self._x, self._y)

    def __add__(self, other: Self) -> Self:
        return Vector2D(self._x + other._x, self._y + other._y)

    def __sub__(self, other: Self) -> Self:
        return Vector2D(self._x - other._x, self._y - other._y)

    def __mul__(self, scalar: float) -> Self:
        return Vector2D(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar: float) -> Self:
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> Self:
        return Vector2D(self._x / scalar, self._y / scalar)

    def dot(self, other: Self) -> float:
        return self._x * other._x + self._y * other._y

    @staticmethod
    def dot_product(v1: Self, v2: Self) -> float:
        return v1.dot(v2)

    def cross(self, other: Self) -> float:
        return self._x * other._y - self._y * other._x

    @staticmethod
    def cross_product(v1: Self, v2: Self) -> float:
        return v1.cross(v2)

    def triple_product(self, v2: Self, v3: Self) -> float:
        return self.dot(Vector2D.cross_product(v2, v3))

    def __str__(self) -> str:
        return f"Vector2D({self._x}, {self._y})"

    def __repr__(self) -> str:
        return f"Vector2D({self._x}, {self._y})"