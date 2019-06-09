from unittest.mock import patch

import pytest

from toy_robot.robot import (InvalidParametersForPlaceException,
                             MissingPlaceCommandException,
                             MoveOutOfBoundsException, Robot)


def test_robot_attributes():
    robot = Robot()
    assert hasattr(robot, 'coordinate')
    assert hasattr(robot, 'facing')


@patch("toy_robot.robot.Robot.place", autospec=True)
def test_invoke_for_place(mock_place):
    robot = Robot()
    robot.invoke('PLACE', ['0', '0', 'NORTH'])
    mock_place.assert_called_once_with(robot, ['0', '0', 'NORTH'])


@patch("toy_robot.robot.Robot.move", autospec=True)
def test_invoke_for_move(mock_move):
    robot = Robot()
    robot.invoke('MOVE', None)
    mock_move.assert_called_once_with(robot)


@patch("toy_robot.robot.Robot.turn_left", autospec=True)
def test_invoke_for_turn_left(mock_turn_left):
    robot = Robot()
    robot.invoke('LEFT', None)
    mock_turn_left.assert_called_once_with(robot)


@patch("toy_robot.robot.Robot.turn_right", autospec=True)
def test_invoke_for_turn_right(mock_turn_right):
    robot = Robot()
    robot.invoke('RIGHT', None)
    mock_turn_right.assert_called_once_with(robot)


@patch("toy_robot.robot.Robot.report", autospec=True)
def test_invoke_for_report(mock_report):
    robot = Robot()
    robot.invoke('REPORT', None)
    mock_report.assert_called_once_with(robot)


@pytest.mark.parametrize(
    'params', [None, ['0'], ['0', '0']]
)
def test_place_with_invalid_params(params):
    with pytest.raises(InvalidParametersForPlaceException) as e:
        robot = Robot()
        robot.place(params)
    assert str(e.value) == 'Invalid number of parameters for PLACE.'


def test_place_with_valid_params():
    robot = Robot()
    robot.place(['0', '0', 'NORTH'])
    assert robot.coordinate.x == 0
    assert robot.coordinate.y == 0
    assert robot.facing.direction == 'NORTH'


def test_move_on_robot_not_placed():
    with pytest.raises(MissingPlaceCommandException) as e:
        robot = Robot()
        robot.move()
    assert str(e.value) == 'Robot not placed.'
    assert robot.coordinate is None
    assert robot.coordinate is None
    assert robot.facing is None


@pytest.mark.parametrize(
    'input_params, x, y, direction', [
        (['0', '0', 'NORTH'], 0, 1, 'NORTH'),
        (['0', '1', 'SOUTH'], 0, 0, 'SOUTH'),
        (['0', '0', 'EAST'], 1, 0, 'EAST'),
        (['1', '0', 'WEST'], 0, 0, 'WEST'),
    ]
)
def test_move_on_robot_placed(input_params, x, y, direction):
    robot = Robot()
    robot.place(input_params)
    robot.move()
    assert robot.coordinate.x == x
    assert robot.coordinate.y == y
    assert robot.facing.direction == direction


@pytest.mark.parametrize(
    'input_params, x, y, direction', [
        (['0', '0', 'SOUTH'], 0, 0, 'SOUTH'),
        (['0', '0', 'WEST'], 0, 0, 'WEST'),
        (['5', '0', 'EAST'], 5, 0, 'EAST'),
        (['5', '0', 'SOUTH'], 5, 0, 'SOUTH'),
        (['5', '5', 'NORTH'], 5, 5, 'NORTH'),
        (['5', '5', 'EAST'], 5, 5, 'EAST'),
        (['0', '5', 'NORTH'], 0, 5, 'NORTH'),
        (['0', '5', 'WEST'], 0, 5, 'WEST'),
    ]
)
def test_move_for_robot_out_of_bounds(input_params, x, y, direction):
    with pytest.raises(MoveOutOfBoundsException) as e:
        robot = Robot()
        robot.place(input_params)
        robot.move()
    assert str(e.value) == 'Cannot move robot. Coordinates out of bound.'
    assert robot.coordinate.x == x
    assert robot.coordinate.y == y
    assert robot.facing.direction == direction


def test_turn_left_on_robot_not_placed():
    with pytest.raises(MissingPlaceCommandException) as e:
        robot = Robot()
        robot.turn_left()
    assert str(e.value) == 'Robot not placed.'
    assert robot.coordinate is None
    assert robot.coordinate is None
    assert robot.facing is None


@pytest.mark.parametrize(
    'input_params, expected_direction', [
        (['0', '0', 'NORTH'], 'WEST'),
        (['0', '0', 'SOUTH'], 'EAST'),
        (['0', '0', 'EAST'], 'NORTH'),
        (['0', '0', 'WEST'], 'SOUTH'),
    ]
)
def test_turn_left_on_robot_placed(input_params, expected_direction):
    robot = Robot()
    robot.place(input_params)
    robot.turn_left()
    assert robot.facing.direction == expected_direction


def test_turn_right_on_robot_not_placed():
    with pytest.raises(MissingPlaceCommandException) as e:
        robot = Robot()
        robot.turn_right()
    assert str(e.value) == 'Robot not placed.'
    assert robot.coordinate is None
    assert robot.coordinate is None
    assert robot.facing is None


@pytest.mark.parametrize(
    'input_params, expected_direction', [
        (['0', '0', 'NORTH'], 'EAST'),
        (['0', '0', 'SOUTH'], 'WEST'),
        (['0', '0', 'EAST'], 'SOUTH'),
        (['0', '0', 'WEST'], 'NORTH'),
    ]
)
def test_turn_right_on_robot_placed(input_params, expected_direction):
    robot = Robot()
    robot.place(input_params)
    robot.turn_right()
    assert robot.facing.direction == expected_direction


def test_report_on_robot_not_placed():
    with pytest.raises(MissingPlaceCommandException) as e:
        robot = Robot()
        robot.report()
    assert str(e.value) == 'Robot not placed.'
    assert robot.coordinate is None
    assert robot.coordinate is None
    assert robot.facing is None


def test_report_on_robot_placed(capsys):
    robot = Robot()
    robot.place(['0', '0', 'NORTH'])
    robot.report()
    assert robot.coordinate.x == 0
    assert robot.coordinate.y == 0
    assert robot.facing.direction == 'NORTH'
    captured = capsys.readouterr()
    assert captured.out.replace('\n', '') == 'Output: 0, 0, NORTH'
