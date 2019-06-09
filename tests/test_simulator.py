import pytest

from toy_robot.simulator import Simulator


@pytest.mark.parametrize(
    'line', [
        'PLACE 0,0,NORTH',
        'PLACE 5,5,NORTH',
        ]
)
def test_run_for_valid_line(line):
    simulator = Simulator()
    is_successful = simulator.run(line)
    assert is_successful is True


@pytest.mark.parametrize(
    'line', [
        'INVALID PLACE',
        'INVALID MOVE',
        'PLACE',
        ]
)
def test_run_for_invalid_line(line):
    simulator = Simulator()
    is_successful = simulator.run(line)
    assert is_successful is False
