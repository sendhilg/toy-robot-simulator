from toy_robot.coordinate import Coordinate, Table
from toy_robot.facing import Facing


class InvalidParametersForPlaceException(Exception):
    pass


class MissingPlaceCommandException(Exception):
    pass


class MoveOutOfBoundsException(Exception):
    pass


class Robot(object):
    def __init__(self):
        self.coordinate = None
        self.facing = None

    @property
    def coordinate(self):
        return self._coordinate

    @coordinate.setter
    def coordinate(self, coordinate):
        self._coordinate = coordinate

    @property
    def facing(self):
        return self._facing

    @facing.setter
    def facing(self, facing):
        self._facing = facing

    def place(self, params):
        if params and len(params) > 2:
            self.coordinate = Coordinate(params[0], params[1])
            self.facing = Facing(params[2])
        else:
            raise InvalidParametersForPlaceException(
                'Invalid number of parameters for PLACE.'
                )

    def move(self):
        """
        Move the robot one unit in the direction it is currently facing.
        Any move that will cause the robot to go out of bounds
        will raise an exception.
        """
        if not self.coordinate:
            raise MissingPlaceCommandException(
                'Cannot move robot until placed.'
                )

        if (self.facing.direction == 'NORTH'
                and self.coordinate.y < Table.MAX.value):
            self.coordinate.y += 1
        elif (self.facing.direction == 'SOUTH'
                and self.coordinate.y > Table.MIN.value):
            self.coordinate.y -= 1
        elif (self.facing.direction == 'EAST'
                and self.coordinate.x < Table.MAX.value):
            self.coordinate.x += 1
        elif (self.facing.direction == 'WEST'
                and self.coordinate.x != Table.MIN.value):
            self.coordinate.x -= 1
        else:
            raise MoveOutOfBoundsException(
                'Cannot move robot. Coordinates out of bound.'
                )

    def turn_left(self):
        """Turn the robot 90 degrees left from the current direction."""
        if not self.coordinate:
            raise MissingPlaceCommandException(
                'Cannot turn robot until placed.'
                )

        self.facing.direction = {
            'NORTH': 'WEST',
            'WEST': 'SOUTH',
            'SOUTH': 'EAST',
            'EAST': 'NORTH'
        }.get(self.facing.direction)

    def turn_right(self):
        """Turn the robot 90 degrees right from the current direction."""
        if not self.coordinate:
            raise MissingPlaceCommandException(
                'Cannot turn robot until placed.'
                )

        self.facing.direction = {
            'NORTH': 'EAST',
            'EAST': 'SOUTH',
            'SOUTH': 'WEST',
            'WEST': 'NORTH'
        }.get(self.facing.direction)

    def report(self):
        if not self.coordinate:
            raise MissingPlaceCommandException(
                'Cannot report on robot until placed.'
                )
        print(
            f'Output: {self.coordinate.x}, {self.coordinate.y}, '
            f'{self.facing.direction}'
            )

    def invoke(self, identifier, params):
        if identifier == 'PLACE':
            self.place(params)
        elif identifier == 'REPORT':
            self.report()
        elif identifier == 'LEFT':
            self.turn_left()
        elif identifier == 'RIGHT':
            self.turn_right()
        elif identifier == 'MOVE':
            self.move()
