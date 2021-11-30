from microbit import *
def on_button_pressed_a():
    player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

_11q: game.LedSprite = None
qq1: game.LedSprite = None
q: game.LedSprite = None
player: game.LedSprite = None
player = game.create_sprite(2, 4)
health = 2
game.set_score(0)

def on_forever():
    global q, qq1, _11q, health
    q = game.create_sprite(randint(0, 4), 0)
    qq1 = game.create_sprite(randint(0, 4), 0)
    _11q = game.create_sprite(randint(0, 4), 0)
    basic.pause(100)
    for index in range(4):
        q.change(LedSpriteProperty.Y, 1)
        _11q.change(LedSpriteProperty.Y, 1)
        qq1.change(LedSpriteProperty.Y, 1)
        basic.pause(1000)
    if q.is_touching(player) or (_11q.is_touching(player) or qq1.is_touching(player)):
        health += -1
    else:
        game.add_score(1)
    if health == 0:
        game.game_over()
    q.delete()
    qq1.delete()
    _11q.delete()
basic.forever(on_forever)
