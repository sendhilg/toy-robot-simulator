import pytest

from toy_robot.facing import (Facing, FacingDirection,
                              InvalidFacingDirectionException)


@pytest.mark.parametrize(
    'direction', ['INVALID_NORTH', 'INVALID_SOUTH']
)
def test_invalid_facing_direction(direction):
    assert FacingDirection.has_direction(direction) is False


@pytest.mark.parametrize(
    'direction', ['NORTH', 'SOUTH', 'EAST', 'WEST']
)
def test_valid_facing_direction(direction):
    assert FacingDirection.has_direction(direction) is True


@pytest.mark.parametrize(
    'direction', ['INVALID_NORTH', 'INVALID_SOUTH']
)
def test_invalid_facing_direction_exception(direction):
    with pytest.raises(InvalidFacingDirectionException) as e:
        Facing(direction)
    assert str(e.value) == f'Invalid facing direction {direction}.'


def test_facing_attributes_and_values():
    facing = Facing('NORTH')
    assert hasattr(facing, 'direction')
    assert facing.direction == 'NORTH'
