import pygame
import math
import random
import time
# Importing Pygame, which is the main library I use, and some other libraries like random which
# I use to generate random numbers with a given interval

from levels import *
# Here I imported a giant array from another file. That array represented a tile map that I use to
# create the level later on. The reason I didn't just include this class in this file was because it was too
# large, and it wouldn't load properly when I tried to convert this file to a pdf.
# ** There's no citation for it because I made the tile map, it wasn't imported from online **

pygame.init()

# ---------------- Setting up the screen, assigning some global variables, and loading text fonts
screen = pygame.display.set_mode((1050, 700))
# screen = pygame.display.set_mode((1200, 650))
clock = pygame.time.Clock()
fps = 60
screen_width = screen.get_width()
screen_height = screen.get_height()
screen2 = pygame.Surface((screen_width, screen_height)).convert_alpha()
screen3 = pygame.Surface((screen_width, screen_height)).convert_alpha()
screen3.set_alpha(100)
screen4 = pygame.Surface((screen_width, screen_height)).convert_alpha()
timer = 0
shake = [0, 0]
shake_strength = 3
scroll = [0, 0]
bulletR = 20
scroll_counter = 0
tile_size = 30
print(pygame.font.get_fonts())
font15 = pygame.font.Font("freesansbold.ttf", 15)
font20 = pygame.font.Font("freesansbold.ttf", 20)
font30 = pygame.font.Font("freesansbold.ttf", 30)
font40 = pygame.font.Font("freesansbold.ttf", 40)
better_font40 = pygame.font.SysFont("keyboard.ttf", 40)
font50 = pygame.font.Font("freesansbold.ttf", 50)
font100 = pygame.font.Font("freesansbold.ttf", 100)

# ---------------- Loading in the images, removing the backgrounds, and rescaling some of them
scrollImg = pygame.transform.scale(pygame.image.load("skull_scroll1.png"), (tile_size, tile_size)).convert_alpha()
scrollDimensions = [tile_size, tile_size]
vineImg = pygame.transform.scale(pygame.image.load("vine.png"), (tile_size, tile_size)).convert_alpha()
bulletImg = pygame.transform.scale(pygame.image.load("bullet2.png"), (bulletR * 4, bulletR * 4)).convert_alpha()
backgroundImg = pygame.transform.scale(pygame.image.load("background.png"), (1200, 900)).convert_alpha().convert()
healthbarImg = pygame.image.load("healthbar2.png").convert_alpha()
lensImg = pygame.image.load("focuslens.png").convert_alpha()
bulletGlowImg = pygame.image.load("bulletglow.png").convert_alpha()
scrollGlowImg = pygame.image.load("scrollGlow.png").convert_alpha()
scrollGlowImg.set_alpha(200)
shroomImg = pygame.image.load("shroom.png").convert_alpha()
hpBoxImg = pygame.image.load("healthbox.png").convert_alpha()
spawnerImg = pygame.image.load("spawnerImg.png").convert_alpha()
arrowsImg = pygame.image.load("arrows.png").convert_alpha()
arrowsImgL = pygame.image.load("arrowsL.png").convert_alpha()
arrowsImgR = pygame.image.load("arrowsR.png").convert_alpha()
arrowsImgU = pygame.image.load("arrowsU.png").convert_alpha()
arrowsImgRU = pygame.image.load("arrowsLU.png").convert_alpha()
arrowsImgLU = pygame.image.load("arrowsRU.png").convert_alpha()
arrowsImgRL = pygame.image.load("arrowsRLpng.png").convert_alpha()
arrowsImgRLU = pygame.image.load("arrowsLRU.png").convert_alpha()
fallTextUI = pygame.image.load("don't_fall.png").convert_alpha()
vinesTextUI = pygame.image.load("vines_reset_your_jump.png").convert_alpha()
bulletsTextUI = pygame.image.load("avoid_bullets.png").convert_alpha()
mushroomsTextUI = pygame.transform.scale(pygame.image.load("and_mushrooms.png").convert_alpha(), (175, 200))
scrollsTextUI = pygame.transform.scale(pygame.image.load("scroll_text.png").convert_alpha(), (170, 200))
glTextUI = pygame.image.load("glText.png").convert_alpha()
debugTextUI = pygame.transform.scale(pygame.image.load("debugText.png").convert_alpha(), (1000, 500))
text_dimensions = (80, 80)
scrollTextD = pygame.transform.scale(pygame.image.load("scrolltextdenominator.png").convert_alpha(), text_dimensions)
scrollText1 = pygame.transform.scale(pygame.image.load("scrolltext1.png").convert_alpha(), text_dimensions)
scrollText2 = pygame.transform.scale(pygame.image.load("scrolltext2.png").convert_alpha(), text_dimensions)
scrollText3 = pygame.transform.scale(pygame.image.load("scrolltext3.png").convert_alpha(), text_dimensions)
scrollText4 = pygame.transform.scale(pygame.image.load("scrolltext4.png").convert_alpha(), text_dimensions)
scrollText5 = pygame.transform.scale(pygame.image.load("scrolltext5.png").convert_alpha(), text_dimensions)
scrollText6 = pygame.transform.scale(pygame.image.load("scrolltext6.png").convert_alpha(), text_dimensions)
scrollText7 = pygame.transform.scale(pygame.image.load("scrolltext7.png").convert_alpha(), text_dimensions)
scrollText8 = pygame.transform.scale(pygame.image.load("scrolltext8.png").convert_alpha(), text_dimensions)
scrollText9 = pygame.transform.scale(pygame.image.load("scrolltext9.png").convert_alpha(), text_dimensions)
scrollText10 = pygame.transform.scale(pygame.image.load("scrolltext10.png").convert_alpha(), text_dimensions)
scrollText11 = pygame.transform.scale(pygame.image.load("scrolltext11.png").convert_alpha(), text_dimensions)

