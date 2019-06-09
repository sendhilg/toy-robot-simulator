from io import StringIO
from unittest.mock import patch

from toy_robot.__main__ import main


@patch("toy_robot.simulator.Simulator.run", autospec=True)
def test_main_for_user_input(mock_simulator_run, monkeypatch):
    input_line = StringIO('1234\n')
    monkeypatch.setattr('sys.stdin', input_line)
    main()
    mock_simulator_run.assert_called_once()


@patch("toy_robot.simulator.Simulator.run", autospec=True)
def test_main_for_no_user_input(mock_simulator_run, monkeypatch):
    input_line = StringIO(None)
    monkeypatch.setattr('sys.stdin', input_line)
    main()
    mock_simulator_run.assert_not_called()
