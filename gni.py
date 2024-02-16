#gni means 'generate notes interface'
import settings as s, my_song as m_s, current_section as c_s, tones as t, pygame.mixer, display as d, debug as db, structure

class Note():

    note = pygame.Surface((100,100))    #1st item to blit to screen
    rect = () #refers to __init__ item 10 
    position = () #2nd item to blit to screen

    def __init__(self, xPos, yPos, sound, duration, imageOut, letterName, octave, polyOrder) -> None:
        print('in_gni_class_Note')
        pygame.sprite.Sprite.__init__(self)
        self.imageOut = imageOut
        self.final_image = pygame.Surface((100,100))
        self.final_image = pygame.image.load(imageOut).convert()
        self.rect = self.final_image.get_rect()
        Note.image = self.final_image
        self.xPos = xPos
        self.yPos = yPos
        self.sound = sound
        self.duration = duration
        self.letterName = letterName
        self.octave = octave
        self.polyOrder = polyOrder
        #Player.face_right = Player.hero
        Note.position = (self.xPos, self.yPos)
        d.Data.position= Note.position
        #create.py should handle inputting a new surface into the Data.note position
        Note.rect = self.rect 
   
    def returnLetterName(self):
        return self.letterName
    
    def returnOctave(self):
        return self.octave

    def returnSound(self):
        return self.sound
    
    def returnDuration(self):
        return self.duration
    
    def returnImage(self):
        return self.image

    def returnData():
       return Note.note, Note.position
    
    def returnXPos(self):
        return self.xPos 
    
    def returnRect(self):
        return self.rect
    
    def _blit_():
       d.Data.frame.blit(Note.note, Note.position)
    
    def play(x):
        pygame.mixer.find_channel(True)
        pygame.mixer.Sound.play(x)  
    
    '''except Exception as e:
            print('error_in_step3 early randomizer with settings...')
            print(e)'''
    #db.Data.debug_log.append(f'_in_gni:_instance.notesRemaining = {cs.Data.notesRemaining}')
    # breadcrumb print(f' in gni: Note spacial data xPos {xPos} {name}{octave} yPos{height}') 
    # breadcrumb print(f' instance.notesRemaining = {instance.notesRemaining}')