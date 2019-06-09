from enum import Enum


class CommandNotFoundException(Exception):
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


class Command(object):

    def parse(self, line):
        split_line = line.split(None, 1)
        identifier = split_line[0] if len(split_line) > 0 else ""
        params_str = split_line[1] if len(split_line) > 1 else ""
        params = list(map(str.strip, params_str.split(',')))

        if CommandIdentifier.has_identifier(identifier):
            return identifier, params

        raise CommandNotFoundException(f'{identifier} command not found.')
