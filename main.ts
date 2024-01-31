controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    vx = 0
    vy = -72
    player1.setVelocity(vx, vy)
})
scene.onHitWall(SpriteKind.Player, function (sprite, location) {
    info.changeLifeBy(-1)
})
function spawnFood (time: number, score: number) {
    total = 144
    if (score > 10) {
        chance = 100 / total + Math.sqrt(time) / 500
    } else {
        chance = 100 / total
    }
    for (let value of Map) {
        if (Math.percentChance(chance)) {
            tiles.setTileAt(value, sprites.castle.tileGrass2)
            tiles.setWallAt(value, true)
            total += -1
        }
    }
    tiles.placeOnRandomTile(person, sprites.builtin.field1)
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    vx = -72
    vy = 0
    player1.setVelocity(vx, vy)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite2, otherSprite) {
    info.changeScoreBy(1)
    spawnFood(game.runtime(), info.score())
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    vx = 72
    vy = 0
    player1.setVelocity(vx, vy)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    vx = 0
    vy = 72
    player1.setVelocity(vx, vy)
})
info.onLifeZero(function () {
    game.gameOver(false)
    game.splash("Score: " + info.score(), "High Score: " + info.highScore())
})
let chance = 0
let total = 0
let vy = 0
let vx = 0
let Map: tiles.Location[] = []
let person: Sprite = null
let player1: Sprite = null
tiles.setCurrentTilemap(tilemap`level1`)
player1 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . 2 2 2 2 2 2 2 2 . . . . 
    . . . 2 4 2 2 2 2 2 2 c 2 . . . 
    . . 2 c 4 2 2 2 2 2 2 c c 2 . . 
    . 2 c c 4 4 4 4 4 4 2 c c 4 2 d 
    . 2 c 2 e e e e e e e b c 4 2 2 
    . 2 2 e b b e b b b e e b 4 2 2 
    . 2 e b b b e b b b b e 2 2 2 2 
    . e e 2 2 2 e 2 2 2 2 2 e 2 2 2 
    . e e e e e e f e e e f e 2 d d 
    . e e e e e e f e e f e e e 2 d 
    . e e e e e e f f f e e e e e e 
    . e f f f f e e e e f f f e e e 
    . . f f f f f e e f f f f f e . 
    . . . f f f . . . . f f f f . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
person = sprites.create(img`
    . . . . f f f f . . . . . 
    . . f f f f f f f f . . . 
    . f f f f f f c f f f . . 
    f f f f f f c c f f f c . 
    f f f c f f f f f f f c . 
    c c c f f f e e f f c c . 
    f f f f f e e f f c c f . 
    f f f b f e e f b f f f . 
    . f 4 1 f 4 4 f 1 4 f . . 
    . f e 4 4 4 4 4 4 e f . . 
    . f f f e e e e f f f . . 
    f e f b 7 7 7 7 b f e f . 
    e 4 f 7 7 7 7 7 7 f 4 e . 
    e e f 6 6 6 6 6 6 f e e . 
    . . . f f f f f f . . . . 
    . . . f f . . f f . . . . 
    `, SpriteKind.Food)
Map = tiles.getTilesByType(sprites.builtin.field1)
scene.cameraFollowSprite(player1)
info.setScore(0)
person.setPosition(120, 88)
info.setLife(10)
game.setGameOverScoringType(game.ScoringType.HighScore)
