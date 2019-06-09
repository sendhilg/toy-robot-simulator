from enum import Enum


class InvalidCoordinatesException(Exception):
    pass


class Table(Enum):
    MIN = 0
    MAX = 5


class Coordinate(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = self.validate_coordinate(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = self.validate_coordinate(value)

    def validate_coordinate(self, value):
        try:
            v = int(value)
        except ValueError:
            raise InvalidCoordinatesException(
                'Coordinate values must be numbers.'
                )

        if v < Table.MIN.value or v > Table.MAX.value:
            raise InvalidCoordinatesException(
                f'Coordinate values must be between '
                f'{Table.MIN.value} to '
                f'{Table.MAX.value}.'
                )

        return v