# ---------------- Loading sound effects and creating variables to store them
# *** I didn't make this music it was posted on the channel "CrazyBlox" ***
# Here's a link to the YouTube video
# https://www.youtube.com/watch?v=gvwLSFve-tY&ab_channel=Crazyblox
# pygame.mixer.music.load("Y2Mate.is - Flood Escape 2 OST - Cave System-gvwLSFve-tY-128k-1656398163711.mp3")
# pygame.mixer.music.play(-1)


# Here I create rects (which are rectangles that act as hitboxes) for each tile and other entity in the tile map
# This is where I am using the level data I imported from the other file I mentioned earlier
tile_rects = []
bounds_rects = []
vines = []
bells = []
hpBoxes = []
y = 0
for row in LevelData.tile_map1:
    x = 0
    for tile in row:
        if tile == 1:
            bounds_rects.append(pygame.rect.Rect(tile_size * x, tile_size * y, tile_size, tile_size))
        if tile == 3:
            tile_rects.append(pygame.rect.Rect(tile_size * x, tile_size * y, tile_size, tile_size))
        if tile == 2:
            vines.append(pygame.rect.Rect(tile_size * x, tile_size * y, tile_size, tile_size))
        if tile == 4:
            bells.append(pygame.rect.Rect(tile_size * x, tile_size * y, tile_size, tile_size))
        if tile == 5:
            hpBoxes.append(pygame.rect.Rect(tile_size * x, tile_size * y, tile_size, tile_size))
        x += 1
    y += 1


# ---------------- Shockwave class, this is a visual effect that basically just creates an expanding circle that decays over time in width
class Shockwave:
    # Function for initializing the shockwave object with its parameters
    def __init__(self, sx, sy, duration, size, max_size, width, color, color2, shadow):
        self.x = sx
        self.y = sy
        self.duration = duration
        self.size = size
        self.max_size = max_size
        self.width = width
        self.color = color
        self.color2 = color2
        self.shadow = shadow

    # This function is run each frame and increases the size of the shockwave but decreases the width
    def expand(self):
        self.size += dt * (self.max_size-self.size)/(10 * self.duration)
        if self.size/self.max_size < 0.8:
            self.width -= 0.03 * dt
        else:
            self.width -= 0.1 * dt

    # This function draws the shockwave (and its shadow) on the screen
    def blit(self):
        pygame.draw.circle(screen2, self.color2, (self.x - self.shadow - shifted_scroll[0], self.y + self.shadow - shifted_scroll[1]), self.size, int(self.width))
        pygame.draw.circle(screen2, self.color, (self.x - shifted_scroll[0], self.y - shifted_scroll[1]), self.size, int(self.width))


# Creating the list of all the shockwave objects
shockwaves = []


# ---------------- Particle Class, this is used for the dust particles that appear behind the player when the player moves
class Particle:
    # Function for initializing the particle object with its parameters
    def __init__(self, px, py, x_vel, y_vel, color, color2, size, decay, gravity, bounciness):
        self.x = px
        self.y = py
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color
        self.color2 = color2
        self.size = size
        self.decay = decay
        self.gravity = gravity
        self.bounciness = bounciness

    # Function for drawing the particle on the screen
    def blit(self):
        pygame.draw.circle(screen2, self.color2, (self.x - self.size / 4 - shifted_scroll[0], self.y + self.size / 4 - shifted_scroll[1]), self.size)
        pygame.draw.circle(screen2, self.color, (self.x - shifted_scroll[0], self.y - shifted_scroll[1]), self.size)

    # Function that is called every frame for moving the particle and detecting collisions with the tiles
    # This function takes a second parameter called "blocks", which is just a list of all the tile rects
    def move(self, blocks):
        self.x += (self.x_vel * dt)
        self.y += (self.y_vel * dt)
        self.y_vel += (self.gravity * dt)
        self.size -= (self.decay * dt)

        for bl in blocks:
            if bl.collidepoint(self.x, self.y):
                if math.fabs(self.y - bl.top) < (self.y_vel + 10):
                    if self.y_vel > 0:
                        self.y = bl.top
                        self.y_vel *= -self.bounciness
                if math.fabs(self.x - bl.left) < (self.x_vel + 10):
                    self.x = bl.left
                    self.x_vel *= -self.bounciness
                if math.fabs(self.x - bl.right) < (self.x_vel + 10):
                    self.x = bl.right
                    self.x_vel *= -self.bounciness


