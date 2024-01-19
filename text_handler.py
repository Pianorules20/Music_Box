#textHandler.py
import fonts as f, screen_saver as ss, display as d

class Data():
    #use the individual screens to update the Data.text
    start = 20
    xAxis = 20
    yAxis = 650
    offset = 0
    #right_edge = 0
    color_counter = int(0)
    current_color = ss.Data.text
    multi_colors = ss.Data.color_list
    scroll_pages = False

'''def advance():
    
    Data.multi_colors.append(Data.multi_colors[0])
    Data.multi_colors.pop(0)'''

def reset_text():
    Data.start = 20
    Data.xAxis = 20
    Data.yAxis = 650
    Data.offset = 0
    Data.color_counter = int(0)
    Data.current_color = ss.Data.text
    #di.Data.scroll_pages = False

def scroll_page():
    Data.scroll_pages = True
    '''for each in lm.y_values:
        each += 900'''

def handle_strings(myText, xAxis, yAxis, leftEdge, rightEdge, bottomEdge, font, multiple):
    Data.text = myText
    Data.word = Data.text.split(' ')
    Data.start = xAxis
    Data.xAxis = Data.start
    Data.yAxis = yAxis
    Data.offset = 0
    for eachWord in Data.word:
        Data.xAxis += Data.offset
        textA = eachWord
        textB = font
        textC = textB.render(textA, True, Data.current_color, ss.Data.rbg)
        Data.offset = textC.get_width()
        if Data.xAxis > rightEdge:
            Data.xAxis = Data.start
            Data.yAxis += 50
        else:
            pass
        if Data.yAxis > bottomEdge:
            if multiple == 'yes':
                Data.scroll_pages = True
            Data.xAxis = Data.start
            Data.current_color = Data.multi_colors[2]
        else:
            pass
        textD = textC.get_rect()    
        textD.bottomleft = (Data.xAxis, Data.yAxis)
        d.Window.frame.blit(textC, textD)

'''
     d.Window.spacebar1 = 'Press Spacebar to Create and Record'
    d.Window.spacebar2 = f.Data.scripted
    d.Window.spacebar3 = d.Window.spacebar2.render(d.Window.spacebar1, True, ss.Data.text, ss.Data.rbg)
    d.Window.spacebar4 = d.Window.spacebar3.get_rect()
    d.Window.spacebar4.bottomleft = di.Data.left_col_2
    d.Window.frame.blit(d.Window.spacebar3, d.Window.spacebar4)'''
                 
