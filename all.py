import pygame

# data
pg = pygame
screen_width = 800
screen_height = 800
screen = pg.display.set_mode((screen_width, screen_height))

# event

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
                draw_background()
                draw_balls()
                show_h()
                pass
            if e.type == pg.MOUSEBUTTONDOWN:
                show_ball()

        pg.display.update()

# display

def draw_grid(color = (0, 0, 0, 50)):
    pos = pg.mouse.get_pos()

    pg.draw.line(screen, color, (0, pos[1]), (screen_width, pos[1]))
    pg.draw.line(screen, color, (pos[0], 0), (pos[0], screen_height))

def draw_background():

    grid_width, grid_height = screen_width / 22, screen_height / 22

    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (222, 176, 49), [grid_width, grid_height, grid_width * 20, grid_height * 20]) # the color of grids

    draw_point([screen_width / 2, screen_height / 2]) # middle point

    draw_point([grid_width * 5, grid_height * 5])     # left up point
    draw_point([grid_width * 5, grid_height * 11])    # left middle point
    draw_point([grid_width * 5, grid_height * 17])    # left down point

    draw_point([grid_width * 11, grid_height * 5])    # middle up point   
    draw_point([grid_width * 11, grid_height * 17])   # middle down point

    draw_point([grid_width * 17, grid_height * 5])    # right up point
    draw_point([grid_width * 17, grid_height * 11])   # right middle point
    draw_point([grid_width * 17, grid_height * 17])   # right down point

    for i in range(2, 21):
        pg.draw.line(screen, (0, 0, 0), (grid_width * i,  grid_height * 2), (grid_width  * i, grid_height * 20)) # ㅣ
    for i in range(2, 21):
        pg.draw.line(screen, (0, 0, 0), (grid_width * 2, grid_height * i), (grid_width * 20, grid_height * i))   # ㅡ

def draw_ball(color, center):
    pg.draw.circle(screen, color, center, 18)


def draw_point(center):
    pg.draw.circle(screen, (0, 0, 0), center, 4)

#game

balls = []

for i in range(0, 18 + 1):
    l = []
    for ii in range(0, 18 + 1):
        l.append("s")
    balls.append(l)
    print(len(l))

print(len(balls))

is_black_turn = True

#h is hologram
h_color = (255, 138, 138)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def show_h():
    x, y = pg.mouse.get_pos()

    if not (screen_width / 44 * 3 <= x <= screen_width / 44 * 41 and screen_height / 44 * 3 <= y <= screen_height / 44 * 41):
        return
    
    draw_ball(h_color, [screen_width / 22 * round(x / (screen_width / 22)), screen_height / 22 * round(y / (screen_height / 22))])

    print(str(round(x / (screen_width / 22))) + "       " + str(round(y / (screen_height / 22))))


def show_ball():
    global is_black_turn
    mx, my = pg.mouse.get_pos()

    if not (screen_width / 44 * 3 <= mx <= screen_width / 44 * 41 and screen_height / 44 * 3 <= my <= screen_height / 44 * 41):
        return

    x = round(mx / (screen_width / 22))
    y = round(my / (screen_height / 22))

    print(x, y)

    if is_black_turn and balls[x - 2][y - 2] == "s":
        draw_ball(BLACK, [screen_width / 22 * x, screen_height / 22 * y])
        balls[x - 2][y - 2] = "b"
    elif balls[x - 2][y - 2] == "s":
        draw_ball(WHITE, [screen_width / 22 * x, screen_height / 22 * y])
        balls[x - 2][y - 2] = "w"
    is_black_turn = not is_black_turn

def draw_balls():
    for i in range(18 + 1):
        for ii in range(18 + 1):
        
            if balls[i][ii] == "s":
                continue

            x = (i + 2) * (screen_width / 22)
            y = (ii + 2) * (screen_height / 22)

            if balls[i][ii] == "b":
                draw_ball(BLACK, [x, y])
            else:
                draw_ball(WHITE, [x, y])


class App:

    def __init__(self):
        pg.init()
        pg.display.set_caption("오목")
        screen.fill((222, 176, 49))
        draw_background()
    
    def start(self):
        event.event()
        pass
        
if __name__ == "__main__":
    app = App()

    app.start()