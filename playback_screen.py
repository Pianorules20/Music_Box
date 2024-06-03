#player.py
import screen_saver as s_s, fonts as f, layout_playback_style as l_p, display as d, pygame
import display as d, gni # generate_notes_interface


#def handle_strings(myText, xAxis, yAxis, leftEdge, rightEdge, bottomEdge, font, multiple):
class Data():
    
    recording = 'my_recording'

class Note(pygame.sprite.Sprite):

    counter = 0
    #note = pygame.sprite.Sprite()
    note = pygame.Surface((0,0))    #1st item to blit to screen
    rect = () #refers to __init__ item 10 
    position = () #2nd item to blit to screen
    
    def __init__(self, frame, x_plot, y_plot) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.frame = frame
        self.image = pygame.Surface((0,0))
        self.image = pygame.image.load(frame).convert()
        self.rect = self.image.get_rect()
        Note.note = self.image
        self.x_plot = x_plot         

    
def playback_screen():

    d.Data.window.fill(s_s.Data.rbg,(0,0, l_p.Data.width, l_p.Data.height))

    Data.splash_A = 'My Recording'
    Data.splash_B = f.Data.large_script
    Data.splash_C = Data.splash_B.render(Data.splash_A, True, s_s.Data.text, s_s.Data.rbg)
    Data.splash_D = Data.splash_C.get_rect()
    Data.splash_D.center = l_p.Data.x1000, l_p.Data.y100
    d.Data.window.blit(Data.splash_C, Data.splash_D)
    
    for eachNote in l_p.Data.objects:

        yPos = gni.Note.returnOctave(eachNote)
        xPos = gni.Note.returnXPos(eachNote)
        #final = gni.Note.returnRect(eachNote)
        image = gni.Note.returnImage(eachNote)
        d.Data.window.blit(image, ( xPos * d.Data.view_multiplier, yPos))
    #snapshot = d.Data.blit(rectangle, (eachNote.x_pos,eachNote.y_pos))   # blits basic screen
    #snapshot = snapshot
    '''
    Data.recording_A = pb.Data.recording
    th.reset_text()
    th.handle_strings(Data.recording_A, l_p.Data.x10, l_p.Data.y100, l_p.Data.x10, l_p.Data.x1800, \
                l_p.Data.y1900, f.Data.large_script, multiple = 'no')
    for eachNote in l_p.Data.objects:
        d.Data.frame.blit(eachNote.image, Data.splash_D)  #update my second parameter'''