# Defining the list that holds all the dust objects
dust = []

# ---------------- Color Classes — These are just classes that hold RGB values
# that I found online from a color palette called "Endesga" on lospec.com (I made the ExplosiveColors palette)


class ExplosiveColors:
    def __init__(self):
        pass

    white = (235, 237, 233)
    orange = (218, 134, 62)
    red = (117, 36, 5)
    cream = (232, 193, 112)
    purple = (36, 21, 39)
    light_purple = (62, 33, 55)
    blue = (21, 29, 40)
    grey = (147, 153, 173)
    pink = (212, 108, 127)


class Endesga:
    maroon_red = (87, 28, 39)
    lighter_maroon_red = (127, 36, 51)
    dark_green = (9, 26, 23)
    light_brown = (191, 111, 74)
    black = (19, 19, 19)
    grey_blue = (66, 76, 110)
    cream = (237, 171, 80)
    white = (255, 255, 255)
    very_light_blue = (199, 207, 221)


# ---------------- Variable that stores whether the player is moving or not
moving = 0


# ---------------- Player Class
# This is the object that the player controls
class Player:
    # This function initializes the player's parameters
    def __init__(self, p_rect, p_x_vel, p_y_vel, orb, hp, ahp, mana, jumps):
        self.rect = p_rect
        self.x_vel = p_x_vel
        self.y_vel = p_y_vel
        self.orb = orb
        self.hp = hp
        self.mana = mana
        self.jumps = jumps
        self.apparentHealth = ahp

    # This function allows the player to move based on user inputs through the arrow keys
    def set_move(self, m):
        if m == -1:
            self.x_vel = -2
            if random.randint(0, 5) == 1:
                dust.append(Particle(self.rect.x + self.rect.width, self.rect.y + self.rect.height, random.uniform(-1, 1), random.uniform(-2, -1), Endesga.cream, Endesga.black, random.randint(3, 5), random.uniform(0.06, 0.08), 0.1, 0.8))
        if m == 1:
            self.x_vel = 2
            if random.randint(0, 5) == 1:
                dust.append(Particle(self.rect.x, self.rect.y + self.rect.height, random.uniform(-1, 1), random.uniform(-2, -1), Endesga.cream, Endesga.black, random.randint(3, 5), random.uniform(0.04, 0.08), 0.1, 0.8))
        if m == 0:
            self.x_vel = 0

    # This function moves the player based on its stored velocities
    def move(self):
        scroll[0] += (self.rect.x - scroll[0]) / 10
        scroll[1] += (self.rect.y - scroll[1]) / 10
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        if not self.orb:
            if self.y_vel < 7:
                self.y_vel += 0.2

    # These functions detect collisions between the player's hitbox and other entities in the world
    # The collide function detects collisions between the player and the tiles in the map
    def collide(self, rects):
        for rect in rects:
            if rect.colliderect(self.rect):
                if math.fabs(rect.top - self.rect.bottom) < (tile_size / 3):
                    self.rect.bottom = rect.top
                    self.y_vel = 0
                    self.jumps = 2
                if math.fabs(rect.bottom - self.rect.top) < (tile_size / 3):
                    self.rect.top = rect.bottom
                    self.y_vel = 0
            if rect.colliderect(self.rect):
                if math.fabs(rect.left - self.rect.right) < (tile_size / 3):
                    self.rect.x = rect.left - self.rect.width
                if math.fabs(rect.right - self.rect.left) < (tile_size / 3):
                    self.rect.x = rect.right

    # The collideV function detects collisions with the player's hitbox and vines
    # This function takes in the input "vin", which represents a list of all the vine hitboxes
    def collideV(self, vin):
        for v in vin:
            if v.colliderect(self.rect):
                if self.y_vel > 1:
                    self.y_vel *= 0.95
                self.jumps = 2

    # The collideB function detects collisions with the player's hitbox and mushrooms. If it does detect a collision,
    # it also returns a value "c" which is used as a timer for screen shake
    # This function takes in the input "bel", which represents a list of all the mushroom hitboxes
    def collideB(self, bel):
        c = 0
        for be in bel:
            if be.colliderect(self.rect):
                p.hp -= 5
                c = fps * 0.2
                if random.randint(0, 5) == 1:
                    sparks.append(Spark(be.x + tile_size / 2, be.y + tile_size / 2, 9, Endesga.lighter_maroon_red, Endesga.maroon_red, random.randint(4, 6), random.uniform(0, math.pi * 2), 0.2, 0.4, 0, 0, 10))
        return c

    # The collideH function detects collisions with the player's hitbox and health boxes. If it detects a collision it
    # creates a shockwave and appends it to the "sw" list
    # This function takes in the input "health_boxes", which represents a list of all the health boxes' hitboxes, and
    # "sw", which represents a list of all the shockwaves currently on the screen

    def collideH(self, health_boxes, sw):
        for h in health_boxes:
            if h.colliderect(self.rect):
                p.hp = 1000
                sw.append(Shockwave(h.x + h.width / 2, h.y + h.height / 2, 2, 1, 100, 3, Endesga.lighter_maroon_red, Endesga.maroon_red, 3))
                sw.append(Shockwave(h.x + h.width / 2, h.y + h.height / 2, 2, 25, 150, 3, Endesga.lighter_maroon_red, Endesga.maroon_red, 3))
                health_boxes.remove(h)


