# dev_focus.py
# export as d_f

class Data():

    string = 'None'
    list = []


def magnify(first = Data.string, second = Data.list):
    
    if first == 'None':
        pass
    else:
        print(f'dev_focus: {first}')
    
    if len(second) == 0:
        pass
    else:
        print(f'magnify: {second}')