#plot_notes.py
import mySong as my, objects as ob, plot_meter as pm, generate_notes_interface as gni
import plot_notes_interface as pni

class Pl(): #'Pl' stands for 'Plot'

    def plot_notes(): 

        for eachSection in my.Transcription.transcript: #a list inside of a list

            thisSection = eachSection #this is a list for depopulation 
            
            while len(thisSection) > 0:
                
                for eachNote in thisSection: 
                    xPos = gni.Note.returnXPos(eachNote)
                    if pm.M.meter == xPos:
                        pni.Inc.currentPlot.append(eachNote)
                        thisSection.pop(eachNote)
                    else:
                        pass
                pni.Inc.createIncrement()
            
            

        
'''class Note(pygame.sprite.Sprite):

    counter = 0
    note = pygame.sprite.Sprite()
    note = pygame.Surface((0,0))    #1st item to blit to screen
    rect = () #refers to __init__ item 10 
    position = () #2nd item to blit to screen
    
    def __init__(self, frame, x_plot, y_plot) -> None:
        print('Player Object Initiated')
        pygame.sprite.Sprite.__init__(self)
        self.frame = frame
        self.image = pygame.Surface((0,0))
        self.image = pygame.image.load(frame).convert()
        self.rect = self.image.get_rect()
        Note.note = self.image
        self.x_plot = x_plot
        self.y_plot = y_plot
        #Player.face_right = Player.hero
        Note.position = (self.x_plot, self.y_plot)
        display.Window.position= Note.position
        #create.py should handle inputting a new surface into the Window.note position
        Note.rect = self.rect 
    def returnData():
       return Note.note, Note.position
    
    def _blit_():
       display.Window.frame.blit(Note.note, Note.position)'''