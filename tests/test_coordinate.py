import pytest

from toy_robot.coordinate import Coordinate, InvalidCoordinatesException


@pytest.mark.parametrize(
    'x', ['0', '1', '2', '3', '4', '5']
)
def test_validate_coordinate_for_permissible_digits(x):
    coorodinate = Coordinate()
    v = coorodinate.validate_coordinate(x)
    assert isinstance(v, int) is True


@pytest.mark.parametrize(
    'x', ['-1', '-2', '6', '7']
)
def test_validate_coordinate_for_non_permissible_digits(x):
    with pytest.raises(InvalidCoordinatesException) as e:
        coorodinate = Coordinate()
        coorodinate.validate_coordinate(x)
    assert str(e.value) == 'Coordinate values must be between 0 to 5.'


@pytest.mark.parametrize(
    'x', ['A', 'a', 'B', 'b']
)
def test_validate_coordinate_for_non_digits(x):
    with pytest.raises(InvalidCoordinatesException) as e:
        coorodinate = Coordinate()
        coorodinate.validate_coordinate(x)
    assert str(e.value) == 'Coordinate values must be numbers.'


def test_coordinate_attributes_and_values():
    coorodinate = Coordinate(0, 0)
    assert hasattr(coorodinate, 'x')
    assert hasattr(coorodinate, 'y')
    assert coorodinate.x == 0
    assert coorodinate.y == 0
