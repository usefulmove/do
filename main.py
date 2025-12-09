#!/usr/bin/env python
from pathlib import Path
from random import randint
import sys
from time import sleep
from playsound3 import playsound
from rich.console import Console


SOUND_FILE: str = 'breathe.mp3'


# console colors
CDIM: str = '#616161'
CEMPH: str = '#faf6e4'
CNORM: str = 'default'
CERR: str = '#ff0000'
CWARN: str = '#fff670'


console = Console()


messages: tuple[str, ...] = (
    'return to yourself',
    'let go',
    'breathe',
    'continue',
    'be one with the river',
    'attention softens, clarity returns',
    'what you tended now tends you',
    'carry no burden',
    'love',
    'empty your hands',
    'be without being',
    'let the moment rest',
    'soften with each breath',
    'let the moment occur',
    'the way opens as you do',
    'allow the next step to take you',
    'listen to your silence',
    'lean into stillness',
    'hold nothing',
    'what is is enough',
    'be gentle',
    'it starts now',
    'pause',
    'empty your step',
    'be the breeze',
    'be what is',
    'open',
    'fear is the illusion',
)


def main() -> None:
    if not sys.argv[1:]:
        console.print(f"  [{CERR}]error[/{CERR}]: missing argument(s)")
        return

    try:
        focus_min: float = float(sys.argv[1]) * 60
    except ValueError:
        console.print(f"  [{CERR}]error[/{CERR}]: bad input")
        return

    if sys.argv[2:]:
        focus_note: str = ' '.join(sys.argv[2:])
        console.print(f"  [{CDIM}]focus:[/{CDIM}] [{CEMPH}]{focus_note}[/{CEMPH}]")

    sleep(focus_min)

    playsound(SOUND_FILE)

    message: str = messages[randint(0, len(messages) - 1)]

    console.print(f"  [{CDIM}]done:[/{CDIM}] \"[{CNORM}]{message}[/{CNORM}]\"")


if __name__ == "__main__":
    main()
