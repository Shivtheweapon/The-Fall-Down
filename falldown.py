import uvage
import random
camera = uvage.Camera(800,600)
main_character = uvage.from_color(400, 100, "green", 40, 40)
global increasingSpeed
increasingSpeed = 6
touchingGround = False
floor_1 = uvage.from_color(350,200, "blue", 700, 60)
floor_2 = uvage.from_color(1150,200, "blue", 700, 60)
floor_3 = uvage.from_color(-350,400,"blue",700,60)
floor_4 = uvage.from_color(450,400,"blue",700,60)
floor_5 = uvage.from_color(-250,700,"blue",700,60)
floor_6 = uvage.from_color(550,700,"blue",700,60)
fallThroughFloor = uvage.from_color(400,650,"blue",800,100)
floor_list1 = []
global x
x = 140
global y
y = 0
global isPlaying
isPlaying = True
global z
z = -1




def floor_list():
    for each in floor_list1:
        global z
        each.speedy = z
        z -= .01

        if isPlaying:
            each.move_speed()

        if not main_character.bottom_touches(each) and not main_character.bottom_touches(fallThroughFloor):
            global increasingSpeed
            main_character.speedy = increasingSpeed
        if main_character.bottom_touches(each) or main_character.bottom_touches(fallThroughFloor):
            increasingSpeed = 6

    camera.draw(fallThroughFloor)

    add_floor()

def add_floor():
    x1 = random.randint(-350,350)
    x2 = x1 + 800
    y = 800
    floor_5 = uvage.from_color(x1, y, "blue", 700, 60)
    floor_6 = uvage.from_color(x2, y, "blue", 700, 60)
    global x
    x += 1
    if x % 150 == 0:
        floor_list1.append(floor_5)
        floor_list1.append(floor_6)

def things_to_draw():
    bigList = [main_character] + floor_list1
    for each in bigList:
        camera.draw(each)


def scoring():
    global x
    if x % 30 == 0:
        global y
        y += 1
    score = uvage.from_text(50,50, str(y), 50,"red")
    camera.draw(score)

def Fallthrough():
    global touchingGround
    if main_character.y > 575:
        touchingGround = True
    if main_character.x < 26:
        main_character.x = 26
    if main_character.x > 774:
        main_character.x = 774

def LeftOrRight():
    if uvage.is_pressing("left arrow"):
        main_character.speedx = -20
    if uvage.is_pressing("right arrow"):
        main_character.speedx = 20
def endGame():
    end = "GAME OVER"
    endGameScreen = uvage.from_text(400,300,end,200,'red')

    if main_character.y < 0:
        global isPlaying
        isPlaying = False
    if not isPlaying:
        camera.draw(endGameScreen)
        for each in floor_list1:
            each.speedy = 0




def tick():
    camera.clear("black")
    global increasingSpeed
    increasingSpeed += .13
    endGame()
    floor_list()
    things_to_draw()
    scoring()
    camera.display()
    Fallthrough()
    LeftOrRight()
    main_character.move_speed()
    print(x)





uvage.timer_loop(30, tick)

