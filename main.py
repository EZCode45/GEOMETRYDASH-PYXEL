import pyxel
pyxel.init(200, 200, 'GEOMETRYDASH', 90)
pyxel.mouse(True)
player_x = 50
player_y = 150
gravity = 1
obstacle_x = 145
obstacle_y = 150
obstacle_w = 10
obstacle_h = 10
player_w = 10
player_h = 10
player_y_vel = 0

def update():
    # pyxel.cls(3)
    global player_x, player_y, gravity, obstacle_x, obstacle_y, player_h, player_w, obstacle_h, obstacle_w, player_y_vel
    player = pyxel.rect(player_x, player_y, 10, 10, col = 20)
    obstacle = pyxel.rect(obstacle_x, obstacle_y, 10, 10, 5)
    player_y += gravity
    if player_y >= 150:
        gravity = 0
        if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            player_y_vel -= 50
    else:
        gravity = 1
    player_y += player_y_vel
    obstacle_x -= 1
    if obstacle_x == 2:
        obstacle_x = 145
    player_y_vel = 0
def draw():
    global player_x, player_y, obstacle_x, obstacle_y
    pyxel.rect(0, 0, 200, 200, 3)
    pyxel.rect(player_x, player_y, 10, 10, col = 20)
    pyxel.rect(0, 160, 300, 50, 1)
    pyxel.rect(obstacle_x, obstacle_y, 10, 10, 5)
pyxel.run(update, draw)