# 100, 50 is default spawn point
# 2400, 1050 for dev hideout
# This is defining the player object that will be used in the rest of the code. It does this by passing in
# many parameters to define the player object
p = Player(pygame.rect.Rect(100, 50, 17, 27), 0, -5, False, 1000, 1000, 5, 2)

# This is the list that will hold all the bullet objects
bullets = []


# ---------------- Bullet Class - This class is for the floating orbs that deal damage to the player
class Bullet:
    # This initializes the bullet object with its parameters
    def __init__(self, rect, bx, by, x_vel, y_vel, ang, ricochet, col, dmg, glow, b_timer):
        self.rect = rect
        self.x = bx
        self.y = by
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.angle = ang
        self.ric = ricochet
        self.col = col
        self.dmg = dmg
        self.glow = glow
        self.timer = b_timer

    # This detects whether the bullet has collided with a tile rect and changes the direction the bullet is moving
    # if there is a collision detected
    # *** This function is not used in this program ***
    def collide(self, tiles):
        for ti in tiles:
            if ti.colliderect(self.rect):
                if math.fabs(ti.top - self.y - self.rect.height) < (tile_size / 3):
                    self.y = ti.top - 5 - self.rect.height
                    self.y_vel *= -1
                    self.ric -= 1
                if math.fabs(ti.bottom - self.y) < (tile_size / 3):
                    self.y = ti.bottom + 5
                    self.y_vel *= -1
                    self.ric -= 1
            if ti.colliderect(self.rect):
                if math.fabs(ti.left - self.x - self.rect.width) < (tile_size / 3):
                    self.x = ti.left - 5 - self.rect.width
                    self.x_vel *= -1
                    self.ric -= 1
                if math.fabs(ti.right - self.rect.left) < (tile_size / 3):
                    self.x = ti.right + 5
                    self.x_vel *= -1
                    self.ric -= 1
        self.rect.x = self.x
        self.rect.y = self.y

    # This function moves the bullet and draws it onto the screen, along with a glow sprite that changes in size using a sin wave
    def move(self):
        rad = math.cos(self.glow) * 10
        GlowImgScaled = pygame.transform.scale(bulletGlowImg, (60 + rad, 60 + rad))
        self.timer += 1
        self.glow += math.pi / fps
        # pygame.draw.circle(screen2, self.col, (self.x + self.rect.width / 2 - shifted_scroll[0], self.y + self.rect.width / 2 - shifted_scroll[1]), self.rect.width / 2)
        # pygame.draw.circle(screen3, self.col, (self.x + self.rect.width / 2 - shifted_scroll[0], self.y + self.rect.width / 2 - shifted_scroll[1]), self.rect.width + math.fabs(math.cos(self.glow)) * 5)
        screen2.blit(GlowImgScaled, (self.x + self.rect.width / 2 - shifted_scroll[0] - 30 - rad / 2, self.y + self.rect.width / 2 - shifted_scroll[1] - 30 - rad / 2))
        screen2.blit(bulletImg, (self.x - self.rect.width * 1.5 - shifted_scroll[0], self.y - self.rect.height * 1.5 - shifted_scroll[1]))
        # pygame.draw.rect(screen2, ExplosiveColors.red, pygame.rect.Rect(self.x - shifted_scroll[0], self.y - shifted_scroll[1], self.rect.width, self.rect.height))
        # pygame.draw.rect(screen3, ExplosiveColors.red, b.rect)
        self.x += self.x_vel * self.angle[0]
        self.y += self.y_vel * self.angle[1]


# ---------------- Scroll — This is the main game object that the player must collect to win
class Scroll:
    # This initializes the scroll's parameters
    def __init__(self, rect, picked, image, bob, added):
        self.rect = rect
        self.picked = picked
        self.image = image
        self.bob = bob
        self.added = added

    # This function detects collisions with the player and sroll
    # This function takes in the input "player", which it uses to access the player's hitbox (called player.rect)
    def collide(self, player):
        global scroll_counter
        if self.rect.colliderect(player.rect):
            self.picked = True

        if self.picked:
            if not self.added:
                shockwaves.append(Shockwave(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2, 2, 1, 100, 3, Endesga.cream, Endesga.black, 10))
                shockwaves.append(Shockwave(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2, 2, 25, 150, 3, Endesga.cream, Endesga.black, 10))
                for o in range(30):
                    sparks.append(Spark(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2, 9, Endesga.cream, Endesga.black, random.randint(4, 6), random.uniform(0, math.pi * 2), 0.2, 0.4, 0, 0, 10))
                scroll_counter += 1
                self.added = True

    # This function draws the scroll onto the screen and moves it up and down based on a sin wave
    def draw(self):
        self.bob += math.pi / fps
        if not self.picked:
            rad = math.cos(self.bob) * 10
            GlowImgScaled = pygame.transform.scale(scrollGlowImg, (rad + self.rect.width * 3, rad + self.rect.height * 3))
            screen2.blit(self.image, (self.rect.x - shifted_scroll[0], self.rect.y - math.cos(self.bob) * 5 - shifted_scroll[1]))
            # pygame.draw.circle(screen4, (95, 55, 37, 50), (self.rect.x - shifted_scroll[0] + self.rect.width / 2, self.rect.y - math.cos(self.bob) * 5 - shifted_scroll[1] + self.rect.height / 2), self.rect.width + math.cos(self.bob) * 5)
            # pygame.draw.circle(screen4, (95, 55, 37, 100), (self.rect.x - shifted_scroll[0] + self.rect.width / 2, self.rect.y - math.cos(self.bob) * 5 - shifted_scroll[1] + self.rect.height / 2), self.rect.width * 0.75 + math.cos(self.bob) * 2)
            screen4.blit(GlowImgScaled, (self.rect.x - shifted_scroll[0] - self.rect.width - rad / 2, self.rect.y - math.cos(self.bob) * 5 - shifted_scroll[1] - self.rect.height - rad / 2))


