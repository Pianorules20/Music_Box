# plot_notes_interface.py
import playback as play, generate_notes_interface as geni


class Inc(): # stands for 'Increment'

    sounds = []
    currentPlot = []
    for eachNote in currentPlot():
        sounds.append(geni.returnSound(eachNote))

    
    def createIncrement():
        inc = Inc()

        play.Player.recording.append(inc)