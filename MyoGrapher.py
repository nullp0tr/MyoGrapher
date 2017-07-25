import pygame
from pygame.locals import *

class MyoGrapher(object):
    def __init__(self):
        self.width, self.height = 1200, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.last_values = None

    def plot(self, values, drawLines=False):
        if self.last_values is None:
            self.last_values = values
            return

        D = 5
        self.screen.scroll(-D)
        self.screen.fill((0, 0, 0), (self.width - D, 0, self.width, self.height))

        for i, (u, v) in enumerate(zip(self.last_values, values)):
            if drawLines:
                pygame.draw.line(self.screen, (0, 255, 0),
                                (self.width - D, int(self.height/8 * (i+1 - u))),
                                (self.width, int(self.height/8 * (i+1 - v))))
                pygame.draw.line(self.screen, (255,255,255),
                                (self.width - D, int(self.height/8 * (i+1))),
                                (self.width, int(self.height/8 * (i+1))))

            else:
                c = int(255 * max(0, min(1, v)))
                self.screen.fill((c, c, c), (self.width - D, i * self.height / 8, D, (i + 1) * self.height / 8 - i * self.height / 8))

        pygame.display.flip()
        last_values = values

    def emg_plot(self, emg):
        self.plot([e / 2000. for e in emg])