# Defining all the scroll objects and placing them in a list called "scrolls" that can be referenced later
scrolls = [Scroll(pygame.rect.Rect(1470, 110, scrollDimensions[0], scrollDimensions[1]), False, scrollImg, random.uniform(0, math.pi * 2), False),
           Scroll(pygame.rect.Rect(2480, 75, scrollDimensions[0], scrollDimensions[1]), False, scrollImg, random.uniform(0, math.pi * 2), False),
           Scroll(pygame.rect.Rect(1010, 105, scrollDimensions[0], scrollDimensions[1]), False, scrollImg, random.uniform(0, math.pi * 2), False),
           Scroll(pygame.rect.Rect(850, 260, scrollDimensions[0], scrollDimensions[1]), False, scrollImg, random.uniform(0, math.pi * 2), False),
           Scroll(pygame.rect.Rect(2400, 950, scrollDimensions[0], scrollDimensions[1]), False, scrollImg, random.uniform(0, math.pi * 2), False),
           Scroll(pygame.rect.Rect(520, 800, scrollDimensions[0], scrollDimensions[1]), False, scrollImg, random.uniform(0, math.pi * 2), False),
           Scroll(pygame.rect.Rect(200, 800, scrollDimensions[0], scrollDimensions[1]), False, scrollImg, random.uniform(0, math.pi * 2), False),
           Scroll(pygame.rect.Rect(330, 600, scrollDimensions[0], scrollDimensions[1]), False, scrollImg, random.uniform(0, math.pi * 2), False),
           Scroll(pygame.rect.Rect(450, 500, scrollDimensions[0], scrollDimensions[1]), False, scrollImg, random.uniform(0, math.pi * 2), False),
           Scroll(pygame.rect.Rect(200, 400, scrollDimensions[0], scrollDimensions[1]), False, scrollImg, random.uniform(0, math.pi * 2), False),
           Scroll(pygame.rect.Rect(310, 900, scrollDimensions[0], scrollDimensions[1]), False, scrollImg, random.uniform(0, math.pi * 2), False)]


# Spawner class
# This class spawns bullets at random intervals
class Spawner:
    # This function is for initializing the spawners and its parameters
    def __init__(self, sx, sy, rate, b_list):
        self.x = sx
        self.y = sy
        self.rate = rate
        self.list = b_list

    # This function spawns bullets by appending a bullet object to the "bullets" list, which contains the rest of the bullet objects
    def spawn(self):
        for bullet in range(self.rate):
            if random.randint(0, 100) == 1:
                a = random.uniform(0, 2 * math.pi)
                self.list.append(Bullet(pygame.rect.Rect(self.x + tile_size / 2, self.y + tile_size / 2, bulletR, bulletR),
                                        self.x + tile_size / 2, self.y + tile_size / 2, random.uniform(1, 2), random.uniform(1, 2),
                                        [math.cos(a), math.sin(a)], 0, Endesga.maroon_red, 50 + random.randint(-20, 20),
                                        random.uniform(0, math.pi * 2), 0))

    # This function draws the spawner image on the screen
    def draw(self):
        screen2.blit(spawnerImg, (self.x - shifted_scroll[0], self.y - shifted_scroll[1]))


# This is defining all the spawner objects and placing them in a list called "spawners" which is referenced later
spawners = [Spawner(1000, -100, 5, bullets),
            Spawner(2070, 350, 5, bullets),
            Spawner(1750, -50, 5, bullets),
            Spawner(1080, 400, 5, bullets),
            Spawner(300, 600, 5, bullets),
            Spawner(290, 880, 5, bullets)]


