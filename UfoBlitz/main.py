import pygame as pg
import os
import sys
import random
import pathlib

from Python.planet import PLANET
from Python.ufo import UFO
from Python.score import SCORE
from Python.target import TARGET
from Python.start import START
from Python.floatingtargets import FLOATINGTARGET
from Python.gameover import GAMEOVER

pg.init()
pg.mixer.init()

WIDTH = 900
HEIGHT = 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Orbit")

GRAY = (25,25,35)

FPS = 65

SPAWN_FLOATING = 0 # 5000 

DataFile = pathlib.Path("./Data/data.txt")
if DataFile.exists():
    try:
        with open("./Data/data.txt", "r") as f:
            highscore = int(f.read().strip())
    except:
        print("Cannot read data Error")
        highscore = 0
else:
    with open("./Data/data.txt", "w") as f:
        f.write("0")
    highscore = 0


clock = pg.time.Clock()

Target = TARGET()
FloatingTarget = FLOATINGTARGET()
GameOver = GAMEOVER(highscore)

bullet_list = [] 
target_list = [Target]
floating_target_list = []

Planet = PLANET()
Ufo = UFO()
Score = SCORE()
Start = START(highscore)


BG_MUSIC = pg.mixer.Sound("./Assets/Sounds/8BitMusic.mp3")
BG_MUSIC.set_volume(0.7)
BG_MUSIC.play(-1)

running = False
gameover = False

while not running:
    screen.fill(GRAY)
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            pg.quit()
            sys.exit()

    Start.draw(screen)

    keys = pg.key.get_pressed()
    if keys[pg.K_f]:  
        running = True
    pg.display.flip()
    clock.tick(FPS)

while running:

    SPAWN_FLOATING += 1
    if SPAWN_FLOATING >= 400:
        FloatingTarget = FLOATINGTARGET()
        floating_target_list.append(FloatingTarget)
        SPAWN_FLOATING = 0
    
    if Ufo.dir >= 635:
        del Ufo
        Ufo = UFO()
    
    screen.fill(GRAY)
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False

    for bullet in bullet_list:
        bullet.move()
        bullet.draw(Planet,Score,target_list)
        if bullet.remove:
            bullet_list.remove(bullet)
            del bullet
            break

    highscore = Score.draw(screen,WIDTH,highscore) 

    for target in target_list:
        if target.delete == True:
            target_list.remove(target)
            break
        target.run(screen)

    for floatingtarget in floating_target_list:
        if floatingtarget.delete == True:
            floating_target_list.remove(floatingtarget)
            break
        floatingtarget.run(screen)

    

    if len(target_list) < 3:
        if random.randint(1,55) == 1:
            Target = TARGET()
            target_list.append(Target)

    Planet.run(screen)

    bullet_list,gameover = Ufo.run(screen,bullet_list,floating_target_list,gameover)
    if gameover:
        running = False
    pg.display.flip()
    clock.tick(FPS)

with open("./Data/data.txt", "w") as f:
    f.write(str(highscore))


if gameover:
    while gameover:
        screen.fill(GRAY)
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                pg.quit()
                sys.exit()
        GameOver.draw(screen)
        pg.display.flip()
        clock.tick(FPS)

        keys = pg.key.get_pressed()
        if keys[pg.K_r]:
            print("Restarting Your highscore is saved")
            python = sys.executable  
            os.execl(python, python, *sys.argv) # Got this from the internet
        


pg.quit()
sys.exit()