import pygame
import Colours
import time


class Progress:
    def __init__(self):
        self.done = False
        self.image = pygame.Surface((50, 20))

    def Display(self):
        if self.done == True:
            self.image.fill(Colours.Accent)
        else:
            self.image.fill(Colours.Gray)

        return self.image

    def Done(self):
        self.done = True

class timer:
    def __init__(self, Screen):
        self.blocks = []
        for i in range(12):
            self.blocks.append(Progress())
        self.screen = Screen
        self.Mins = 0

    def Update(self):
        self.seconds = time.time()
        self.NMins = self.seconds/60
        DT = self.NMins - self.Mins
        if DT % 5 == 0:
            self.blocks[DT/5].Done()

        print(DT)

    def Start(self):
        self.seconds = time.time()
        self.Mins = self.seconds/60

    def Display(self):
        for i in range(len(self.blocks)):
            self.screen.blit(self.blocks[i].Display(), (43+ i*60,250))



