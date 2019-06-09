import pytest

from toy_robot.command import (Command, CommandIdentifier,
                               CommandNotFoundException)


@pytest.mark.parametrize(
    'identifier', ['INVALID_PLACE', 'INVALID_MOVE']
)
def test_command_for_invalid_identifiers(identifier):
    assert CommandIdentifier.has_identifier(identifier) is False


@pytest.mark.parametrize(
    'identifier', ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']
)
def test_command_for_valid_identifiers(identifier):
    assert CommandIdentifier.has_identifier(identifier) is True


@pytest.mark.parametrize(
    'line, identifier, params', [
        ('PLACE 0,0,NORTH', 'PLACE', ['0', '0', 'NORTH']),
        ('MOVE', 'MOVE', ['']),
        ('LEFT', 'LEFT', ['']),
        ('RIGHT', 'RIGHT', ['']),
        ('REPORT', 'REPORT', ['']),
    ]
)
def test_command_parse_for_valid_command(line, identifier, params):
    command = Command()
    i, p = command.parse(line)
    assert i == identifier
    assert p == params


@pytest.mark.parametrize(
    'line', ['INVALID_PLACE', 'INVALID_MOVE']
)
def test_command_parse_for_invalid_command(line):
    with pytest.raises(CommandNotFoundException):
        command = Command()
        command.parse(line)
