from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene

def capa(screen):
    effects = [
        Cycle(
            screen,
            FigletText("SNAKE", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("WAY!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])
