import pygame
import os
import Clock
import Timer
import Buttons
import Colours

pygame.init()

Screen_Size = (800,500)
FPS = 30

Alarm_on = False

Alarm_time = ["0"]*5
Temp_Alarm_time = ["0"]*5
Alarm_time[2] = ":"
font = pygame.font.Font("freesansbold.ttf", 70)
font2 = pygame.font.Font("freesansbold.ttf", 20)

Screen = pygame.display.set_mode(Screen_Size, pygame.FULLSCREEN, 16)
pygame.display.set_caption("My First Game")

clock = pygame.time.Clock()
Time = Clock.Tic(Screen, Screen_Size)

rect_buts = []
for i in range(3):
    rect_buts.append(Buttons.Button_Square(i, 40 + (i*260), 310, 200, 150))

Ret_but = Buttons.Button_Square(3, 10, 10, 125, 75)


for i in range(2):
    rect_buts.append(Buttons.Button_Round(i, 50+(i*550), 50, 70))

sleep_but2 = Buttons.Button_Round(1, 600, 50, 70)

inic = Buttons.Indicater(40,400)

k = 4
inp_buttons = []
for i in range(4):
    for j in range(3):
        inp_buttons.append(Buttons.Button_Square(k, 450+ j*120, 25+ (i*120), 90, 90))
        k += 1

timer = Timer.timer(Screen)

run = True
Mode = 0
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False

        if Mode == 1:
            for i in range(len(inp_buttons)):
                ret, lock = inp_buttons[i].check(event)
                if lock == False:
                    if ret != "Del" and ret != "Ent":
                        Temp_Alarm_time = Alarm_time
                        Alarm_time[0] = Temp_Alarm_time[1]
                        Alarm_time[1] = Temp_Alarm_time[3]
                        Alarm_time[3] = Temp_Alarm_time[4]
                        Alarm_time[4] = ret
                    elif ret == "Del":
                        Alarm_time = ["0","0",":","0","0"]
                    elif ret == "Ent":
                        if 0 <= int(Alarm_time[0]) <= 2 and 0 <= int(Alarm_time[3]) <=6:
                            print("accepted")


            Alarm_on = inic.check(event)


        if Mode == 4:
            if event.type == pygame.MOUSEBUTTONUP:
                Mode = 0

        if Mode == 0:
            for i in range(len(rect_buts)):
                ret, lock = rect_buts[i].check(event)
                if lock == False:
                    Mode = ret
                if ret == 7:
                    timer.Start()


        if Mode != 0 and Mode != 4:
            ret, lock = Ret_but.check(event)
            if lock == False:
                Mode = 0


    if Mode == 0: # Main Screen
        Screen.fill(Colours.Main)

        for i in range(len(rect_buts)):
            rect, loc = rect_buts[i].display()
            Screen.blit(rect, loc)

        if Alarm_on == True:
            text = font2.render(f"{Alarm_time[0]}{Alarm_time[1]}{Alarm_time[2]}{Alarm_time[3]}{Alarm_time[4]}", True, Colours.Accent)
            Screen.blit(text, (370, 20))

        timer.Update()
        timer.Display()

        Time.Update()
        Time.Display()

    elif Mode == 1: # Alarm
        Screen.fill(Colours.Main)
        rect, loc = Ret_but.display()
        Screen.blit(rect, loc)

        for i in range(len(inp_buttons)):
            rect, loc = inp_buttons[i].display()
            Screen.blit(rect, loc)

        text = font.render(f"{Alarm_time[0]}{Alarm_time[1]}:{Alarm_time[3]}{Alarm_time[4]}", True, Colours.Accent)
        Screen.blit(text, (120,225))

        rect, loc = inic.display()
        Screen.blit(rect, loc)



    elif Mode == 2: # Music
        Screen.fill((0,255,0))
        rect, loc = Ret_but.display()
        Screen.blit(rect, loc)

    elif Mode == 3: # Weather
        Screen.fill((0,0,255))
        rect, loc = Ret_but.display()
        Screen.blit(rect, loc)

    elif Mode == 4: # Sleep
        Screen.fill((0,0,0))

    else:
        print(Mode)


    if Alarm_on == True:
        T_h, T_m = Time.Time_Check()
        A_h = Alarm_time[0] + Alarm_time[1]
        A_m = Alarm_time[3] + Alarm_time[4]

        if T_h == A_h and T_m == A_m:
            print("Alarm")


    pygame.display.flip()
    clock.tick(FPS)
    os.system("cls")

pygame.quit()
