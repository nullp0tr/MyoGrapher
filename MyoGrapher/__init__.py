import pygame


class MyoGrapher(object):
    def __init__(self, width=1200, height=400):
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.last_values = []
        self.dlast_values = []

    def dplot(self, vals, shifts, colors):
        division_lines = 4
        drift = 5
        self.screen.scroll(-drift)
        self.screen.fill((0, 0, 0),
                         (self.width - drift, 0, self.width, self.height))

        for n, values in enumerate(vals):
            values = [val / float(shifts[n]) for val in values]
            if len(self.dlast_values) < len(vals):
                self.dlast_values.append(values)
                return

            for i, (u, v) in enumerate(zip(self.dlast_values[n], values)):
                pygame.draw.line(self.screen, colors[n],
                                (self.width - drift, int(
                                    self.height / division_lines * (
                                        i + 1 - u))),
                                (self.width, int(
                                    self.height / division_lines * (
                                        i + 1 - v))))
                pygame.draw.line(self.screen, (255, 255, 255),
                                 (self.width - drift, int(
                                     self.height / division_lines * (
                                         i + 1))),
                                 (self.width, int(
                                     self.height / division_lines * (
                                         i + 1))))
            self.dlast_values[n] = values

    def plot(self, values, drawlines=False, curve=True):
        if self.last_values is None:
            self.last_values = values
            return

        division_lines = len(values)
        drift = 5
        self.screen.scroll(-drift)
        self.screen.fill((0, 0, 0), (self.width - drift, 0, self.width, self.height))

        for i, (u, v) in enumerate(zip(self.last_values, values)):
            if drawlines:
                pygame.draw.line(self.screen, (0, 255, 0),
                                 (self.width - drift, int(self.height / division_lines * (i + 1 - u))),
                                 (self.width, int(self.height / division_lines * (i + 1 - v))))
                pygame.draw.line(self.screen, (255, 255, 255),
                                 (self.width - drift, int(self.height / division_lines * (i + 1))),
                                 (self.width, int(self.height / division_lines * (i + 1))))

            else:
                c = int(255 * max(0, min(1, v)))
                self.screen.fill((c, c, c), (self.width - drift, i * self.height / division_lines, drift,
                                             (i + 1) * self.height / division_lines - i * self.height / division_lines))

        if curve:
            self.last_values = values

        pygame.display.flip()

    def emg_plot(self, emg, shift=512, drawlines=False, curve=True):
        self.plot([e / float(shift) for e in emg], drawlines=drawlines, curve=curve)
