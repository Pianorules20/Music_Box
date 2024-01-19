#plot_notes.py
import mySong as my, objects as ob, plot_meter as pm, gni
import pni, debug as db, playback as pb

'''This file works primarily with 'pni' class 'Count' variables are sectionCounter, noteCounter and populate *bool*'''
'''class P():
     pass #'Pl' stands for 'Plot'''
'''
def plot_notes(): 

    if pni.Data.populate_me == True:
            
            db.Data.debug_log.append(f'pni.populate_me = {pni.Data.populate_me}')
            pni.populateNotes()

    else:
        pass
    
        # referencing pm.M.meter

    for eachNote in pni.Data.this_section: 

        xPos = gni.Note.returnXPos(eachNote)

        if pm.M.meter == xPos:

            pni.Data.current_plot.append(eachNote)  # pay attention!!!  This is what the playback will use
            try:
                    
                pni.Data.section_counter -= 1

            except:
                
                pni.advance()

        else:
            
            pass
    
    pni.createPlot(notesExternal = pni.Data.current_plot)
    
    pni.resetPlot()

        #gatekeeper.Gate.current = 'plot_notes'
    else:
        print('error in plot_notes? what happened to Count.note Counter?')
        try: 
                pni.I.sectionCounter +=1
        except:
            pni.I.populateMe != pni.I.populateMe
            gatekeeper.Gate.current = 'playback'''


        
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