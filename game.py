from data import *
import display

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
    
    display.draw_ball(h_color, [screen_width / 22 * round(x / (screen_width / 22)), screen_height / 22 * round(y / (screen_height / 22))])

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
        display.draw_ball(BLACK, [screen_width / 22 * x, screen_height / 22 * y])
        balls[x - 2][y - 2] = "b"
    elif balls[x - 2][y - 2] == "s":
        display.draw_ball(WHITE, [screen_width / 22 * x, screen_height / 22 * y])
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
                display.draw_ball(BLACK, [x, y])
            else:
                display.draw_ball(WHITE, [x, y])
