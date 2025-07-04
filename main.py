import pyxel
pyxel.init(200, 200, 'GEOMETRYDASH', 90)
pyxel.mouse(True)
player_x = 10
player_y = 150
gravity = 0.5
def update():
    player_y_vel = 0
    # pyxel.cls(3)
    global player_x, player_y, gravity
    player_y += gravity
    if player_y >= 150:
        gravity = 0
        if pyxel.btn(pyxel.KEY_SPACE):
            player_y_vel -= 20
    else:
        gravity = 0.5
    player_y += player_y_vel
def draw():
    global player_x, player_y
    pyxel.rect(0, 0, 200, 200, 3)
    pyxel.rect(player_x, player_y, 10, 10, col = 20)
pyxel.run(update, draw)