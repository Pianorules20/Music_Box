#splashScreen.py
import pygame
import pygame.locals
import display_interface as di

'''class Event():
    
    xIncrement = int(20)

    def pulse():
        print(f'xAxis equals {Event.xIncrement}')
        mySongs.Recordings.meter += Event.xIncrement'''

class Window():
    def __init__(self) -> None:
        pass    
    print('Window initialized')
    width = di.Data.width
    height = di.Data.height
    surf = pygame.Surface((di.Data.width/2  , di.Data.height/2))
    frame = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    background = frame.fill((180,180,40),(0,0, di.Data.width, di.Data.height))
    screen = pygame.Surface((0,0), pygame.RESIZABLE)
    width = di.Data.width
    height = di.Data.height
    quitting = False

    def updateScreen():
        update = di.screenGate(di.Data.current)
        update = update
        #print('updateScreen initialized')
        #layer3.center = (objects.Buttons.xAxis, objects.Buttons.yAxis)
        #pygame.draw.rect(Window.frame, (200,200,200), pygame.Rect(30,30,60,60))
        #pygame.Surface((Window.width/20, Window.height/20))
        #Window.width, Window.height
        '''for eachObject in objects.myNotes:
            eachObject._blit_()'''
        pygame.display.flip()        