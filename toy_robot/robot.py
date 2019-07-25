from enum import Enum


class MissingPlaceCommandException(Exception):
    pass


class MoveOutOfBoundsException(Exception):
    pass


class Table(Enum):
    MIN = 0
    MAX = 5


def is_robot_placed(decorated_func):
    def placed(self):
        if self.x_coordinate is None or self.y_coordinate is None:
            raise MissingPlaceCommandException('Robot not placed.')
        decorated_func(self)
    return placed


class Robot(object):
    def __init__(self):
        self.x_coordinate = None
        self.y_coordinate = None
        self.facing = None

    def place(self, params):
        self.x_coordinate = params[0]
        self.y_coordinate = params[1]
        self.facing = params[2]

    @is_robot_placed
    def move(self):
        """
        Move the robot one unit in the direction it is currently facing.
        Any move that will cause the robot to go out of bounds
        will raise an exception.
        """
        if self.facing == 'NORTH' and self.y_coordinate < Table.MAX.value:
            self.y_coordinate += 1
        elif self.facing == 'SOUTH' and self.y_coordinate > Table.MIN.value:
            self.y_coordinate -= 1
        elif self.facing == 'EAST' and self.x_coordinate < Table.MAX.value:
            self.x_coordinate += 1
        elif self.facing == 'WEST' and self.x_coordinate != Table.MIN.value:
            self.x_coordinate -= 1
        else:
            raise MoveOutOfBoundsException(
                'Cannot move robot. Coordinates out of bound.')

    @is_robot_placed
    def turn_left(self):
        """Turn the robot 90 degrees left from the current direction."""
        self.facing = {
            'NORTH': 'WEST',
            'WEST': 'SOUTH',
            'SOUTH': 'EAST',
            'EAST': 'NORTH'
        }.get(self.facing)

    @is_robot_placed
    def turn_right(self):
        """Turn the robot 90 degrees right from the current direction."""
        self.facing = {
            'NORTH': 'EAST',
            'EAST': 'SOUTH',
            'SOUTH': 'WEST',
            'WEST': 'NORTH'
        }.get(self.facing)

    @is_robot_placed
    def report(self):
        print(
            f'Output: {self.x_coordinate}, {self.y_coordinate}, {self.facing}'
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
