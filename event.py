from data import *
import display
import game

e = [[]]

def event():
    clock = pg.time.Clock()
    running = True

    while running:

        clock.tick(60)
        
        for e in pg.event.get():
            
            if e.type == pg.QUIT:
                running = False
            
            if e.type == pg.MOUSEMOTION:
                display.draw_background()
                game.draw_balls()
                game.show_h()
                pass
            if e.type == pg.MOUSEBUTTONDOWN:
                game.show_ball()

        pg.display.update()