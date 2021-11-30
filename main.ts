input.onButtonPressed(Button.A, function on_button_pressed_a() {
    player.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    player.change(LedSpriteProperty.X, 1)
})
let _11q : game.LedSprite = null
let qq1 : game.LedSprite = null
let q : game.LedSprite = null
let player : game.LedSprite = null
player = game.createSprite(2, 4)
let health = 2
game.setScore(0)
basic.forever(function on_forever() {
    
    q = game.createSprite(randint(0, 4), 0)
    qq1 = game.createSprite(randint(0, 4), 0)
    _11q = game.createSprite(randint(0, 4), 0)
    basic.pause(100)
    for (let index = 0; index < 4; index++) {
        q.change(LedSpriteProperty.Y, 1)
        _11q.change(LedSpriteProperty.Y, 1)
        qq1.change(LedSpriteProperty.Y, 1)
        basic.pause(1000)
    }
    if (q.isTouching(player) || (_11q.isTouching(player) || qq1.isTouching(player))) {
        health += -1
    } else {
        game.addScore(1)
    }
    
    if (health == 0) {
        game.gameOver()
    }
    
    q.delete()
    qq1.delete()
    _11q.delete()
})
