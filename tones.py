#py
import pygame

pygame.mixer.init()

class Tone():
    def __init__(self, letterName, octave, sound, clefHeight):
        self.letterName = letterName
        self.octave = octave
        self.sound = sound
        self.clefHeight = clefHeight

    def play(x):
        pygame.mixer.find_channel(True)
        pygame.mixer.Sound.play(x)
		
    def returnLetterName(self):
        return self.letterName
        
    def returnOctave(self):
        return self.octave
        
    def returnSound(self):
        return self.sound
    
    def returnClefHeight(self):
        return self.clefHeight

class Piano():

    A1 = Tone(letterName = 'A', octave = 1, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/A1.wav'), clefHeight = 1)
    Bb1 = Tone(letterName = 'Bb', octave = 1, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Bb1.wav'), clefHeight = 2)
    B1 = Tone(letterName = 'B', octave = 1, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/B1.wav'), clefHeight = 3)
    C1 = Tone(letterName = 'C', octave = 1, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/C1.wav'), clefHeight = 4)
    Db1 = Tone(letterName = 'Db', octave = 1, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Db1.wav'), clefHeight = 5)
    D1 = Tone(letterName = 'D', octave = 1,  sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/D1.wav'), clefHeight = 6)
    Eb1 = Tone(letterName = 'Eb', octave = 1, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Eb1.wav'), clefHeight = 7)
    E1 = Tone(letterName = 'E', octave = 1, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/E1.wav'), clefHeight = 8)
    F1 = Tone(letterName = 'F', octave = 1,  sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/F1.wav'), clefHeight = 9)
    Gb1 = Tone(letterName = 'Gb', octave = 1, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Gb1.wav'), clefHeight = 10)
    G1 = Tone(letterName = 'G', octave = 1, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/G1.wav'), clefHeight = 11)
    Ab1 = Tone(letterName = 'Ab', octave = 1,  sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Ab1.wav'), clefHeight = 12)
    A2 = Tone(letterName = 'A', octave = 2, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/A2.wav'), clefHeight = 13)
    Bb2 = Tone(letterName = 'Bb', octave = 2, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Bb2.wav'), clefHeight = 14)
    B2 = Tone(letterName = 'B', octave = 2,  sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/B2.wav'), clefHeight = 15)
    C2 = Tone(letterName = 'C', octave = 2,  sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/C2.wav'), clefHeight = 16)
    Db2 = Tone(letterName = 'Db', octave = 2, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Db2.wav'), clefHeight = 17)
    D2 = Tone(letterName = 'D', octave = 2,  sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/D2.wav'), clefHeight = 18)
    Eb2 = Tone(letterName = 'Eb', octave = 2, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Eb2.wav'), clefHeight = 19)
    E2 = Tone(letterName = 'E', octave = 2, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/E2.wav'), clefHeight = 20)
    F2 = Tone(letterName = 'F', octave = 2, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/F2.wav'), clefHeight = 21)
    Gb2 = Tone(letterName = 'Gb', octave = 2,  sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Gb2.wav'), clefHeight = 22)
    G2 = Tone(letterName = 'G', octave = 2, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/G2.wav'), clefHeight = 23)
    Ab2 = Tone(letterName = 'Ab', octave = 2, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Ab2.wav'), clefHeight = 24)
    A3 = Tone(letterName = 'A', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/A3.wav'), clefHeight = 25)
    Bb3 = Tone(letterName = 'Bb', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Bb3.wav'), clefHeight = 26)
    B3 = Tone(letterName = 'B', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/B3.wav'), clefHeight = 27)
    C3 = Tone(letterName = 'C', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/C3.wav'), clefHeight = 28)
    Db3 = Tone(letterName = 'Db', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Db3.wav'), clefHeight = 29)
    D3 = Tone(letterName = 'D', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/D3.wav'), clefHeight = 30)
    Eb3 = Tone(letterName = 'Eb', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Eb3.wav'), clefHeight = 31)
    E3 = Tone(letterName = 'E', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/E3.wav'), clefHeight = 32)
    F3 = Tone(letterName = 'F', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/F3.wav'), clefHeight = 33)
    Gb3 = Tone(letterName = 'Gb', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Gb3.wav'), clefHeight = 34)
    G3 = Tone(letterName = 'G', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/G3.wav'), clefHeight = 35)
    Ab3 = Tone(letterName = 'Ab', octave = 3, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Ab3.wav'), clefHeight = 36)
    A4 = Tone(letterName = 'A', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/A4.wav'), clefHeight = 37)
    Bb4 = Tone(letterName = 'Bb', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Bb4.wav'), clefHeight = 38)
    B4 = Tone(letterName = 'B', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/B4.wav'), clefHeight = 39)
    C4 = Tone(letterName = 'C', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/C4.wav'), clefHeight = 40)
    Db4 = Tone(letterName = 'Db', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Db4.wav'), clefHeight = 41)
    D4 = Tone(letterName = 'D', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/D4.wav'), clefHeight = 42)
    Eb4 = Tone(letterName = 'Eb', octave =4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Eb4.wav'), clefHeight = 43)
    E4 = Tone(letterName = 'E', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/E4.wav'), clefHeight = 44)
    F4 = Tone(letterName = 'F', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/F4.wav'), clefHeight = 45)
    Gb4 = Tone(letterName = 'Gb', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Gb4.wav'), clefHeight = 46)
    G4 = Tone(letterName = 'G', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/G4.wav'), clefHeight = 47)
    Ab4 = Tone(letterName = 'Ab', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Ab4.wav'), clefHeight = 48)
    A5 = Tone(letterName = 'A', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/A5.wav'), clefHeight = 49)
    Bb5 = Tone(letterName = 'Bb', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Bb5.wav'), clefHeight = 50)
    B5 =Tone(letterName = 'B', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/B5.wav'), clefHeight = 51)
    C5 = Tone(letterName = 'C', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/C5.wav'), clefHeight = 52)
    Db5 = Tone(letterName = 'Db', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Db5.wav'), clefHeight = 53)
    D5 = Tone(letterName = 'D', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/D5.wav'), clefHeight = 54)
    Eb5 = Tone(letterName = 'Eb', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Eb5.wav'), clefHeight = 55)
    E5 = Tone(letterName = 'E', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/E5.wav'), clefHeight = 56)
    F5 = Tone(letterName = 'F', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/F5.wav'), clefHeight = 57)
    Gb5 = Tone(letterName = 'Gb', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Gb5.wav'), clefHeight = 58)
    G5 = Tone(letterName = 'G', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/G5.wav'), clefHeight = 59)
    Ab5 = Tone(letterName = 'Ab', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Ab5.wav'), clefHeight = 60)
    A6 = Tone(letterName = 'A', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/A6.wav'), clefHeight = 61)
    Bb6 = Tone(letterName = 'Bb', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Bb6.wav'), clefHeight = 62)
    B6 = Tone(letterName = 'B', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/B6.wav'), clefHeight = 63)
    C6 = Tone(letterName = 'C', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/C6.wav'), clefHeight = 64)
    Db6 = Tone(letterName = 'Db',octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Db6.wav'), clefHeight = 65)
    D6 = Tone(letterName = 'D', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/D6.wav'), clefHeight = 66)
    Eb6 = Tone(letterName = 'Eb', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Eb6.wav'), clefHeight = 67)
    E6 = Tone(letterName = 'E', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/E6.wav'), clefHeight = 68)
    F6 = Tone(letterName = 'F', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/F6.wav'), clefHeight = 69)
    Gb6 = Tone(letterName = 'Gb', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Gb6.wav'), clefHeight = 70)
    G6 = Tone(letterName = 'G', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/G6.wav'), clefHeight = 71)
    Ab6 = Tone(letterName = 'Ab', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Ab6.wav'), clefHeight = 72)
    A7 = Tone(letterName = 'A', octave = 7, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/A7.wav'), clefHeight = 73)
    Bb7 = Tone(letterName = 'Bb', octave = 7, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Bb7.wav'), clefHeight = 74)
    B7 = Tone(letterName = 'B', octave = 7, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/B7.wav'), clefHeight = 75)
    C7 = Tone(letterName = 'C', octave = 7, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/C7.wav'), clefHeight = 76)
    Db7 = Tone(letterName = 'Db',octave = 7, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Db7.wav'), clefHeight = 77)
    D7 = Tone(letterName = 'D', octave = 7, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/D7.wav'), clefHeight = 78)
    Eb7 = Tone(letterName = 'Eb', octave = 7,  sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Eb7.wav'), clefHeight = 79)
    E7 = Tone(letterName = 'E', octave = 7, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/E7.wav'), clefHeight = 80)
    F7 = Tone(letterName = 'F7', octave = 7, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/F7.wav'), clefHeight = 81)
    Gb7 = Tone(letterName = 'Gb', octave = 7, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Gb7.wav'), clefHeight = 82)
    G7 = Tone(letterName = 'G', octave = 7, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/G7.wav'), clefHeight = 83)
    Ab7 = Tone(letterName = 'Ab', octave = 7, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Ab7.wav'), clefHeight = 84)
    A8 = Tone(letterName = 'A', octave = 8, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/A8.wav'), clefHeight = 85)
    Bb8 = Tone(letterName = 'Bb', octave = 8, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/Bb8.wav'), clefHeight = 86)
    B8 = Tone(letterName = 'B', octave = 8, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/B8.wav'), clefHeight = 87)
    C8 = Tone(letterName = 'C', octave = 8, sound = pygame.mixer.Sound('sounds/polyphone/Yamaha_CFX_Grand/C8.wav'), clefHeight = 88)

    tones = [A1, Bb1, B1, C1, Db1, D1, Eb1, E1, F1, \
            Gb1, G1, Ab1, A2, Bb2, B2, C2, Db2, D2, \
            Eb2, E2, F2, Gb2, G2, Ab2, A3, Bb3, B3, \
            C3, Db3, D3, Eb3, E3, F3, Gb3, G3, Ab3, \
            A4, Bb4, B4, C4, Db4, D4, Eb4, E4, F4, \
            Gb4, G4, Ab5, A5, Bb5, B5, C5, Db5, D5, \
            Eb5, E5, F5, Gb5, G5, Ab5, A6, Bb6, B6, \
            C6, Db6, D6, Eb6, E6, F6, Gb6, G6, Ab6, \
            A7, Bb7, B7, C7, Db7, D7, Eb7, E7, F7, \
            Gb7, G7, Ab7, A8, Bb8, B8, C8]

    for eachTone in tones:
        pygame.mixer.Sound.set_volume(eachTone.sound, 1)

class Harp():
    A4 = Tone(letterName = 'C', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/A4.wav'), clefHeight = 37)
    B4 = Tone(letterName = 'B', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/B4.wav'), clefHeight = 39)
    Db4 = Tone(letterName = 'Db', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/Db4.wav'), clefHeight = 41)
    D4 = Tone(letterName = 'D', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/D4.wav'), clefHeight = 42)
    E4 = Tone(letterName = 'E', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/E4.wav'), clefHeight = 44)
    Gb4 = Tone(letterName = 'Gb', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/Gb4.wav'), clefHeight = 46)
    G4 = Tone(letterName = 'G', octave = 4, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/G4.wav'), clefHeight = 47)
    A5 = Tone(letterName = 'A', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/A5.wav'), clefHeight = 49)
    B5 =Tone(letterName = 'B', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/B5.wav'), clefHeight = 51)
    C5 = Tone(letterName = 'C', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/C5.wav'), clefHeight = 52)
    D5 = Tone(letterName = 'D', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/D5.wav'), clefHeight = 54)
    E5 = Tone(letterName = 'E', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/E5.wav'), clefHeight = 56)
    Gb5 = Tone(letterName = 'Gb', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/Gb5.wav'), clefHeight = 58)
    Ab5 = Tone(letterName = 'Ab', octave = 5, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/Ab5.wav'), clefHeight = 60)
    A6 = Tone(letterName = 'A', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/A6.wav'), clefHeight = 61)
    B6 = Tone(letterName = 'B', octave = 6, sound = pygame.mixer.Sound('sounds/polyphone/Celtic_Harp/B6.wav'), clefHeight = 63)
    
    introMusic = [A4, B4, Db4, D4, E4, 
         Gb4, G4, A5, B5, C5, 
         D5, E5, Gb5, Ab5, A6, 
         B6]    
    
    for eachTone in introMusic:
        pygame.mixer.Sound.set_volume(eachTone.sound, 0.3)