#branches.py
import settings as s, structure as struc, plot_notes as pn, playback as pb, post_production as pp, debug as db
import my_song as m_s

class Branch():
    pass

def generator_branches():
    if s.Data.structure == 'Random Short Form':
        print('in branches entering structure.randomShortForm()')
        struc.randomShortForm()
    elif s.Data.structure == 'Long Form New':
        struc.longFormNew()
    elif s.Data.structure == 'User Constructed': #catches settings 'User Constructed'
        struc.userConstructed()
    else:
        info = 'Error in branches.Branch...re: settings.Data.structure'
        print(info)
        #db.debug_log.append(info)

def plot_notes():
    pn.plot_notes()

def playback():
    pb.play()

def post_production():

    pp.print_sheet()
    pp.record_audio()
    pp.next()

def pause():
    pass