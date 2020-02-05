from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene

import keyboard

def capa(screen):
    effects = [
        Cycle(
            screen,
            FigletText("SNAKE WAY", font='big'),
            int(screen.height / 2 - 8)),
        # Cycle(
        #     screen,
        #     FigletText("WAY", font='big'),
        #     int(screen.height / 2 + 3)),
        Cycle(
            screen,
            FigletText("-----------", font='small'),
            int(screen.height / 2 + 4)),
        Cycle(
            screen,
            FigletText("Press Enter!", font='small'),
            int(screen.height / 2 + 8)),
        Cycle(
            screen,
            FigletText("-----------", font='small'),
            int(screen.height / 2 + 12)),    
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])

