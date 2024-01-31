def on_up_pressed():
    global vx, vy
    vx = 0
    vy = -72
    player1.set_velocity(vx, vy)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_hit_wall(sprite, location):
    info.change_life_by(-1)
scene.on_hit_wall(SpriteKind.player, on_hit_wall)

def spawnFood(time: number, score: number):
    global total, chance
    total = 144
    if score > 10:
        chance = 100 / total + Math.sqrt(time) / 500
    else:
        chance = 100 / total
    for value in Map:
        if Math.percent_chance(chance):
            tiles.set_tile_at(value, sprites.castle.tile_grass2)
            tiles.set_wall_at(value, True)
            total += -1
    tiles.place_on_random_tile(person, sprites.builtin.field1)

def on_left_pressed():
    global vx, vy
    vx = -72
    vy = 0
    player1.set_velocity(vx, vy)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap(sprite2, otherSprite):
    info.change_score_by(1)
    spawnFood(game.runtime(), info.score())
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_right_pressed():
    global vx, vy
    vx = 72
    vy = 0
    player1.set_velocity(vx, vy)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    global vx, vy
    vx = 0
    vy = 72
    player1.set_velocity(vx, vy)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    game.game_over(False)
    game.splash("Score: " + ("" + str(info.score())),
        "High Score: " + ("" + str(info.high_score())))
info.on_life_zero(on_life_zero)

chance = 0
total = 0
vy = 0
vx = 0
Map: List[tiles.Location] = []
person: Sprite = None
player1: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
"""))
player1 = sprites.create(img("""
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
    """),
    SpriteKind.player)
person = sprites.create(img("""
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
    """),
    SpriteKind.food)
Map = tiles.get_tiles_by_type(sprites.builtin.field1)
scene.camera_follow_sprite(player1)
info.set_score(0)
person.set_position(120, 88)
info.set_life(10)
game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)