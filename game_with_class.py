import pygame
import time
from math import fabs
import random

pygame.init()
clock = pygame.time.Clock()
# set up the screen display
screen_wh = {
    "display_width": 480,
    "display_height": 512
}
screen_size = (screen_wh["display_height"], screen_wh["display_width"])
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Game")

background_imgs = {
    "img1": "images/background.png",
    "img2": "images/grassground.png"
}

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

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


def image_display(source, x, y):
    img = pygame.image.load(source)
    screen.blit(img, [x, y])


def text_display(font, text, size, color):
    text_font = pygame.font.Font(font, size)
    text_dis = text_font.render(text, True, color)
    return text_dis


class characters:

    def __init__(self, x, y, speed_x, speed_y):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def movement_function(self, tick):
        if tick % 60 == 0:
            self.speed_x = random.randrange(-2, 3)
            self.speed_y = random.randrange(-2, 3)
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x < 32 or self.x > screen_wh["display_width"] - 64:
            self.speed_x *= -1
        if self.y < 32 or self.y > screen_wh["display_height"] - 64:
            self.speed_y *= -1

    def collision_detection(self, hero):
        if abs(hero.x - self.x) + abs(hero.y - self.y) < 32:
            return 1
        else:
            return 0

    def hp_manage(self):
        pass

    def exp_manage(self):
        pass


class hero:

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.win = 0
        self.death = 0

    def hero_move(self):
        if self.x < 0:
            self.x = 10
        elif self.x > screen_wh["display_width"] - 10:
            self.x = screen_wh["display_width"] - 10
        elif self.y < 0:
            self.y = 10
        elif self.y > screen_wh["display_height"] - 64:
            self.y = screen_wh["display_height"] - 64


class items:

    def __init__(self, x, y):
        pass


class scene_display:

    def __init__(self):
        pass

    def draw_img(self):
        pass

    def mouse_detection(self):
        pass


class monster(characters):

    def death(self, hero):
        print self.collision_detection(hero)
        if self.collision_detection(hero) == 1:
            hero.death += 1
            image_display(random.choice(background_imgs.values()), 0, 0)
            hero.x = random.randrange(100, 300)
            hero.y = random.randrange(100, 300)
        else:
            image_display("images/hero.png", hero1.x, hero1.y)


class goblin(characters):

    def exp_increase(self):
        pass

    def win(self, hero):
        if self.collision_detection(hero) == 1:
            hero.win += 1
            self.x = random.randrange(100, 300)
            self.y = random.randrange(100, 300)

        else:
            image_display("images/goblin.png", goblin1.x, goblin1.y)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 25)
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
        if click[0] == 1:
            game_on()
        screen.blit(play_text, [205, 255])
        pygame.display.update()
        clock.tick(15)


def game_on():
    tick = 0
    game_on = True
    while game_on:
        tick += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:  # keydown means a user pressed a key
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
            hero1.y -= hero1.speed
        if keys_down["down"]:
            hero1.y += hero1.speed
        if keys_down["left"]:
            hero1.x -= hero1.speed
        if keys_down["right"]:
            hero1.x += hero1.speed

        image_display(background_imgs["img1"], 0, 0)
        hero1.hero_move()
        monster1.movement_function(tick)
        goblin1.movement_function(tick)
        monster1.collision_detection(hero1)
        goblin1.collision_detection(hero1)
        goblin1.win(hero1)
        monster1.death(hero1)
        win_dis = text_display(None, "WINS: %d" % hero1.win, 25, red)
        screen.blit(win_dis, [40, 40])
        death_dis = text_display(None, "Death: %d" % hero1.death, 25, black)
        screen.blit(death_dis, [410, 410])
        image_display("images/monster.png", monster1.x, monster1.y)
        pygame.display.flip()


hero1 = hero(100, 100, 10)
monster1 = monster(50, 50, 4, 4)
goblin1 = goblin(200, 200, 4, 4)
game_intro()
game_on()
