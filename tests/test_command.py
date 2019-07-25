import pytest

from toy_robot.command import (Command, CommandIdentifier,
                               CommandNotFoundException, FacingDirection,
                               InvalidCoordinatesException,
                               InvalidFacingDirectionException,
                               InvalidParametersForPlaceException)


@pytest.mark.parametrize(
    'direction', ['TOP', 'BOTTOM']
)
def test_for_invalid_facing_direction(direction):
    assert FacingDirection.has_direction(direction) is False


@pytest.mark.parametrize(
    'direction', ['NORTH', 'SOUTH', 'WEST', 'EAST']
)
def test_for_valid_facing_direction(direction):
    assert FacingDirection.has_direction(direction) is True


@pytest.mark.parametrize(
    'identifier', ['INVALID_PLACE', 'INVALID_MOVE']
)
def test_command_identifier_for_invalid_identifiers(identifier):
    assert CommandIdentifier.has_identifier(identifier) is False


@pytest.mark.parametrize(
    'identifier', ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']
)
def test_command_identifier_for_valid_identifiers(identifier):
    assert CommandIdentifier.has_identifier(identifier) is True


@pytest.mark.parametrize(
    'line, identifier, params', [
        ('PLACE 0,0,NORTH', 'PLACE', [0, 0, 'NORTH']),
        ('MOVE', 'MOVE', ['']),
        ('LEFT', 'LEFT', ['']),
        ('RIGHT', 'RIGHT', ['']),
        ('REPORT', 'REPORT', ['']),
    ]
)
def test_command_parse_for_all_valid_commands(line, identifier, params):
    command = Command()
    i, p = command.parse(line)
    assert i == identifier
    assert p == params


@pytest.mark.parametrize(
    'line', ['INVALID_PLACE', 'INVALID_MOVE']
)
def test_command_parse_for_invalid_command(line):
    with pytest.raises(CommandNotFoundException) as e:
        command = Command()
        command.parse(line)
    assert str(e.value) == f'{line} command not found.'


def test_place_command_for_invalid_facing_direction():
    with pytest.raises(InvalidFacingDirectionException) as e:
        command = Command()
        command.parse('PLACE 0,0,TOP')
    assert str(e.value) == f'Invalid facing direction TOP.'


@pytest.mark.parametrize(
    'x', ['0', '1', '2', '3', '4', '5']
)
def test_validate_coordinates_for_permissible_digits(x):
    command = Command()
    x_coordinate, y_coordinate = command.validate_coordinates(x, 0)
    assert int(x) == x_coordinate
    assert int(0) == y_coordinate


@pytest.mark.parametrize(
    'x', ['A', 'a', 'B', 'b']
)
def test_validate_coordinates_for_non_digits(x):
    with pytest.raises(InvalidCoordinatesException) as e:
        command = Command()
        command.validate_coordinates(x, 0)
    assert str(e.value) == 'Coordinate values must be numbers.'


@pytest.mark.parametrize(
    'params', [None, ['0'], ['0', '0']]
)
def test_place_with_invalid_params(params):
    with pytest.raises(InvalidParametersForPlaceException) as e:
        command = Command()
        command.validate_place_command_params(params)
    assert str(e.value) == 'Invalid number of parameters for PLACE.'
