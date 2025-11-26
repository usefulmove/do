#!/usr/bin/env python3
import sys
from time import sleep
from playsound3 import playsound


SOUND_PATH = './breathe.mp3'


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

    print(f"  success: enjoy your day")

    playsound(SOUND_PATH)


if __name__ == "__main__":
    main()
