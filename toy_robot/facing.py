from enum import Enum


class InvalidFacingDirectionException(Exception):
    pass


class FacingDirection(Enum):
    NORTH = 'NORTH'
    WEST = 'WEST'
    SOUTH = 'SOUTH'
    EAST = 'EAST'

    @classmethod
    def has_direction(cls, direction):
        return any(direction == item.value for item in cls)


class Facing(object):
    def __init__(self, direction):
        self.direction = direction

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        d = direction.strip()
        if not FacingDirection.has_direction(d):
            raise InvalidFacingDirectionException(
                f'Invalid facing direction {direction}.'
                )
        self._direction = direction
