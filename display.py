from data import *

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