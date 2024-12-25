from data import *
import event
import display

class App:

    def __init__(self):
        pg.init()
        pg.display.set_caption("오목")
        screen.fill((222, 176, 49))
        display.draw_background()
    
    def start(self):
        event.event()
        pass
        
if __name__ == "__main__":
    app = App()

    app.start()