# This is the spark class, which is used for visual effects
class Spark:
    # This function initializes the spark object by taking in parameters
    def __init__(self, sx, sy, vel, color, color2, size, angle, decay, speed_decay, rotation, gravity, length):
        self.x = sx
        self.y = sy
        self.vel = vel
        self.color = color
        self.color2 = color2
        self.size = size
        self.angle = angle
        self.decay = decay
        self.gravity = gravity
        self.rotation = rotation
        self.speed_decay = speed_decay
        self.length = length

    # This function is used for creating the vertices of the spark, in the shape of a diamond, using parameters given
    # when the object was initialized such as the x, y, size, length, and angle
    # This function then uses those points to draw the polygon on the screen
    # The function also draws a shadow below the diamond using the points and the "shadow" parameter
    def blit(self):
        points = [(self.x + (self.size * self.length/3 * math.cos(self.angle)) - self.size - shifted_scroll[0], self.y + (self.size * 2 * math.sin(self.angle)) + self.size - shifted_scroll[1]),
                  (self.x + (self.size * math.cos(self.angle + math.pi / 2)) - self.size - shifted_scroll[0], self.y + (self.size * math.sin(self.angle + math.pi / 2)) + self.size - shifted_scroll[1]),
                  (self.x + (self.size * 2 * self.length/3 * math.cos(self.angle + math.pi)) - self.size - shifted_scroll[0], self.y + (self.size * 3 * math.sin(self.angle + math.pi)) + self.size - shifted_scroll[1]),
                  (self.x + (self.size * math.cos(self.angle - math.pi / 2)) - self.size - shifted_scroll[0], self.y + (self.size * math.sin(self.angle - math.pi / 2)) + self.size - shifted_scroll[1])]
        pygame.draw.polygon(screen2, self.color2, points)
        points = [(self.x + (self.size * self.length/3 * math.cos(self.angle)) - shifted_scroll[0], self.y + (self.size * 2 * math.sin(self.angle)) - shifted_scroll[1]),
                  (self.x + (self.size * math.cos(self.angle + math.pi / 2)) - shifted_scroll[0], self.y + (self.size * math.sin(self.angle + math.pi/2)) - shifted_scroll[1]),
                  (self.x + (self.size * 2 * self.length/3 * math.cos(self.angle + math.pi)) - shifted_scroll[0], self.y + (self.size * 3 * math.sin(self.angle + math.pi)) - shifted_scroll[1]),
                  (self.x + (self.size * math.cos(self.angle - math.pi / 2)) - shifted_scroll[0], self.y + (self.size * math.sin(self.angle - math.pi/2)) - shifted_scroll[1])]
        pygame.draw.polygon(screen2, self.color, points)

    # This function uses the angle, decay, gravity, rotation, and speed_decay parameters to move the points
    def move(self):
        self.x += self.vel * math.cos(self.angle) * dt
        self.y += self.gravity * dt
        self.y += self.vel * math.sin(self.angle) * dt
        self.size -= self.decay * dt
        self.rotation = 1 / (self.size * 20)
        if self.vel > 0:
            self.vel -= self.speed_decay * dt
        if 3 * math.pi / 2 > self.angle > math.pi / 2:
            self.angle -= self.rotation * dt
        if 5 * math.pi / 2 > self.angle > 3 * math.pi / 2:
            self.angle += self.rotation * dt
        if math.pi / 2 > self.angle > 0:
            self.angle += self.rotation * dt


# This is the sparks list that holds all the spark objects
sparks = []

# This is the list that holds all the lines in the background
lines = []
# This for loop creates the background lines and appends them to the "lines" list
for i in range(33):
    lines.append([[-i * 200 + 1200, -500], [500, 1400], random.randint(50, 60)])


# This function takes in the "ev" parameter, which is a built-in function that detects the player's key presses
# Using this "ev" parameter, the function executes different sections of code based on what the keypress is
def detect_DOWN_events(player, ev, mu, mr, ml):
    if ev == pygame.K_UP:
        if player.jumps > 0:
            mu = True
            player.y_vel = -5
            player.jumps -= 1
    if event.key == pygame.K_RIGHT:
        Player.set_move(player, 1)
        mr = True
    if event.key == pygame.K_LEFT:
        Player.set_move(player, -1)
        ml = True
    if event.key == pygame.K_SPACE:
        if player.mana > 1:
            player.orb = not p.orb
    return mu, mr, ml


# This function is very similar to the function above, taking in a similar "ev" input that represents key presses
# However, this function detects when the key is lifted rather than when the key is pressed
def detect_UP_events(player, ev, mu, mr, ml):
    if ev == pygame.K_RIGHT:
        Player.set_move(player, 0)
        mr = False
    if event.key == pygame.K_LEFT:
        Player.set_move(player, 0)
        ml = False
    if event.key == pygame.K_UP:
        mu = False
    return mu, mr, ml


