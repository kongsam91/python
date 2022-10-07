import pandas as pd
import eel
from main import main

def close_callback(route, websockets):
    if not websockets:
        print('Bye!')
        quit()

# @eel.expose
main()
eel.init('fitting_GUI') #網頁資料夾
eel.start('.\fitting.html',
                        size=(1024,720),
                        port= 8787,
                        position=(0,0),
                        close_callback=close_callback
                        )