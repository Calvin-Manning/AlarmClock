import pygame
import Colours

class Button_Square(pygame.sprite.Sprite):
    def __init__(self, Type, x, y, len, hight):
        super().__init__()

        But_Names = ("Alarm", "Music", "Weather", "Return", "1","2","3","4","5","6","7","8","9","0","Ent","Del")
        self.Name = But_Names[Type]

        self.ret = 0
        self.lock = True

        self.loc = (x,y)
        self.size = (len,hight)

        self.colour = Colours.Second

        self.font = pygame.font.Font("freesansbold.ttf", 40)
        self.text = self.font.render(self.Name, True, Colours.Accent)
        self.txtRect = self.text.get_rect().center

        self.image = pygame.Surface((self.size[0], self.size[1]))
        self.image.fill(self.colour)


        pygame.draw.rect(self.image,self.colour,pygame.Rect(0, 0, self.size[0], self.size[1]))

        self.rect = self.image.get_rect()

        self.image.blit(self.text,(0,0))


    def display(self):
        return self.image, self.loc

    def check(self, event):
        self.lock = True
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if self.loc[0] <= x <= self.loc[0]+self.rect[2] and self.loc[1] <= y <= self.loc[1]+self.rect[3]:
                if self.Name == "Alarm":
                    self.ret = 1
                    self.lock = False
                if self.Name == "Music":
                    self.ret = 2
                    self.lock = False
                if self.Name == "Weather":
                    self.ret = 3
                    self.lock = False
                if self.Name == "Return":
                    self.ret = 200
                    self.lock = False
                if self.Name == "0" or self.Name == "1" or self.Name == "2" or self.Name == "3" or self.Name == "4" or self.Name == "5" or self.Name == "6" or self.Name == "7" or self.Name == "8" or self.Name == "9" or self.Name == "Del" or self.Name == "Ent":
                    self.ret = self.Name
                    self.lock = False

        return self.ret, self.lock


class Button_Round(pygame.sprite.Sprite):
    def __init__(self, Type, x, y, Rad):
        super().__init__()

        But_Names = ("Sleep", "Start")
        self.Name = But_Names[Type]

        self.ret = 0
        self.lock = True

        self.loc = (x,y)
        self.size  = Rad

        self.colour = Colours.Co

        self.font = pygame.font.Font("freesansbold.ttf", 30)
        self.text = self.font.render(self.Name, True, Colours.Accent)
        self.txtRect = self.text.get_rect().center

        self.image = pygame.Surface((self.size*2, self.size*2))
        self.image.fill(Colours.Main)

        pygame.draw.circle(self.image, self.colour, (self.size, self.size), self.size)

        self.rect = self.image.get_rect()

        self.image.blit(self.text,(0,0))

    def display(self):
        return self.image, self.loc

    def check(self, event):
        self.lock = True
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if self.loc[0] <= x <= self.loc[0]+self.rect[2] and self.loc[1] <= y <= self.loc[1]+self.rect[3]:

                if self.Name == "Sleep":
                    self.ret = 4
                    self.lock = False
                if self.Name == "Start":
                    self.ret = 7
                    self.lock = True

        return self.ret, self.lock


class Indicater:
    def __init__(self, x, y):

        self.loc = (x,y)

        self.lock = True

        self.On = (70,250,70)
        self.Off = (250,70,70)
        self.TF = False

        self.image = pygame.Surface((350, 75))
        self.image.fill(self.Off)

        self.rect = self.image.get_rect()

    def display(self):
        return self.image, self.loc

    def check(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if self.loc[0] <= x <= self.loc[0]+self.rect[2] and self.loc[1] <= y <= self.loc[1]+self.rect[3]:
                if self.TF == True:
                    self.TF = False
                    self.image.fill(self.Off)

                elif self.TF == False:
                    self.TF = True
                    self.image.fill(self.On)

        return self.TF
