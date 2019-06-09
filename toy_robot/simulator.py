from toy_robot.command import Command, CommandNotFoundException
from toy_robot.coordinate import InvalidCoordinatesException
from toy_robot.facing import InvalidFacingDirectionException
from toy_robot.robot import (
    InvalidParametersForPlaceException,
    MissingPlaceCommandException,
    MoveOutOfBoundsException,
    Robot,
)


class Simulator(object):
    def __init__(self):
        self.command = Command()
        self.robot = Robot()

    def run(self, line):
        is_successful = True
        try:
            identifier, params = self.command.parse(line)
        except CommandNotFoundException as e:
            print(f'Error processing {line}: {e}')
            is_successful = False
        else:
            try:
                self.robot.invoke(identifier, params)
            except (
                MoveOutOfBoundsException,
                MissingPlaceCommandException,
                InvalidParametersForPlaceException,
                InvalidFacingDirectionException,
                InvalidCoordinatesException
            ) as e:
                print(f'Error processing command {identifier}: {e}')
                is_successful = False
        return is_successful
