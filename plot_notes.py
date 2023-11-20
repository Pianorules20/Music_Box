#plot_notes.py
import mySong as my, objects as ob, plot_meter as pm, generate_notes_interface as gni, gatekeeper
import plot_notes_interface as pni

'''This file works primarily with 'pni' class 'Count' variables are sectionCounter, noteCounter and populate *bool*'''
class P(): #'Pl' stands for 'Plot'

    def plot_notes(): 

        if pni.Count.populate == True:
                
                print('pni.Count.populate = True')
                pni.populate()

        else:

            if pni.Count.noteCounter > 0:

                print(f'pni.Count.noteCounter = {len(pni.Count.noteCounter)} ')
                for eachNote in pni.Count.thisSection: 

                    xPos = gni.Note.returnXPos(eachNote)

                    if pm.M.meter == xPos:

                        pni.Inc.currentPlot.append(eachNote)
                    
                        pni.Count.thisSection.pop(eachNote)
                    else:
                        pass
                
                pni.Inc.createIncrement()
                pni.Count.noteCounter -=1
                gatekeeper.Gate.passGate('plot_notes')
                

            else:
                print('error in plot_notes? what happened to Count.note Counter?')
                try: 
                        pni.Count.sectionCounter +=1
                except:
                    pni.Count.populate != pni.Count.populate
                    gatekeeper.Gate.passGate('playback')



            
            

        
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