# Defining some more variables to use in the game loop
oscillating_random_thing = 0
ShakeCounter = 0
moveR = False
moveL = False
moveU = False
# ---------------- Main Game Loop
last_time = time.time()
running = True
while running:

    # ---------------- Reset Variables and Clear screens
    oscillating_random_thing += math.pi/fps
    click = False
    shifted_scroll = [scroll[0] - screen_width / 2, scroll[1] - screen_height / 2]
    mx, my = pygame.mouse.get_pos()
    screen.fill(Endesga.dark_green)
    screen2.fill(Endesga.dark_green)
    # screen2.blit(backgroundImg, ((-shifted_scroll[0] / 10 - 50), (-shifted_scroll[1] / 10 - 100)))
    screen3.fill((0, 0, 0, 0))
    screen4.fill((0, 0, 0, 0))
    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()
    timer -= 1 * dt
    shake = [0, 0]

    # ---------------- Drawing Background lines onto the screen
    for line in lines:
        if line[0][0] > 6100:
            line[0][0] = -500
        line[0][0] += 5
        line[1][0] = line[0][0] - 3600
        # pygame.draw.line(screen2, (0, 0, 0), (line[0][0] - shifted_scroll[0], line[0][1] - shifted_scroll[1]), (line[1][0] - shifted_scroll[0], line[1][1] - shifted_scroll[1]), line[2])

    # ---------------- Drawing Background Text onto the screen
    screen2.blit(fallTextUI, (425 - shifted_scroll[0], 200 - shifted_scroll[1]))
    screen2.blit(vinesTextUI, (650 - shifted_scroll[0], 50 - shifted_scroll[1]))
    screen2.blit(bulletsTextUI, (1000 - shifted_scroll[0], -100 - shifted_scroll[1]))
    screen2.blit(mushroomsTextUI, (1220 - shifted_scroll[0], 170 - shifted_scroll[1]))
    screen2.blit(scrollsTextUI, (1495 - shifted_scroll[0], 69 - shifted_scroll[1]))
    screen2.blit(glTextUI, (1750 - shifted_scroll[0], 0 - shifted_scroll[1]))
    screen2.blit(debugTextUI, (1800 - shifted_scroll[0], 950 - shifted_scroll[1]))

    # ---------------- Event loop
    # This is used to detect player inputs on the keyboard
    # This calls the functions mentioned earlier to decide what to do with each keyboard input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.KEYDOWN:
            moveU, moveR, moveL = detect_DOWN_events(p, event.key, moveU, moveR, moveL)
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            moveU, moveR, moveL = detect_UP_events(p, event.key, moveU, moveR, moveL)

    # ---------------- Blit level
    # These nested for loops take the rects, which represent blocks the player can stand on, from "levelData.tile_map1",
    # and draw them onto the screen. There are two here because one is for the shadow (that is purely aesthetic) and
    # the other is for the actual tiles that the player can collide with and stand on
    y = 0
    x = 0
    for row in LevelData.tile_map1:
        x = 0
        for tile in row:
            if tile == 3:
                pygame.draw.rect(screen2, Endesga.grey_blue, pygame.Rect(tile_size * x - shifted_scroll[0], tile_size * y - shifted_scroll[1], tile_size, tile_size))
            x += 1
        y += 1

    y = 0
    x = 0
    for row in LevelData.tile_map1:
        x = 0
        for tile in row:
            if tile == 3:
                pygame.draw.rect(screen2, Endesga.very_light_blue, (tile_size * x + (tile_size / 7) - shifted_scroll[0], tile_size * y - (tile_size / 7) - shifted_scroll[1], tile_size, tile_size))
            x += 1
        y += 1

    # Drawing the vines and mushrooms onto the screen by using a for loop to go through the "vines" and "bells" lists
    for vine in vines:
        screen2.blit(vineImg, (vine.x - shifted_scroll[0], vine.y - shifted_scroll[1]))
    for bell in bells:
        screen2.blit(shroomImg, (bell.x - shifted_scroll[0] + 4, bell.y - shifted_scroll[1] - 4))

    # ---------------- Bullets
    # Calling bullet methods for every bullet object. This also detects collisions between the player's hitbox, "p.rect", and
    # the bullet's hitbox "b"
    for b in bullets:
        # Moving each bullet
        Bullet.move(b)
        # Detecting collisions between the bullet and the player
        if math.fabs(b.x - p.rect.x - p.rect.width / 2) < p.rect.width:
            if math.fabs(b.y - p.rect.y - p.rect.height / 2) < p.rect.height:
                ShakeCounter = fps * 0.2
                p.hp -= b.dmg
                for i in range(10):
                    sparks.append(Spark(b.x, b.y, 9, Endesga.lighter_maroon_red, Endesga.maroon_red,
                                        random.randint(4, 6), random.uniform(0, math.pi * 2), 0.2, 0.4, 0, 0, 10))
                bullets.remove(b)
            else:
                if b.timer > 300:
                    bullets.remove(b)

    # If the shake counter is greater than zero the screen is shifted by a random amount in a random direction
    # and the shake counter is decremented
    if ShakeCounter > 0:
        shake = random.randint(-shake_strength, shake_strength), random.randint(-shake_strength, shake_strength)
        ShakeCounter -= 1

    # ---------------- Calling all the sparks methods needed for each spark object in the list "sparks"
    for s in sparks:
        Spark.move(s)
        Spark.blit(s)
        if s.size < 0:
            sparks.remove(s)

    # ---------------- Calling all the particle methods needed for each dust object in the list "dust"
    for d in dust:
        Particle.move(d, tile_rects)
        Particle.blit(d)
        if d.size < 0:
            dust.remove(d)

    # ---------------- Calling all the shockwave methods needed for each shockwave object in the list "shockwaves"
    for shock in shockwaves:
        Shockwave.expand(shock)
        Shockwave.blit(shock)
        if shock.width < 2:
            shockwaves.remove(shock)

    # ---------------- Drawing all the health boxes on the screen
    for hb in hpBoxes:
        screen2.blit(hpBoxImg, (hb.x - shifted_scroll[0] + 5, hb.y - shifted_scroll[1] + 3 * math.sin(oscillating_random_thing) - 3))

    # ---------------- Detecting collisions by calling all the collision functions
    Player.move(p)
    Player.collide(p, tile_rects)
    Player.collideV(p, vines)
    Player.collideB(p, bells)
    Player.collideH(p, hpBoxes, shockwaves)

    # ---------------- Using the collideB function's output to reset the "shockwave" variable's value
    if Player.collideB(p, bells) != 0:
        ShakeCounter = Player.collideB(p, bells)

    # ---------------- Detecting player collisions with the map's boundaries and setting the player's health to
    # zero if a collision is detected
    for b in bounds_rects:
        if b.colliderect(p.rect):
            p.hp = -1

    # ---------------- Calling all the spawner methods for each spawner object in the list "spawners"
    for spawner in spawners:
        Spawner.spawn(spawner)
        Spawner.draw(spawner)

    # ---------------- Resetting many of the player object's parameters if the health reaches zero
    if p.hp <= 0:
        ShakeCounter = fps * 0.5
        p.rect.x = 100
        p.rect.y = 50
        p.y_vel = -5
        p.jumps = 2
        p.apparentHealth = 1000
        p.hp = 1000

    # ---------------- Slightly incrementing the player's hp and also updating the (purely aesthetic) secondary health
    # bar that is drawn on top of the actual health bar
    p.apparentHealth -= (p.apparentHealth - p.hp) / 30
    if p.hp < 1000:
        p.hp += 0.05

    # ---------------- Drawing the player onto the screen
    pygame.draw.rect(screen2, ExplosiveColors.cream, pygame.rect.Rect(p.rect.x - shifted_scroll[0], p.rect.y - shifted_scroll[1], p.rect.width, p.rect.height), 0, 8)
    pygame.draw.rect(screen2, Endesga.black, pygame.rect.Rect(p.rect.x - shifted_scroll[0], p.rect.y - shifted_scroll[1], p.rect.width, p.rect.height), 1, 8)

    # ---------------- Arrows UI — using global variables to decide which image to blit onto the screen
    screen4.blit(lensImg, (0, 0))
    screen4.blit(arrowsImg, (75, 100))
    if moveR:
        screen4.blit(arrowsImgR, (75, 100))
    if moveL:
        screen4.blit(arrowsImgL, (75, 100))
    if moveU:
        screen4.blit(arrowsImgU, (75, 100))
    if moveL and moveR:
        screen4.blit(arrowsImgRL, (75, 100))
    if moveL and moveU:
        screen4.blit(arrowsImgLU, (75, 100))
    if moveR and moveU:
        screen4.blit(arrowsImgRU, (75, 100))
    if moveR and moveL and moveU:
        screen4.blit(arrowsImgRLU, (75, 100))

    # Drawing the player's health bars
    pygame.draw.rect(screen4, Endesga.lighter_maroon_red, pygame.rect.Rect(33, 40, p.apparentHealth / 3.6 + 4 * math.sin(oscillating_random_thing), 30), 0, 5)
    pygame.draw.rect(screen4, Endesga.maroon_red, pygame.rect.Rect(33, 40, p.hp / 3.6 + 4 * math.sin(oscillating_random_thing), 30), 0, 5)
    screen4.blit(healthbarImg, (20, 20))

    # ---------------- Calling all the scroll methods for each scroll in the "scrolls" list
    for scr in scrolls:
        Scroll.collide(scr, p)
        Scroll.draw(scr)

    # Blitting all the scroll images based on what the value of the global variable "scroll_counter" is
    if scroll_counter > 0:
        screen4.blit(scrollTextD, (900, 50))
    if scroll_counter == 1:
        screen4.blit(scrollText1, (870, 50))
    if scroll_counter == 2:
        screen4.blit(scrollText2, (870, 50))
    if scroll_counter == 3:
        screen4.blit(scrollText3, (870, 50))
    if scroll_counter == 4:
        screen4.blit(scrollText4, (870, 50))
    if scroll_counter == 5:
        screen4.blit(scrollText5, (870, 50))
    if scroll_counter == 6:
        screen4.blit(scrollText6, (870, 50))
    if scroll_counter == 7:
        screen4.blit(scrollText7, (870, 50))
    if scroll_counter == 8:
        screen4.blit(scrollText8, (870, 50))
    if scroll_counter == 9:
        screen4.blit(scrollText9, (870, 50))
    if scroll_counter == 10:
        screen4.blit(scrollText10, (860, 50))
    if scroll_counter == 11:
        screen4.blit(scrollText11, (860, 50))

    # ---------------- End frame — Drawing all the secondary screens onto the main screen, drawing the mouse of the
    # player (which isn't really used in this game), and updating the screen
    pygame.mouse.set_visible(False)
    pygame.draw.circle(screen3, ExplosiveColors.white, (mx, my), 5, 1)
    screen.blit(screen2, (shake[0], shake[1]))
    screen.blit(screen3, (0, 0))
    screen.blit(screen4, (0, 0))
    pygame.display.update()
    clock.tick(fps)
