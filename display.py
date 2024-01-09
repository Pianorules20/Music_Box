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

    surf = pygame.Surface((di.I.width/2, di.I.height/2))
    position = di.I.width, di.I.height
    frame = pygame.display.set_mode((di.I.width, di.I.height), pygame.RESIZABLE)
    background = frame.fill((180,180,40),(0,0, di.I.width, di.I.height))
    screen = pygame.Surface((0,0), pygame.RESIZABLE)
    
    def updateScreen():
        update = di.I.screenGate(di.I.current)
        update = update
        #print('updateScreen initialized')
        #layer3.center = (objects.Buttons.xAxis, objects.Buttons.yAxis)
        #pygame.draw.rect(Window.frame, (200,200,200), pygame.Rect(30,30,60,60))
        #pygame.Surface((Window.width/20, Window.height/20))
        #Window.width, Window.height
        '''for eachObject in objects.myNotes:
            eachObject._blit_()'''
        pygame.display.flip()
        
            