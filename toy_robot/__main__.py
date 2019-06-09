import sys

from toy_robot.simulator import Simulator


def main():
    simulator = Simulator()

    for line in sys.stdin:
        simulator.run(line.strip('\n'))


if __name__ == "__main__":
    main()
