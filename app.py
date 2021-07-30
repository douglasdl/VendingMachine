import eel
import random
from datetime import datetime

def close_callback(route, websockets):
    if not websockets:
        print('Bye!')
        exit()

eel.init('web')

@eel.expose
def get_random_name():
    eel.prompt_alerts('Random name')

@eel.expose
def get_random_number():
    eel.prompt_alerts(random.randint(1, 100))

@eel.expose
def get_date():
    eel.prompt_alerts(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

@eel.expose
def get_ip():
    eel.prompt_alerts('127.0.0.1')

eel.start('index.html', mode='chrome', 
                        host='localhost', 
                        port=27000, 
                        block=True, 
                        size=(300, 460), 
                        position=(0,0), 
                        disable_cache=True, 
                        close_callback=close_callback, 
                        cmdline_args=['--browser-startup-dialog', 
                                '--incognito', '--no-experiments'])