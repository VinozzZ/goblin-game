import pygame
import time
from math import fabs
import random

pygame.init()

screen_wh = {
    "display_width": 480,
    "display_height": 512
}
background_imgs = {
    "img1": "images/background.png",
    "img2": "images/grassground.png"
}
keys = {
     "right": 275,
     "left": 276,
     "up": 273,
     "down": 274
 }

keys_down = {
     "right": False,
     "left": False,
     "up": False,
     "down": False
 }
hero_dict = {
    "x": 100,
    "y": 100,
    "speed": 10,
    "wins": 0,
    "Death": 0
}
goblin_dict = {
    "x": 200,
    "y": 200,
    "speed": 10
}
monster_dict = {
    "x": 50,
    "y": 50,
    "speed_x": 4,
    "speed_y": 4
}
hero_width = 10
screen_size = (screen_wh["display_height"], screen_wh["display_width"])
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
background_img = pygame.image.load(background_imgs["img1"])
hero_img = pygame.image.load("images/hero.png")
goblin_img = pygame.image.load("images/goblin.png")
monster_img = pygame.image.load("images/monster.png")


def monster_moving():
    if monster_dict["x"] < 32 or monster_dict["x"] > screen_wh["display_width"] - 20:
        monster_dict["speed_x"] *= -1
    if monster_dict["y"] < 32 or monster_dict["y"] > screen_wh["display_height"] - 20:
        monster_dict["speed_y"] *= -1


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',25)
        intro_text = largeText.render("Goblin Game", True, black)
        screen.blit(intro_text, [150, 200])
        mouse = pygame.mouse.get_pos()
        smallText = pygame.font.Font(None, 30)
        # button "Play"
        if 200 + 50 > mouse[0] > 50 and 250 + 30 > mouse[1] > 30:
            pygame.draw.rect(screen, black, (200, 250, 50, 30))
            play_text = smallText.render("Play", True, red)
        else:
            pygame.draw.rect(screen, red, (200, 250, 50, 30))
            play_text = smallText.render("Play", True, black)
        click = pygame.mouse.get_pressed()
        if click[0] == 1 :
            game_on()
        screen.blit(play_text, [205, 255])
        pygame.display.update()
        clock.tick(15)

def music_sound():
    # Sound
    background_sound = pygame.mixer.Sound("sounds/music.wav")
    pygame.mixer.Sound.play(background_sound)
# ------------MAIN LOOP----------


def game_on():
    tick = 0
    game_on = True
    background_img = pygame.image.load(background_imgs["img1"])
    while game_on:
        tick += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:  # keydown means a user pressed a key
                if event.key == pygame.K_LEFT:
                        keys_down["left"] = True
                elif event.key == pygame.K_RIGHT:
                    keys_down["right"] = True
                elif event.key == keys["down"]:
                    keys_down["down"] = True
                elif event.key == keys["up"]:
                    keys_down["up"] = True
            elif event.type == pygame.KEYUP:
                for key in keys_down:
                    keys_down[key] = False

        if keys_down["up"]:
            hero_dict["y"] -= hero_dict["speed"]
        if keys_down["down"]:
            hero_dict["y"] += hero_dict["speed"]
        if keys_down["left"]:
            hero_dict["x"] -= hero_dict["speed"]
        if keys_down["right"]:
            hero_dict["x"] += hero_dict["speed"]

        if hero_dict["x"] < 0:
            hero_dict["x"] = 10
        elif hero_dict["x"] > screen_wh["display_width"] - 10:
            hero_dict["x"] = screen_wh["display_width"] - 10
        elif hero_dict["y"] < 0:
            hero_dict["y"] = 10
        elif hero_dict["y"] > screen_wh["display_height"] - 64:
            hero_dict["y"] = screen_wh["display_height"] - 64
    # collision detection
        if abs(hero_dict["x"] - goblin_dict["x"]) + abs(hero_dict["y"] - goblin_dict["y"]) < 32:
            goblin_dict["x"] = random.randint(0, 450)
            goblin_dict["y"] = random.randint(0, 482)
            hero_dict["wins"] += 1

    # monster eats the hero
        if abs(hero_dict["x"] - monster_dict["x"]) + abs(hero_dict["y"] - monster_dict["y"]) < 32:
            hero_dict["x"] = 0
            hero_dict["y"] = 0
            hero_dict["Death"] += 1
            background_img = pygame.image.load(random.choice(background_imgs.values()))
    # Monster move
        if tick % 60 == 0:
            monster_dict["speed_x"] = random.randrange(-2, 3)
            monster_dict["speed_y"] = random.randrange(-2, 3)
        monster_dict["x"] += monster_dict["speed_x"]
        monster_dict["y"] += monster_dict["speed_y"]
        monster_moving()
        screen.fill(white)
        screen.blit(background_img, [0, 0])
        wins_font = font.render("WINS: %d" % hero_dict["wins"], True, red)
        screen.blit(wins_font, [40, 40])
        death_font = font.render("Death: %d" % hero_dict["Death"], True, (0, 0, 0))
        screen.blit(death_font, [410, 410])
        screen.blit(hero_img, [hero_dict["x"], hero_dict["y"]])
        screen.blit(goblin_img, [goblin_dict["x"], goblin_dict["y"]])
        screen.blit(monster_img, [monster_dict["x"], monster_dict["y"]])
        pygame.display.flip()


music_sound()
game_intro()
