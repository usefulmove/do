#!/home/dedmonds/repos/do/.venv/bin/python
import sys
from time import sleep
from playsound3 import playsound

SOUND_PATH = '/home/dedmonds/repos/do/breathe.mp3'


def main():
    if not sys.argv[1:]:
        print("error: missing argument(s)")
        return

    try:
        focus_min: float = float(sys.argv[1]) * 60
    except ValueError:
        print("error: bad input")
        return

    if sys.argv[2:]:
        print(f"  focus: {sys.argv[2]}")

    sleep(focus_min)

    playsound(SOUND_PATH)

    print(f"  success: enjoy your day")


if __name__ == "__main__":
    main()
