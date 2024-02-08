#screen_saver.py

class Data():
    
    red = 180
    blue = 180
    green = 40
    rbg = (red, blue, green)
    
    text_red = 10
    text_blue = 10
    text_green = 20
    text = (text_red, text_blue, text_green)   
    debug1 = (30, 30, 30)
    debug2 = (70, 70, 70)
    debug3 = (110, 110, 110)
    color_list = [debug1, debug2, debug3]

    counter = int(0)
    red_regress = False
    blue_regress = False
    banner_regress = int(0)

def advance():
    Data.rbg = (Data.red, Data.blue, Data.green)
    Data.text = (Data.text_red, Data.text_blue, Data.text_green)
    Data.colors = f'colors: rbg {Data.red}, {Data.blue}, {Data.green}, regress red {Data.red_regress} blue {Data.blue_regress}'
    #artifact debug line  db.debug_log.append(f'counter {int(Data.counter/10)}')
    
    if Data.blue_regress == False:
        if Data.blue < 200:
            if Data.counter % 30  == 0:
                Data.blue += 1
            else:
                pass
        else:
            Data.blue_regress = True
    else:
        if Data.blue > 130:
            if Data.counter % 30 == 0:
                Data.blue -= 1
            else:
                pass
        else:
            Data.blue_regress = False


    if Data.red_regress == False:
        if Data.red < 225:
            Data.counter += 1
            if Data.counter == 40:
                Data.red += 1
                Data.text_red += 1 
                Data.counter = int(0)
            else:
                pass
        else:
            Data.red_regress = True
    else:
        if Data.red > 180:
            Data.counter += 1
            if Data.counter == 40:
                Data.red -= 1
                Data.text_red -= 1
                Data.counter = int(0)
            else:
                pass
        else:
            Data.red_regress = False
    
    Data.banner_regress += 0.03
    if Data.banner_regress >= 1200:
        Data.banner_regress -= 2400
    else:
        pass