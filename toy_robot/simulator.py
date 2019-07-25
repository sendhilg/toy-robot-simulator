from .command import (Command, CommandNotFoundException,
                      InvalidCoordinatesException,
                      InvalidFacingDirectionException,
                      InvalidParametersForPlaceException)
from .robot import (MissingPlaceCommandException, MoveOutOfBoundsException,
                    Robot)


class Simulator(object):
    def __init__(self):
        self.command = Command()
        self.robot = Robot()

    def run(self, line):
        is_successful = True
        try:
            identifier, params = self.command.parse(line)
        except (
            CommandNotFoundException,
            InvalidParametersForPlaceException,
            InvalidFacingDirectionException,
            InvalidCoordinatesException,
        ) as e:
            print(f'Error processing {line}: {e}')
            is_successful = False
        else:
            try:
                self.robot.invoke(identifier, params)
            except (
                MoveOutOfBoundsException,
                MissingPlaceCommandException,
            ) as e:
                print(f'Error processing command {identifier}: {e}')
                is_successful = False
        return is_successful
