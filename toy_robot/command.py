from enum import Enum


class CommandNotFoundException(Exception):
    pass


class InvalidParametersForPlaceException(Exception):
    pass


class InvalidCoordinatesException(Exception):
    pass


class InvalidFacingDirectionException(Exception):
    pass


class CommandIdentifier(Enum):
    PLACE = 'PLACE'
    MOVE = 'MOVE'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    REPORT = 'REPORT'

    @classmethod
    def has_identifier(cls, identifier):
        return any(identifier == item.value for item in cls)


class FacingDirection(Enum):
    NORTH = 'NORTH'
    WEST = 'WEST'
    SOUTH = 'SOUTH'
    EAST = 'EAST'

    @classmethod
    def has_direction(cls, direction):
        return any(direction == item.value for item in cls)


class Command(object):

    def parse(self, line):
        split_line = line.split(None, 1)
        identifier = split_line[0] if len(split_line) > 0 else ""
        params_str = split_line[1] if len(split_line) > 1 else ""
        params = list(map(str.strip, params_str.split(',')))

        if not CommandIdentifier.has_identifier(identifier):
            raise CommandNotFoundException(f'{identifier} command no no not found.')

        if identifier == 'PLACE':
            params = self.validate_place_command_params(params)

        return identifier, params

    def validate_place_command_params(self, params):
        if params and len(params) > 2:
            x, y = self.validate_coordinates(params[0], params[1])
            facing = self.validate_facing(params[2])
        else:
            raise InvalidParametersForPlaceException(
                'Invalid number of parameters for PLACE.'
            )
        return [x, y, facing]

    def validate_coordinates(self, x, y):
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            raise InvalidCoordinatesException(
                'Coordinate values must be numbers.'
            )
        return x, y

    def validate_facing(self, direction):
        if not FacingDirection.has_direction(direction):
            raise InvalidFacingDirectionException(
                f'Invalid facing direction {direction}.'
            )
        return direction
