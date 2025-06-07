from typing import Self


class ScreenLimits:
    MAX_WIDTH = 1024
    MAX_HEIGHT = 768


class Point2D:

    __slots__ = ('_x', '_y')

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        if not (0 <= value <= ScreenLimits.MAX_WIDTH):
            raise ValueError(f"x должен быть между 0 и {ScreenLimits.MAX_WIDTH}")
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        if not (0 <= value <= ScreenLimits.MAX_HEIGHT):
            raise ValueError(f"y должен быть между 0 и {ScreenLimits.MAX_HEIGHT}")
        self._y = value

    def __eq__(self, other: Self) -> bool:
        return self._x == other._x and self._y == other._y

    def __str__(self) -> str:
        return f"Point2D({self._x}, {self._y})"

    def __repr__(self) -> str:
        return f"Point2D({self._x}, {self._y})"