#mainBranch.py
import settings, branches2, plot_notes, playback, post_production

class Branch():

    def generator_branches():
        if settings.Preferences.structure == 'Random Short Form':
            branches2.randomShortForm()
        elif settings.Preferences.structure == 'Long Form New':
            branches2.longFormNew()
        elif settings.Preferences.structure == 'User Constructed': #catches settings 'User Constructed'
            branches2.userConstructed()
        else:
            print('Error in branches.Branch...re: settings.Preferences.structure')

    def plot_notes():
        plot_notes.Plot.plot_notes()

    def playback():
        playback.Player.play()

    def post_production():
        post_production.Printer.current_function()
        post_production.Recorder.current_function()

    def pause():
        pass


