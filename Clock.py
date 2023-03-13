import pygame
import Colours
import time

Time = time.ctime()

Day_S = Time[0:3]
Day_I = Time[8:10]
Month = Time[4:7]
Year = Time[20:24]
Hour = Time[11:13]
Min = Time[14:16]
Sec = Time[17:19]


class Tic:
    def __init__(self, Plate, Screen_Size):
        self.Day_S = ""
        self.Day_I = ""
        self.Month = ""
        self.Year = ""
        self.Hour = ""
        self.Min = ""
        self.Sec = ""

        self.Plate = Plate
        self.Screen_Size = Screen_Size

        self.font0 = pygame.font.Font('freesansbold.ttf', 85)
        self.font1 = pygame.font.Font('freesansbold.ttf', 16)

    def Update(self):
        Time = time.ctime()

        self.Day_S = Time[0:3]
        self.Day_I = Time[8:10]
        self.Month = Time[4:7]
        self.Year = Time[20:24]
        self.Hour = Time[11:13]
        self.Min = Time[14:16]
        self.Sec = Time[17:19]

    def Display(self):
        self.text = self.font0.render(f"{self.Hour}:{self.Min}", True, Colours.Accent, None)
        self.text_R = self.text.get_rect()
        self.Plate.blit(self.text, (self.Screen_Size[0]/2 - self.text_R[2]/2 - 10,100))

    def Time_Check(self):
        return self.Hour, self.Min

