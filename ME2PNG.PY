import sys
import re
import os

import PIL
from PIL import Image

john = 0

# Splitting the level into sections
if len(sys.argv) < 2:
    file_in = input('Path to Mario Editor Level JSON: ')
else:
    file_in = sys.argv[1]

with open(file_in, 'r') as file:
    content = file.read()

sect_split = re.split(r'(?="[^"]+": \{ "MUSIC": )',content)

for i, element in enumerate(sect_split):
    if i == 0:
        john = 1
    else:
        if os.path.exists(f'{i}.section'):
            os.remove(f'{i}.section')
        with open(f'{i}.section', 'w') as file_out:
            file_out.write(element)

print(f'{i} sections split.')

# Constants and defines

do_bg_image = 1
do_bg_tiles = 1
do_tiles = 1
do_obj = 1
do_warps = 1
do_mods = 1
do_textmods = 1
do_png = 1

def classic():
    global bg_image, height, width, x, y
    while y < (height - 10):
        while x <= width:
            bg_image += f'"{x}-{y}":[34,48],'
            x += 1
        x = 0
        y += 1
    if height <= 27:
        while (y <= height) and (y < 16):
            while x <= width:
                bg_image += f'"{x}-{y}":[34,48],'
                x += 1
            x = 0
            y += 1
        while (16 <= y <= 18) and y <= height:
            z = y - 9
            while x <= width:
                bg_image += f'"{x}-{y}":[51,{z}],"{x+1}-{y}":[52,{z}],'
                x += 2
            x = 0
            y += 1
        while y <= height:
            z = y - 19
            while x <= width:
                bg_image += f'"{x}-{y}":[{x % 32 + 51},{z}],'
                x += 1
            x = 0
            y += 1
    else:
        while (height - 10) <= y <= (height - 8):
            z = y - height + 17
            while x <= width:
                bg_image += f'"{x}-{y}":[51,{z}],"{x+1}-{y}":[52,{z}],'
                x += 2
            x = 0
            y += 1
        while y <= height:
            z = y - height + 7
            while x <= width:
                bg_image += f'"{x}-{y}":[{x % 32 + 51},{z}],'
                x += 1
            x = 0
            y += 1
    x = y = 0

def starry_night():
    global bg_image, height, width, x, y
    while y < (height - 14):
        z = y % 10 + 13
        while x <= width:
            bg_image += f'"{x}-{y}":[{x % 32 + 51},{z}],'
            x += 1
        x = 0
        y += 1
    while y < (height - 2):
        z = y - height + 37
        while x <= width:
            bg_image += f'"{x}-{y}":[{x % 32 + 51},{z}],'
            x += 1
        x = 0
        y += 1
    while y < height:
        while x <= width:
            bg_image += f'"{x}-{y}":[53,7],'
            x += 1
        x = 0
        y += 1
    x = y = 0

def blue_cave(posx,posy,lenx,leny):
    global bg_image, height, width, x, y
    while y < height:
        z = y % leny + posy
        while x < width:
            bg_image += f'"{x}-{y}":[{x % lenx + posx},{z}],'
            x += 1
        x = 0
        y += 1
    x = y = 0

def bloo_cave(posx,posy,lenx,leny,lim,offset):
    global bg_image, height, width, x, y
    while y < lim:
        z = (y - offset) % leny + posy
        while x < width:
            bg_image += f'"{x}-{y}":[{x % lenx + posx},{z}],'
            x += 1
        x = 0
        y += 1
    x = 0

def castle():
    global bg_image, height, width, x, y
    if height <= 27:
        while y < height:
            while x < width:
                bg_image += f'"{x}-{y}":[{x % 16 + 83},{y}],'
                x += 1
            x = 0
            y += 1
        x = y = 0
    else:
        while y < (height - 22):
            z = y % 5
            while x < width:
                bg_image += f'"{x}-{y}":[{x % 8 + 83},{z}],'
                x += 1
            x = 0
            y += 1
        z = 5
        while y < height:
            while x < width:
                bg_image += f'"{x}-{y}":[{x % 16 + 83},{z}],'
                x += 1
            x = 0
            y += 1
            z += 1
        x = y = 0

def desert():
    global bg_image, height, width, x, y
    if height <= 27:
        while y < height:
            while x < width:
                bg_image += f'"{x}-{y}":[{x % 32 + 83},{y + 27}],'
                x += 1
            x = 0
            y += 1
        x = y = 0
    else:
        while y < (height - 27):
            while x < width:
                bg_image += f'"{x}-{y}":[{83},{27}],'
                x += 1
            x = 0
            y += 1
        z = 27
        while y < height:
            while x < width:
                bg_image += f'"{x}-{y}":[{x % 32 + 83},{z}],'
                x += 1
            x = 0
            y += 1
            z += 1
        x = y = 0

def house():
    global bg_image, height, width, x, y
    while (y < height) and (y < 9):
        while x < width:
            bg_image += f'"{x}-{y}":[{x % 16 + 99},{y}],'
            x += 1
        x = 0
        y += 1
    while y < height:
        z = y % 2 + 11
        while x < width:
            bg_image += f'"{x}-{y}":[{x % 2 + 56},{z}],'
            x += 1
        x = 0
        y += 1
    x = y = 0

def fort():
    global bg_image, height, width, x, y
    if height <= 27:
        blue_cave(83,54,32,27)
    else:
        bloo_cave(83,54,32,26,26,0)
        bloo_cave(83,76,32,1,height - 1,0)
        blue_cave(83,80,32,1)
    y = 0

def storm():
    global bg_image, height, width, x, y
    while (y < height) and (y < 6):
        while x < width:
            bg_image += f'"{x}-{y}":[{45},{76}],'
            x += 1
        x = 0
        y += 1
    while y < (height - 9):
        while x < width:
            bg_image += f'"{x}-{y}":[{45},{76}],'
            x += 1
        x = 0
        y += 1
    bloo_cave(32,76,32,9,height,y)

def airship():
    global bg_image, height, width, x, y
    bloo_cave(99,9,16,8,min(height,8),0)
    bloo_cave(99,17,16,3,height,8)
    y = 0

def castle_garden():
    global y
    bloo_cave(33,48,1,1,max(height-8,min(17,height)),0)
    bloo_cave(83,124,32,8,height,y)
    y = 0

def cave_entrance():
    bloo_cave(83,81,32,20,min(height,20),0)
    blue_cave(53,8,1,1)

def forest():
    global y
    bloo_cave(83,101,32,9,max(height-14,min(9,height)),0)
    bloo_cave(83,110,32,14,height,y)
    y = 0

def hills():
    global y
    bloo_cave(32,85,1,1,max(height-14,min(11,height)),0)
    bloo_cave(32,85,32,14,height,y)
    y = 0

def mountain():
    global y
    bloo_cave(0,91,1,1,max(height-12,min(13,height)),0)
    bloo_cave(0,91,32,9,min(y+9,height),y)
    blue_cave(53,9,1,1)

def sky_hills():
    global y
    bloo_cave(0,100,1,1,max(height-10,min(14,height)),0)
    bloo_cave(0,100,32,10,height,y)
    y = 0

def snow():
    global y
    bloo_cave(53,10,1,1,max(height-12,min(13,height)),0)
    bloo_cave(70,7,1,4,min(y+4,height),y)
    bloo_cave(32,99,32,8,height,y)
    y = 0

def snow_hills():
    global y
    bloo_cave(0,110,1,1,max(height-10,min(14,height)),0)
    bloo_cave(0,110,32,10,height,y)
    y = 0

def underwater():
    global y
    bloo_cave(4,120,1,1,max(height-18,min(9,height)),0)
    bloo_cave(0,120,32,18,height,y)
    y = 0

def volcano():
    global y
    bloo_cave(35,121,1,1,max(height-12,min(14,height)),0)
    bloo_cave(32,121,32,12,height,y)
    y = 0

def waterfall():
    global y
    bloo_cave(32,107,1,1,max(height-14,min(10,height)),0)
    bloo_cave(32,107,32,14,height,y)
    y = 0

bgcmd = {
    'CLASSIC': lambda: classic(),
    'STARRY NIGHT': lambda: starry_night(),
    'CLOUDS': lambda: blue_cave(51,35,32,32),
    'CAVE': lambda: blue_cave(54,7,4,4),
    'BLUE CAVE': lambda: blue_cave(58,7,4,4),
    'CAVE ENTRANCE': lambda: cave_entrance(),
    'UNDERWATER': lambda: underwater(),
    'DESERT': lambda: desert(),
    'DESERT BRICKS': lambda: blue_cave(51,10,2,2),
    'SNOW': lambda: snow(),
    'CASTLE GARDEN': lambda: castle_garden(),
    'MOUNTAIN': lambda: mountain(),
    'HILLS': lambda: hills(),
    'SKY HILLS': lambda: sky_hills(),
    'SNOW HILLS': lambda: snow_hills(),
    'ICE': lambda: blue_cave(62,7,4,4),
    'METAL': lambda: blue_cave(54,11,2,2),
    'PIPES': lambda: blue_cave(35,48,16,27),
    'WATERFALL': lambda: waterfall(),
    'FOREST': lambda: forest(),
    'BONUS': lambda: blue_cave(66,7,4,4),
    'HOUSE': lambda: house(),
    'MINIGAME': lambda: blue_cave(51,67,18,9),
    'DUNGEON': lambda: blue_cave(0,49,32,12),
    'VOLCANO': lambda: volcano(),
    'CASTLE': lambda: castle(),
    'FORT': lambda: fort(),
    'GHOST': lambda: blue_cave(0,61,32,30),
    'AIRSHIP': lambda: airship(),
    'STORM': lambda: storm()
}

def afhb(ax,ay):
    global submods
    submods += f'"{ax+7}-{ay-0.625}":[47,32],"{ax+8}-{ay}":[50,32],"{ax+9}-{ay}":[50,32],"{ax+10}-{ay-0.625}":[50,35],"{ax+3}-{ay+3.375}":[47,32],"{ax+4}-{ay+4}":[50,32],"{ax+5}-{ay+4}":[50,32],"{ax+6}-{ay+3.375}":[50,35],'
    return f'"{ax}-{ay-2}":[48,32],"{ax}-{ay-1}":[48,33],"{ax}-{ay}":[48,34],"{ax+1}-{ay-2}":[49,32],"{ax+1}-{ay-1}":[49,33],"{ax+1}-{ay}":[49,34],"{ax-1}-{ay-0.625}":[50,34],"{ax+2}-{ay-0.625}":[50,33]'

def ball(ax,ay):
    return f'"{ax-0.5}-{ay-4}":[17,42],"{ax-0.5}-{ay-3}":[17,43],"{ax+0.5}-{ay-4}":[18,42],"{ax+0.5}-{ay-3}":[18,43],"{ax}-{ay-2}":[6,45],"{ax}-{ay-1}":[6,45]'

def block_train(ax,ay):
    return f'"{ax}-{ay}":[16,32],"{ax+1}-{ay}":[16,32],"{ax+2}-{ay}":[16,32],"{ax+3}-{ay}":[16,32],"{ax+4}-{ay}":[16,32],"{ax+5}-{ay}":[16,32],"{ax+6}-{ay}":[16,32],"{ax+7}-{ay}":[16,32]'

def boo_circle(ax,ay):
    return f'"{ax}-{ay}":[7,45],"{ax}-{ay-4.5}":[7,44],"{ax-2.25}-{ay-3.875}":[7,44],"{ax-3.875}-{ay-2.25}":[7,44],"{ax-4.5}-{ay}":[7,44],"{ax-3.875}-{ay+2.25}":[7,44],"{ax-2.25}-{ay+3.875}":[7,44],"{ax}-{ay+4.5}":[7,44],"{ax+2.25}-{ay+3.875}":[7,44],"{ax+3.875}-{ay+2.25}":[7,44],"{ax+4.5}-{ay}":[7,44]'

def bowser_npc(ax,ay):
    return f'"{ax-1}-{ay-1}":[15,36],"{ax}-{ay-1}":[16,36],"{ax-1}-{ay}":[15,37],"{ax}-{ay}":[16,37],"{ax+1}-{ay}":[17,37],"{ax-1}-{ay+1}":[15,38],"{ax}-{ay+1}":[16,38],"{ax+1}-{ay+1}":[17,38]'

def checkpoint(ax,ay):
    return f'"{ax}-{ay}":[5,32],"{ax}-{ay+1}":[5,33],"{ax+1}-{ay+1}":[6,33],"{ax}-{ay+2}":[5,34]'

def endcastle(ax,ay):
    return f'"{ax+0}-{ay}":[3,38],"{ax+1}-{ay}":[4,38],"{ax+2}-{ay}":[5,38],"{ax-1}-{ay}":[2,38],"{ax-2}-{ay}":[1,38],"{ax-3}-{ay}":[0,38],"{ax+0}-{ay-1}":[3,37],"{ax+1}-{ay-1}":[4,37],"{ax+2}-{ay-1}":[5,37],"{ax-1}-{ay-1}":[2,37],"{ax-2}-{ay-1}":[1,37],"{ax-3}-{ay-1}":[0,37],"{ax+0}-{ay-2}":[3,36],"{ax+1}-{ay-2}":[4,36],"{ax+2}-{ay-2}":[5,36],"{ax-1}-{ay-2}":[2,36],"{ax-2}-{ay-2}":[1,36],"{ax-3}-{ay-2}":[0,36],"{ax+0}-{ay-3}":[3,35],"{ax+1}-{ay-3}":[4,35],"{ax-1}-{ay-3}":[2,35],"{ax-2}-{ay-3}":[1,35],"{ax+0}-{ay-4}":[3,34],"{ax+1}-{ay-4}":[4,34],"{ax-1}-{ay-4}":[2,34],"{ax-2}-{ay-4}":[1,34]'

def flagpole(ax,ay):
    return f'"{ax}-{ay}":[5,32],"{ax}-{ay+1}":[7,33],"{ax+1}-{ay+1}":[8,33],"{ax}-{ay+2}":[7,34],"{ax}-{ay+3}":[8,32],"{ax}-{ay+4}":[8,32],"{ax}-{ay+5}":[8,32],"{ax}-{ay+6}":[8,32],"{ax}-{ay+7}":[8,32],"{ax}-{ay+8}":[8,32],"{ax}-{ay+9}":[8,34]'

def fourtall(ax,ay,bx,by):
    return f'"{ax}-{ay}":[{bx},{by}],"{ax}-{ay+1}":[{bx},{by+1}],"{ax}-{ay+2}":[{bx},{by+2}],"{ax}-{ay+3}":[{bx},{by+3}]'

def fourwide(ax,ay,bx,by):
    return f'"{ax}-{ay}":[{bx},{by}],"{ax+1}-{ay}":[{bx+1},{by}],"{ax+2}-{ay}":[{bx+2},{by}],"{ax+3}-{ay}":[{bx+3},{by}]'

def firebar(ax,ay):
    return f'"{ax}-{ay}":[17,47],"{ax}-{ay-1}":[17,46],"{ax}-{ay-2}":[17,46],"{ax}-{ay-3}":[17,45]'

def firebar_large(ax,ay):
    return f'"{ax}-{ay}":[17,47],"{ax}-{ay-1}":[17,46],"{ax}-{ay-2}":[17,46],"{ax}-{ay-3}":[17,46],"{ax}-{ay-4}":[17,46],"{ax}-{ay-5}":[17,45]'

def htile_two(ax,ay,x1,y1,x2,y2):
    return f'"{ax}-{ay}":[{x1},{y1}],"{ax+1}-{ay}":[{x2},{y2}]'

def htile_three(ax,ay,x1,y1,x2,y2,x3,y3):
    return f'"{ax}-{ay}":[{x1},{y1}],"{ax+1}-{ay}":[{x2},{y2}],"{ax+2}-{ay}":[{x3},{y3}]'

def large_turnip(ax,ay):
    global submods
    submods += f'"{ax-1}-{ay+1}":[17,32],"{ax}-{ay+1}":[18,32],"{ax+1}-{ay+1}":[19,32],"{ax-1}-{ay+2}":[17,33],"{ax}-{ay+2}":[18,33],"{ax+1}-{ay+2}":[19,33],'
    return f'"{ax}-{ay}":[17,35]'

def lemmy(ax,ay,bx,by):
    return f'"{ax}-{ay}":[{bx},{by}],"{ax}-{ay+1}":[{bx},{by+1}],"{ax+1}-{ay}":[{bx+1},{by}],"{ax+1}-{ay+1}":[{bx+1},{by+1}],"{ax}-{ay+2}":[{bx},{by+2}],"{ax+1}-{ay+2}":[{bx+1},{by+2}]'

def o_piece(ax,ay,bx,by):
    return f'"{ax}-{ay}":[{bx},{by}],"{ax}-{ay+1}":[{bx},{by+1}],"{ax+1}-{ay}":[{bx+1},{by}],"{ax+1}-{ay+1}":[{bx+1},{by+1}]'

def platform_h(ax,ay):
    return f'"{ax-2}-{ay}":[15,32],"{ax-1}-{ay}":[15,32],"{ax}-{ay}":[14,32],"{ax+1}-{ay}":[15,32],"{ax+2}-{ay}":[15,32]'

def platform_v(ax,ay):
    return f'"{ax}-{ay-2}":[15,32],"{ax}-{ay-1}":[15,32],"{ax}-{ay}":[14,32],"{ax}-{ay+1}":[15,32],"{ax}-{ay+2}":[15,32]'

def platform_hv(ax,ay):
    return f'"{ax-2}-{ay}":[15,32],"{ax-1}-{ay}":[15,32],"{ax}-{ay}":[14,32],"{ax+1}-{ay}":[15,32],"{ax+2}-{ay}":[15,32],"{ax}-{ay-2}":[15,32],"{ax}-{ay-1}":[15,32],"{ax}-{ay+1}":[15,32],"{ax}-{ay+2}":[15,32]'

def rect_three_two(ax,ay,bx,by):
    return f'"{ax}-{ay}":[{bx},{by}],"{ax}-{ay+1}":[{bx},{by+1}],"{ax+1}-{ay}":[{bx+1},{by}],"{ax+1}-{ay+1}":[{bx+1},{by+1}],"{ax+2}-{ay}":[{bx+2},{by}],"{ax+2}-{ay+1}":[{bx+2},{by+1}]'

def regular(ax,ay,bx,by):
    return f'"{ax}-{ay}":[{bx},{by}]'

def reznor(ax,ay):
    return f'"{ax-1}-{ay-5}":[35,46],"{ax}-{ay-5}":[36,46],"{ax-1}-{ay-4}":[35,47],"{ax}-{ay-4}":[36,47],"{ax-3}-{ay-3}":[29,42],"{ax-2}-{ay-3}":[30,42],"{ax-1}-{ay-3}":[31,42],"{ax}-{ay-3}":[32,42],"{ax+1}-{ay-3}":[33,42],"{ax+2}-{ay-3}":[34,42],"{ax-4}-{ay-2}":[35,46],"{ax-3}-{ay-2}":[29,43],"{ax-2}-{ay-2}":[30,43],"{ax-1}-{ay-2}":[31,43],"{ax}-{ay-2}":[32,43],"{ax+1}-{ay-2}":[33,43],"{ax+2}-{ay-2}":[34,43],"{ax+3}-{ay-2}":[36,46],"{ax-4}-{ay-1}":[35,47],"{ax-3}-{ay-1}":[29,44],"{ax-2}-{ay-1}":[30,44],"{ax-1}-{ay-1}":[31,44],"{ax}-{ay-1}":[32,44],"{ax+1}-{ay-1}":[33,44],"{ax+2}-{ay-1}":[34,44],"{ax+3}-{ay-1}":[36,47],"{ax-4}-{ay  }":[31,42],"{ax-3}-{ay  }":[32,42],"{ax-2}-{ay  }":[30,45],"{ax-1}-{ay  }":[31,45],"{ax}-{ay  }":[32,45],"{ax+1}-{ay  }":[33,45],"{ax+2}-{ay  }":[31,42],"{ax+3}-{ay  }":[32,42],"{ax-3}-{ay+1}":[29,46],"{ax-2}-{ay+1}":[30,46],"{ax-1}-{ay+1}":[31,46],"{ax}-{ay+1}":[32,46],"{ax+1}-{ay+1}":[33,46],"{ax+2}-{ay+1}":[34,46],"{ax-3}-{ay+2}":[29,47],"{ax-2}-{ay+2}":[30,47],"{ax-1}-{ay+2}":[31,47],"{ax}-{ay+2}":[32,47],"{ax+1}-{ay+2}":[33,47],"{ax+2}-{ay+2}":[34,47],"{ax-1}-{ay+3}":[31,42],"{ax}-{ay+3}":[32,42]'

def rope(ax,ay,bx):
    return f'"{ax}-{ay}":[{bx},32],"{ax}-{ay+1}":[12,33]'

def spinning(ax,ay):
    return f'"{ax-1}-{ay}":[12,34],"{ax}-{ay}":[14,34],"{ax+1}-{ay}":[13,34],"{ax+2}-{ay}":[14,34],"{ax+3}-{ay}":[15,34]'

def spike(ax,ay):
    return f'"{ax-1}-{ay-24}":[41,44],"{ax}-{ay-24}":[42,44],"{ax-1.5}-{ay-23}":[40,46],"{ax-0.5}-{ay-23}":[41,46],"{ax+0.5}-{ay-23}":[42,46],"{ax-1.5}-{ay-22}":[40,45],"{ax-0.5}-{ay-22}":[41,46],"{ax+0.5}-{ay-22}":[42,45],"{ax-1.5}-{ay-21}":[40,46],"{ax-0.5}-{ay-21}":[41,46],"{ax+0.5}-{ay-21}":[42,46],"{ax-1.5}-{ay-20}":[40,45],"{ax-0.5}-{ay-20}":[41,46],"{ax+0.5}-{ay-20}":[42,45],"{ax-1.5}-{ay-19}":[40,46],"{ax-0.5}-{ay-19}":[41,46],"{ax+0.5}-{ay-19}":[42,46],"{ax-1.5}-{ay-18}":[40,45],"{ax-0.5}-{ay-18}":[41,46],"{ax+0.5}-{ay-18}":[42,45],"{ax-1.5}-{ay-17}":[40,46],"{ax-0.5}-{ay-17}":[41,46],"{ax+0.5}-{ay-17}":[42,46],"{ax-1.5}-{ay-16}":[40,45],"{ax-0.5}-{ay-16}":[41,46],"{ax+0.5}-{ay-16}":[42,45],"{ax-1.5}-{ay-15}":[40,46],"{ax-0.5}-{ay-15}":[41,46],"{ax+0.5}-{ay-15}":[42,46],"{ax-1.5}-{ay-14}":[40,45],"{ax-0.5}-{ay-14}":[41,46],"{ax+0.5}-{ay-14}":[42,45],"{ax-1.5}-{ay-13}":[40,46],"{ax-0.5}-{ay-13}":[41,46],"{ax+0.5}-{ay-13}":[42,46],"{ax-1.5}-{ay-12}":[40,45],"{ax-0.5}-{ay-12}":[41,46],"{ax+0.5}-{ay-12}":[42,45],"{ax-1.5}-{ay-11}":[40,46],"{ax-0.5}-{ay-11}":[41,46],"{ax+0.5}-{ay-11}":[42,46],"{ax-1.5}-{ay-10}":[40,45],"{ax-0.5}-{ay-10}":[41,46],"{ax+0.5}-{ay-10}":[42,45],"{ax-1.5}-{ay-9}":[40,46],"{ax-0.5}-{ay-9}":[41,46],"{ax+0.5}-{ay-9}":[42,46],"{ax-1.5}-{ay-8}":[40,45],"{ax-0.5}-{ay-8}":[41,46],"{ax+0.5}-{ay-8}":[42,45],"{ax-1.5}-{ay-7}":[40,46],"{ax-0.5}-{ay-7}":[41,46],"{ax+0.5}-{ay-7}":[42,46],"{ax-1.5}-{ay-6}":[40,45],"{ax-0.5}-{ay-6}":[41,46],"{ax+0.5}-{ay-6}":[42,45],"{ax-1.5}-{ay-5}":[40,46],"{ax-0.5}-{ay-5}":[41,46],"{ax+0.5}-{ay-5}":[42,46],"{ax-1.5}-{ay-4}":[40,45],"{ax-0.5}-{ay-4}":[41,46],"{ax+0.5}-{ay-4}":[42,45],"{ax-1.5}-{ay-3}":[40,46],"{ax-0.5}-{ay-3}":[41,46],"{ax+0.5}-{ay-3}":[42,46],"{ax-1.5}-{ay-2}":[40,45],"{ax-0.5}-{ay-2}":[41,46],"{ax+0.5}-{ay-2}":[42,45],"{ax-1.5}-{ay-1}":[40,46],"{ax-0.5}-{ay-1}":[41,46],"{ax+0.5}-{ay-1}":[42,46],"{ax-1}-{ay}":[41,47],"{ax}-{ay}":[42,47]'

def sq_four(ax,ay,bx,by):
    return f'"{ax}-{ay}":[{bx},{by}],"{ax+1}-{ay}":[{bx+1},{by}],"{ax+2}-{ay}":[{bx+2},{by}],"{ax+3}-{ay}":[{bx+3},{by}],"{ax}-{ay+1}":[{bx},{by+1}],"{ax+1}-{ay+1}":[{bx+1},{by+1}],"{ax+2}-{ay+1}":[{bx+2},{by+1}],"{ax+3}-{ay+1}":[{bx+3},{by+1}],"{ax}-{ay+2}":[{bx},{by+2}],"{ax+1}-{ay+2}":[{bx+1},{by+2}],"{ax+2}-{ay+2}":[{bx+2},{by+2}],"{ax+3}-{ay+2}":[{bx+3},{by+2}],"{ax}-{ay+3}":[{bx},{by+3}],"{ax+1}-{ay+3}":[{bx+1},{by+3}],"{ax+2}-{ay+3}":[{bx+2},{by+3}],"{ax+3}-{ay+3}":[{bx+3},{by+3}]'

def tall(ax,ay,bx,by):
    return f'"{ax}-{ay}":[{bx},{by}],"{ax}-{ay+1}":[{bx},{by+1}]'

def toad_house(ax,ay,bx,by):
    return f'"{ax-2}-{ay-1}":[{bx+1},{by}],"{ax-1}-{ay-1}":[{bx+2},{by}],"{ax}-{ay-1}":[{bx+3},{by}],"{ax+1}-{ay-1}":[{bx+4},{by}],"{ax+2}-{ay-1}":[{bx+5},{by}],"{ax-3}-{ay}":[{bx},{by+1}],"{ax-2}-{ay}":[{bx+1},{by+1}],"{ax-1}-{ay}":[{bx+2},{by+1}],"{ax}-{ay}":[{bx+3},{by+1}],"{ax+1}-{ay}":[{bx+4},{by+1}],"{ax+2}-{ay}":[{bx+5},{by+1}],"{ax+3}-{ay}":[{bx+6},{by+1}],"{ax-3}-{ay+1}":[{bx},{by+2}],"{ax-2}-{ay+1}":[{bx+1},{by+2}],"{ax-1}-{ay+1}":[{bx+2},{by+2}],"{ax}-{ay+1}":[{bx+3},{by+2}],"{ax+1}-{ay+1}":[{bx+4},{by+2}],"{ax+2}-{ay+1}":[{bx+5},{by+2}],"{ax+3}-{ay+1}":[{bx+6},{by+2}],"{ax-3}-{ay+2}":[{bx},{by+3}],"{ax-2}-{ay+2}":[{bx+1},{by+3}],"{ax-1}-{ay+2}":[{bx+2},{by+3}],"{ax}-{ay+2}":[{bx+3},{by+3}],"{ax+1}-{ay+2}":[{bx+4},{by+3}],"{ax+2}-{ay+2}":[{bx+5},{by+3}],"{ax+3}-{ay+2}":[{bx+6},{by+3}],"{ax-3}-{ay+3}":[{bx},{by+4}],"{ax-2}-{ay+3}":[{bx+1},{by+4}],"{ax-1}-{ay+3}":[{bx+2},{by+4}],"{ax}-{ay+3}":[{bx+3},{by+4}],"{ax+1}-{ay+3}":[{bx+4},{by+4}],"{ax+2}-{ay+3}":[{bx+5},{by+4}],"{ax+3}-{ay+3}":[{bx+6},{by+4}],"{ax-2}-{ay+4}":[45,40],"{ax-1}-{ay+4}":[46,40],"{ax}-{ay+4}":[47,40],"{ax+1}-{ay+4}":[48,40],"{ax+2}-{ay+4}":[49,40],"{ax-2}-{ay+5}":[45,41],"{ax-1}-{ay+5}":[46,41],"{ax}-{ay+5}":[47,41],"{ax+1}-{ay+5}":[48,41],"{ax+2}-{ay+5}":[49,41]'

def toadette(ax,ay,bx,by):
    return f'"{ax}-{ay}":[{bx},{by}],"{ax}-{ay+1}":[{bx},{by+1}],"{ax+1}-{ay+1}":[{bx+1},{by+1}]'

def vtile_two(ax,ay,x1,y1,x2,y2):
    return f'"{ax}-{ay}":[{x1},{y1}],"{ax}-{ay+1}":[{x2},{y2}]'

def vtile_three(ax,ay,x1,y1,x2,y2,x3,y3):
    return f'"{ax}-{ay}":[{x1},{y1}],"{ax}-{ay+1}":[{x2},{y2}],"{ax}-{ay+2}":[{x3},{y3}]'

def weed(ax,ay,bx,by):
    global submods
    submods += f'"{ax}-{ay+1}":[{bx},{by}],'
    return f'"{ax}-{ay}":[17,35]'

def wide(ax,ay,bx,by):
    return f'"{ax}-{ay}":[{bx},{by}],"{ax+1}-{ay}":[{bx+1},{by}]'

def unknown(ax,ay):
    return f'"{ax}-{ay}":[6,34]'

objcmd = {
    'MARIO': lambda ax, ay: tall(ax,ay,0,32),
    'WARP MARIO': lambda ax, ay: o_piece(ax,ay,1,32),
    'JUMP MARIO': lambda ax, ay: tall(ax,ay,3,32),
    'VINE MARIO': lambda ax, ay: tall(ax,ay,4,32),
    'CHECKPOINT': lambda ax, ay: checkpoint(ax,ay),
    'AUTOSCROLLER': lambda ax, ay: regular(ax,ay,6,32),
    'FLAGPOLE': lambda ax, ay: flagpole(ax,ay),
    'END CASTLE': lambda ax, ay: endcastle(ax,ay),
    'COIN': lambda ax, ay: regular(ax,ay,0,34),
    'P-COIN': lambda ax, ay: regular(ax,ay,0,35),
    'BUBBLE COIN': lambda ax, ay: o_piece(ax,ay,6,35),
    'BUBBLE ITEM': lambda ax, ay: o_piece(ax,ay,6,37),
    'ICE COIN': lambda ax, ay: regular(ax,ay,8,35),
    'ICE MUNCHER': lambda ax, ay: regular(ax,ay,8,36),
    'SPRING': lambda ax, ay: regular(ax,ay,0,41),
    'HIDDEN SPRING': lambda ax, ay: regular(ax,ay,1,41),
    'TIMED SPRING': lambda ax, ay: regular(ax,ay,2,41),
    'SUPER SPRING': lambda ax, ay: regular(ax,ay,3,41),
    'PROPELLER BLOCK': lambda ax, ay: tall(ax,ay-1,8,37),
    '3UP MOON': lambda ax, ay: regular(ax,ay,5,35),
    'KEY': lambda ax, ay: regular(ax,ay,7,32),
    'P-SWITCH': lambda ax, ay: regular(ax,ay,6,39),
    'E-SWITCH': lambda ax, ay: regular(ax,ay,7,39),
    'RED E-SWITCH': lambda ax, ay: regular(ax,ay,8,39),
    'FALLING SPIKE': lambda ax, ay: regular(ax,ay,6,40),
    'P-PLATFORM': lambda ax, ay: regular(ax,ay,7,40),
    'QUICKSAND': lambda ax, ay: regular(ax,ay,8,40),
    'TOP BLOWPIPE': lambda ax, ay: wide(ax,ay,0,40),
    'BOTTOM BLOWPIPE': lambda ax, ay: wide(ax,ay,0,39),
    'LEFT BLOWPIPE': lambda ax, ay: tall(ax,ay,2,39),
    'RIGHT BLOWPIPE': lambda ax, ay: tall(ax,ay,3,39),
    'RIGHT WALL TRIANGLE': lambda ax, ay: regular(ax,ay,4,39),
    'INVERTED RIGHT WALL TRIANGLE': lambda ax, ay: regular(ax,ay,4,40),
    'LEFT WALL TRIANGLE': lambda ax, ay: regular(ax,ay,5,39),
    'INVERTED LEFT WALL TRIANGLE': lambda ax, ay: regular(ax,ay,5,40),
    'TOP FLIPPERS': lambda ax, ay: fourwide(ax,ay,8,41),
    'BOTTOM FLIPPERS': lambda ax, ay: fourwide(ax,ay,4,41),
    'LEFT FLIPPERS': lambda ax, ay: fourtall(ax,ay,9,37),
    'RIGHT FLIPPERS': lambda ax, ay: fourtall(ax,ay,10,37),
    'FALLING SPIKE': lambda ax, ay: regular(ax,ay,6,40),
    'MOVING PLATFORM': lambda ax, ay: htile_three(ax,ay,9,36,9,33,9,32),
    'TOUCH-START MOVING PLATFORM': lambda ax, ay: htile_three(ax,ay,9,36,9,34,9,32),
    'FALLING PLATFORM': lambda ax, ay: htile_three(ax,ay,9,36,9,35,9,32),
    'DONUT': lambda ax, ay: regular(ax,ay,10,32),
    'RED DONUT': lambda ax, ay: regular(ax,ay,11,32),
    'SPINNING PLATFORM': lambda ax, ay: spinning(ax,ay),
    'TIMED PLATFORM': lambda ax, ay: wide(ax,ay,10,34),
    'ARROW PLATFORM': lambda ax, ay: wide(ax,ay,10,35),
    'MOVING PIPE': lambda ax, ay: wide(ax,ay,10,36),
    'PARABEETLE': lambda ax, ay: regular(ax,ay,13,33),
    'BLOCK TRAIN': lambda ax, ay: block_train(ax,ay),
    'BOUNCER': lambda ax, ay: htile_three(ax-2,ay,14,33,15,33,15,33),
    'H EXPAND PLATFORM': lambda ax, ay: platform_h(ax,ay),
    'V EXPAND PLATFORM': lambda ax, ay: platform_v(ax,ay),
    'HV EXPAND PLATFORM': lambda ax, ay: platform_hv(ax,ay),
    'LEFT CONVEYOR BELT': lambda ax, ay: regular(ax,ay,10,33),
    'RIGHT CONVEYOR BELT': lambda ax, ay: regular(ax,ay,11,33),
    'MOVING ROPE': lambda ax, ay: rope(ax,ay,12),
    'TOUCH-START MOVING ROPE': lambda ax, ay: rope(ax,ay,13),
    'MOVING SAW': lambda ax, ay: vtile_three(ax,ay-2,11,37,11,38,11,39),
    'SKULL RAFT': lambda ax, ay: regular(ax,ay,11,40),
    'SMALL TURNIP': lambda ax, ay: weed(ax,ay,16,34),
    'LARGE TURNIP': lambda ax, ay: large_turnip(ax,ay),
    'COIN TURNIP': lambda ax, ay: weed(ax,ay,17,34),
    'MULTI-COIN TURNIP': lambda ax, ay: weed(ax,ay,18,34),
    'SHROOM TURNIP': lambda ax, ay: weed(ax,ay,19,34),
    '1UP TURNIP': lambda ax, ay: weed(ax,ay,13,35),
    'POISON TURNIP': lambda ax, ay: weed(ax,ay,12,35),
    'STAR TURNIP': lambda ax, ay: weed(ax,ay,16,35),
    'BOMB TURNIP': lambda ax, ay: weed(ax,ay,14,35),
    'SHELL TUTNIP': lambda ax, ay: weed(ax,ay,15,35), # TUTNIP
    'POW BLOCK': lambda ax, ay: regular(ax,ay,20,34),
    'STACKABLE BLOCK': lambda ax, ay: regular(ax,ay,20,33),
    'SHROOM BLOCK': lambda ax, ay: regular(ax,ay,20,32),
    'DIG SAND': lambda ax, ay: regular(ax,ay,20,35),
    'WATER TOP': lambda ax, ay: regular(ax,ay,12,36),
    'WATER TOP 2': lambda ax, ay: regular(ax,ay,13,36),
    'WATERFALL': lambda ax, ay: regular(ax,ay,14,36),
    'VINE': lambda ax, ay: regular(ax,ay,18,35),
    'MUNCHER': lambda ax, ay: regular(ax,ay,12,41),
    'MUNCHER 2': lambda ax, ay: regular(ax,ay,18,41),
    'JELECTRO': lambda ax, ay: regular(ax,ay,19,35),
    'LAVA': lambda ax, ay: regular(ax,ay,15,41),
    'LAVA RIGHT SLOPE': lambda ax, ay: o_piece(ax,ay,16,40),
    'LAVA LEFT SLOPE': lambda ax, ay: o_piece(ax,ay,13,40),
    'LAVA RIGHT STEEP SLOPE': lambda ax, ay: tall(ax,ay,18,39),
    'LAVA LEFT STEEP SLOPE': lambda ax, ay: tall(ax,ay,12,39),
    'TOAD HOUSE': lambda ax, ay: toad_house(ax,ay-4,30,37),
    'TOAD HOUSE 2': lambda ax, ay: toad_house(ax,ay-4,37,37),
    'TOAD HOUSE 3': lambda ax, ay: toad_house(ax,ay-4,44,35),
    'LUIGI NPC': lambda ax, ay: tall(ax,ay,21,32),
    'WARIO NPC': lambda ax, ay: tall(ax,ay,22,32),
    'WALUIGI NPC': lambda ax, ay: tall(ax,ay,23,32),
    'PEACH NPC': lambda ax, ay: o_piece(ax,ay,24,32),
    'DAISY NPC': lambda ax, ay: tall(ax,ay,26,32),
    'ROSALINA NPC': lambda ax, ay: tall(ax,ay,27,32),
    'PEACHETTE NPC': lambda ax, ay: tall(ax,ay,28,32),
    'BOWSETTE NPC': lambda ax, ay: o_piece(ax,ay,29,32),
    'RED TOAD NPC': lambda ax, ay: tall(ax,ay,21,34),
    'BLUE TOAD NPC': lambda ax, ay: tall(ax,ay,22,34),
    'YELLOW TOAD NPC': lambda ax, ay: tall(ax,ay,23,34),
    'GREEN TOAD NPC': lambda ax, ay: tall(ax,ay,24,34),
    'PINK TOADETTE NPC': lambda ax, ay: toadette(ax,ay,25,34),
    'PURPLE TOADETTE NPC': lambda ax, ay: toadette(ax,ay,27,34),
    'CYAN TOADETTE NPC': lambda ax, ay: toadette(ax,ay,29,34),
    'ORANGE TOADETTE NPC': lambda ax, ay: toadette(ax,ay,31,34),
    'TOADSWORTH NPC': lambda ax, ay: toadette(ax,ay,31,32),
    'BOWSER NPC': lambda ax, ay: bowser_npc(ax,ay),
    'NONE NPC': lambda ax, ay: tall(ax,ay-1,12,37),
    'QUESTION BLOCK': lambda ax, ay: regular(ax,ay,32,32),
    'MULTICOIN BLOCK': lambda ax, ay: regular(ax,ay,26,34),
    'MULTICOIN SHROOM BLOCK': lambda ax, ay: regular(ax,ay,28,34),
    'COIN CHAIN BLOCK': lambda ax, ay: regular(ax,ay,30,34),
    'HIDDEN BLOCK': lambda ax, ay: regular(ax,ay,32,34),
    'TRIPLE BLOCK': lambda ax, ay: htile_three(ax,ay,14,39,15,39,16,39),
    'TRIPLE HIDDEN BLOCK': lambda ax, ay: htile_three(ax,ay,17,36,18,36,19,36),
    'LARGE BLOCK': lambda ax, ay: o_piece(ax,ay,13,37),
    'SPIKED BLOCK': lambda ax, ay: tall(ax,ay-1,33,32),
    'WINGED BLOCK': lambda ax, ay: rect_three_two(ax-1,ay-1,18,37),
    'BUMP BLOCK': lambda ax, ay: regular(ax,ay,20,36),
    'BRICK': lambda ax, ay: regular(ax,ay,21,36),
    'BLUE BRICK': lambda ax, ay: regular(ax,ay,22,36),
    'RED BRICK': lambda ax, ay: regular(ax,ay,23,36),
    'GREEN BRICK': lambda ax, ay: regular(ax,ay,24,36),
    'BOMB BRICK': lambda ax, ay: regular(ax,ay,25,36),
    'FLIP BLOCK': lambda ax, ay: regular(ax,ay,14,32),
    'NOTE BLOCK': lambda ax, ay: regular(ax,ay,21,37),
    'HIDDEN NOTE BLOCK': lambda ax, ay: regular(ax,ay,22,37),
    'YELLOW NOTE BLOCK': lambda ax, ay: regular(ax,ay,23,37),
    'HIDDEN YELLOW NOTE BLOCK': lambda ax, ay: regular(ax,ay,24,37),
    'WARP NOTE BLOCK': lambda ax, ay: regular(ax,ay,25,37),
    'HIDDEN WARP NOTE BLOCK': lambda ax, ay: regular(ax,ay,26,37),
    'MESSAGE BLOCK': lambda ax, ay: regular(ax,ay,21,38),
    'BLUE POW BLOCK': lambda ax, ay: regular(ax,ay,22,38),
    'ROULETTE BLOCK': lambda ax, ay: regular(ax,ay,23,38),
    'ON OFF BLOCK': lambda ax, ay: regular(ax,ay,24,38),
    'ON OFF PLATFORM': lambda ax, ay: regular(ax,ay,25,38),
    'GRAY FLOWER BLOCK': lambda ax, ay: regular(ax,ay,26,38),
    'GRAY HAMMER BLOCK': lambda ax, ay: regular(ax,ay,26,36),
    'GRAY BOOMERANG BLOCK': lambda ax, ay: regular(ax,ay,19,39),
    'GRAY LEAF BLOCK': lambda ax, ay: regular(ax,ay,20,39),
    'GRAY STAR BLOCK': lambda ax, ay: regular(ax,ay,21,39),
    'GRAY BOMB BLOCK': lambda ax, ay: regular(ax,ay,22,39),
    'GRAY SHELL BLOCK': lambda ax, ay: regular(ax,ay,23,39),
    'GRAY SWITCH BLOCK': lambda ax, ay: regular(ax,ay,24,39),
    'GRAY SHOE BLOCK': lambda ax, ay: regular(ax,ay,25,39),
    'GRAY FEMALE BLOCK': lambda ax, ay: regular(ax,ay,26,39),
    'GOOMBA': lambda ax, ay: regular(ax,ay,32,36),
    'PARAGOOMBA': lambda ax, ay: regular(ax,ay,31,36),
    'BUBBLE GOOMBA': lambda ax, ay: o_piece(ax,ay,29,36),
    'SHOE GOOMBA': lambda ax, ay: regular(ax,ay,33,36),
    'BRICK GOOMBA': lambda ax, ay: regular(ax,ay,34,36),
    'GALOOMBA': lambda ax, ay: regular(ax,ay,35,36),
    'PARACHUTE GALOOMBA': lambda ax, ay: tall(ax,ay-1,29,38),
    'KOOPA': lambda ax, ay: tall(ax,ay-1,34,32),
    'RED KOOPA': lambda ax, ay: tall(ax,ay-1,35,32),
    'HYPER KOOPA': lambda ax, ay: tall(ax,ay-1,36,32),
    'PARAKOOPA': lambda ax, ay: tall(ax,ay-1,37,32),
    'RED PARAKOOPA': lambda ax, ay: tall(ax,ay-1,38,32),
    'HYPER PARAKOOPA': lambda ax, ay: tall(ax,ay-1,39,32),
    'JUMPING KOOPA': lambda ax, ay: tall(ax,ay-1,40,32),
    'REX': lambda ax, ay: tall(ax,ay,29,40),
    'SPIKE': lambda ax, ay: regular(ax,ay,34,34),
    'PURPLE HOOPSTER': lambda ax, ay: regular(ax,ay,35,34),
    'RED NINJI': lambda ax, ay: regular(ax,ay,36,34),
    'WIGGLER': lambda ax, ay: tall(ax,ay-1,33,34),
    'CHEEP CHEEP': lambda ax, ay: regular(ax,ay,37,34),
    'GREEN CHEEP CHEEP': lambda ax, ay: regular(ax,ay,38,34),
    'SPIKED CHEEP CHEEP': lambda ax, ay: regular(ax,ay,39,34),
    'URCHIN': lambda ax, ay: o_piece(ax,ay,19,40),
    'TORPEDO TED': lambda ax, ay: o_piece(ax,ay,21,40),
    'RIP VAN FISH': lambda ax, ay: regular(ax,ay,40,34),
    'PORCU PUFFER': lambda ax, ay: o_piece(ax-1,ay,23,40),
    'LAVA LOTUS': lambda ax, ay: o_piece(ax,ay,25,40),
    'FISHBONE': lambda ax, ay: wide(ax-.5,ay,34,35),
    'BLOOPER': lambda ax, ay: regular(ax,ay,44,41),
    'NIPPER': lambda ax, ay: regular(ax,ay,44,40),
    'MONTY MOLE': lambda ax, ay: regular(ax,ay,36,36),
    'VULCANO LOTUS': lambda ax, ay: wide(ax,ay,36,37),
    'DINO TORCH': lambda ax, ay: regular(ax,ay,37,36),
    'FIRE SNAKE': lambda ax, ay: regular(ax,ay,38,36),
    'POKEY': lambda ax, ay: regular(ax,ay,39,36),
    'HAMMER BRO': lambda ax, ay: tall(ax,ay-1,41,32),
    'FIRE BRO': lambda ax, ay: tall(ax,ay-1,42,32),
    'BOOMERANG BRO': lambda ax, ay: tall(ax,ay-1,43,32),
    'SLEDGE BRO': lambda ax, ay: o_piece(ax-1,ay,27,40),
    'SUMO BRO': lambda ax, ay: o_piece(ax-1,ay,27,38),
    'AMAZING FLYING HAMMER BRO': lambda ax, ay: afhb(ax,ay),
    'CHARGING CHUCK': lambda ax, ay: o_piece(ax-1,ay,27,36),
    'BUZZY BEETLE': lambda ax, ay: regular(ax,ay,36,35),
    'SPINY': lambda ax, ay: regular(ax,ay,37,35),
    'CEILING BUZZY BEETLE': lambda ax, ay: regular(ax,ay,38,35),
    'CEILING SPINY': lambda ax, ay: regular(ax,ay,39,35),
    'PIRANHA PLANT': lambda ax, ay: tall(ax-0.5,ay,0,42),
    'DOWN PIRANHA PLANT': lambda ax, ay: tall(ax-0.5,ay,0,44),
    'RIGHT PIRANHA PLANT': lambda ax, ay: wide(ax,ay-0.5,2,46),
    'LEFT PIRANHA PLANT': lambda ax, ay: wide(ax,ay-0.5,0,46),
    'RED PIRANHA PLANT': lambda ax, ay: vtile_two(ax-0.5,ay,0,42,1,43),
    'DOWN RED PIRANHA PLANT': lambda ax, ay: vtile_two(ax-0.5,ay,1,44,0,45),
    'RIGHT RED PIRANHA PLANT': lambda ax, ay: htile_two(ax,ay-0.5,2,47,3,46),
    'LEFT RED PIRANHA PLANT': lambda ax, ay: htile_two(ax,ay-0.5,0,46,1,47),
    'SHORT PIRANHA PLANT': lambda ax, ay: tall(ax-0.5,ay,2,42),
    'DOWN SHORT PIRANHA PLANT': lambda ax, ay: tall(ax-0.5,ay,2,44),
    'JUMP PIRANHA PLANT': lambda ax, ay: tall(ax-0.5,ay,3,42),
    'FIRE PIRANHA PLANT': lambda ax, ay: vtile_two(ax-0.5,ay,1,42,0,43),
    'DOWN FIRE PIRANHA PLANT': lambda ax, ay: vtile_two(ax-0.5,ay,0,44,1,45),
    'RIGHT FIRE PIRANHA PLANT': lambda ax, ay: htile_two(ax,ay-0.5,2,46,3,47),
    'LEFT FIRE PIRANHA PLANT': lambda ax, ay: htile_two(ax,ay-0.5,0,47,1,46),
    'RED JUMP PIRANHA PLANT': lambda ax, ay: vtile_two(ax-0.5,ay,3,42,3,44),
    'RED FIRE PIRANHA PLANT': lambda ax, ay: tall(ax-0.5,ay,1,42),
    'DOWN RED FIRE PIRANHA PLANT': lambda ax, ay: tall(ax-0.5,ay,1,44),
    'RIGHT RED FIRE PIRANHA PLANT': lambda ax, ay: wide(ax,ay-0.5,2,47),
    'LEFT RED FIRE PIRANHA PLANT': lambda ax, ay: wide(ax,ay-0.5,0,47),
    'BALL PIRANHA PLANT': lambda ax, ay: vtile_three(ax-0.5,ay-1,43,37,0,42,0,43),
    'PTOOIE': lambda ax, ay: tall(ax,ay,50,40),
    'SWOOPER': lambda ax, ay: regular(ax,ay,40,35),
    'BUSTER BEETLE': lambda ax, ay: regular(ax,ay,41,35),
    'NOKOBON': lambda ax, ay: regular(ax,ay,42,35),
    'SPIKETOP': lambda ax, ay: regular(ax,ay,43,35),
    'BLARGG': lambda ax, ay: regular(ax,ay,15,40),
    'SHY GUY': lambda ax, ay: regular(ax,ay,41,34),
    'BLUE SHY GUY': lambda ax, ay: regular(ax,ay,42,34),
    'SNIFIT': lambda ax, ay: regular(ax,ay,43,34),
    'BLUE SNIFIT': lambda ax, ay: regular(ax,ay,44,34),
    'BIG SHY GUY': lambda ax, ay: o_piece(ax-1,ay,44,32),
    'BIG BLUE SHY GUY': lambda ax, ay: o_piece(ax-1,ay,46,33),
    'BOMB GUY': lambda ax, ay: regular(ax,ay,40,36),
    'NINJI': lambda ax, ay: regular(ax,ay,41,36),
    'TWEETER': lambda ax, ay: regular(ax,ay,42,36),
    'GREY SNIFIT': lambda ax, ay: regular(ax,ay,43,36),
    'HOOPSTER': lambda ax, ay: regular(ax,ay,44,35),
    'FLURRY': lambda ax, ay: regular(ax,ay,45,34),
    'GREEN POKEY': lambda ax, ay: regular(ax,ay,46,32),
    'RED PANSER': lambda ax, ay: regular(ax,ay,4,42),
    'GREEN PANSER': lambda ax, ay: regular(ax,ay,5,42),
    'BLUE PANSER': lambda ax, ay: regular(ax,ay,6,42),
    'PORCUPO': lambda ax, ay: regular(ax,ay,7,42),
    'DRY BONES': lambda ax, ay: tall(ax,ay-1,4,43),
    'BONY BEETLE': lambda ax, ay: regular(ax,ay,7,43),
    'PODOBOO': lambda ax, ay: regular(ax,ay,4,45),
    'THWOMP': lambda ax, ay: o_piece(ax,ay,5,43),
    'THWIMP': lambda ax, ay: regular(ax,ay,4,46),
    'NET KOOPA': lambda ax, ay: tall(ax,ay-1,14,42),
    'RED NET KOOPA': lambda ax, ay: tall(ax,ay-1,15,42),
    'HYPER NET KOOPA': lambda ax, ay: tall(ax,ay-1,16,42),
    'NET SPARK': lambda ax, ay: regular(ax,ay,4,47),
    'LITTLE SPARK': lambda ax, ay: regular(ax,ay,5,47),
    'FAST SPARK': lambda ax, ay: regular(ax,ay,5,46),
    'BIG SPARK': lambda ax, ay: o_piece(ax,ay,8,44),
    'PHANTO': lambda ax, ay: regular(ax,ay,5,45),
    'ROTODISC': lambda ax, ay: regular(ax,ay,15,44),
    'FIREBAR': lambda ax, ay: firebar(ax,ay),
    'LARGE FIREBAR': lambda ax, ay: firebar_large(ax,ay),
    'GRINDER': lambda ax, ay: o_piece(ax-0.5,ay-0.5,6,46),
    'LINE GRINDER': lambda ax, ay: o_piece(ax-0.5,ay-0.5,8,46),
    'BALL & CHAIN': lambda ax, ay: ball(ax,ay),
    'BOUNCE PODOBOO': lambda ax, ay: regular(ax,ay,16,44),
    'GIANT SPIKE': lambda ax, ay: spike(ax,ay),
    'BOWSER STATUE': lambda ax, ay: o_piece(ax-0.5,ay-0.5,8,42),
    'GOLD BOWSER STATUE': lambda ax, ay: o_piece(ax-0.5,ay-0.5,10,42),
    'MECHAKOOPA': lambda ax, ay: o_piece(ax-0.5,ay-1,12,42),
    'CHAIN CHOMP': lambda ax, ay: regular(ax,ay,10,44),
    'FIRE CHOMP': lambda ax, ay: regular(ax,ay,11,44),
    'BOO': lambda ax, ay: regular(ax,ay,12,44),
    'BIG BOO': lambda ax, ay: sq_four(ax,ay,43,44),
    'STRETCH BOO': lambda ax, ay: regular(ax,ay+0.3125,13,44),
    'BLOCK BOO': lambda ax, ay: regular(ax,ay,14,44),
    'EERIE': lambda ax, ay: regular(ax,ay,10,45),
    'BOO CIRCLE': lambda ax, ay: boo_circle(ax,ay),
    'BOO SNAKE': lambda ax, ay: regular(ax,ay,11,45),
    'BOBOMB': lambda ax, ay: regular(ax,ay,12,45),
    'PARACHUTE BOBOMB': lambda ax, ay: vtile_two(ax,ay-1,29,38,13,45),
    'BULLET BILL': lambda ax, ay: regular(ax,ay,14,45),
    'SIDE BULLET BILL': lambda ax, ay: regular(ax,ay,15,45),
    'HOMING BULLET BILL': lambda ax, ay: regular(ax,ay,16,45),
    'BANZAI BILL': lambda ax, ay: sq_four(ax,ay,47,44),
    'DIAGONAL CANNON': lambda ax, ay: regular(ax,ay,13,39),
    'BOBOMB CANNON': lambda ax, ay: regular(ax,ay,17,39),
    'SIDE CANNON': lambda ax, ay: o_piece(ax,ay,10,46),
    'QUAD CANNON': lambda ax, ay: o_piece(ax,ay,12,46),
    'LARGE CANNONBALL': lambda ax, ay: o_piece(ax,ay,14,46),
    'RIGHT ENGINE': lambda ax, ay: htile_three(ax,ay,19,42,20,42,21,42),
    'LEFT ENGINE': lambda ax, ay: htile_three(ax-3,ay,19,43,20,43,21,43),
    'UP ENGINE': lambda ax, ay: vtile_three(ax,ay-3,18,44,18,45,18,46),
    'DOWN ENGINE': lambda ax, ay: vtile_three(ax,ay,19,44,19,45,19,46),
    'ROCKY WRENCH': lambda ax, ay: regular(ax,ay,17,44),
    'BULLET GENERATOR': lambda ax, ay: regular(ax,ay,18,47),
    'STORM GENERATOR': lambda ax, ay: regular(ax,ay,19,47),
    'CHEEP CHEEP GENERATOR': lambda ax, ay: regular(ax,ay,20,47),
    'LAKITU': lambda ax, ay: tall(ax,ay,16,46),
    'BALL LAKITU': lambda ax, ay: vtile_two(ax,ay,21,47,16,47),
    'ANGRY SUN': lambda ax, ay: o_piece(ax-0.25,ay-0.25,20,44),
    'MAGIKOOPA': lambda ax, ay: tall(ax,ay,22,42),
    'BOOM BOOM': lambda ax, ay: o_piece(ax-1,ay,43,42),
    'LARRY KOOPA': lambda ax, ay: o_piece(ax-1,ay,45,42),
    'MORTON KOOPA': lambda ax, ay: o_piece(ax-1,ay,47,42),
    'WENDY KOOPA': lambda ax, ay: o_piece(ax-1,ay,49,42),
    'IGGY KOOPA': lambda ax, ay: o_piece(ax-1,ay,26,46),
    'ROY KOOPA': lambda ax, ay: o_piece(ax-1,ay,26,44),
    'LEMMY KOOPA': lambda ax, ay: lemmy(ax-1,ay-1,24,45),
    'LUDWIG VON KOOPA': lambda ax, ay: o_piece(ax-1,ay,22,46),
    'BIRDO': lambda ax, ay: vtile_three(ax,ay-1,28,42,28,43,28,44),
    'MOUSER': lambda ax, ay: o_piece(ax-1,ay,26,42),
    'REZNOR': lambda ax, ay: reznor(ax,ay),
    'BOWSER': lambda ax, ay: lemmy(ax-1,ay,24,42),
    'AXE': lambda ax, ay: o_piece(ax-0.125,ay-0.1875,22,44),
    'COLLAPSING BRIDGE': lambda ax, ay: regular(ax,ay-0.5,20,46),
    'END BOSS': lambda ax, ay: regular(ax,ay,41,45)
}

warpcmd = {
    'WARP TOP': lambda ax, ay: regular(ax+0.5,ay,37,47),
    'WARP BOTTOM': lambda ax, ay: regular(ax+0.5,ay,38,46),
    'WARP LEFT': lambda ax, ay: regular(ax,ay+0.5,38,47),
    'WARP RIGHT': lambda ax, ay: regular(ax,ay+0.5,37,46),
    'DOOR': lambda ax, ay: tall(ax,ay,35,44),
    'LOCKED DOOR': lambda ax, ay: tall(ax,ay,36,44),
    'BOSS DOOR': lambda ax, ay: tall(ax,ay,37,44),
    'HIDDEN DOOR': lambda ax, ay: tall(ax,ay,38,44),
    'HIDDEN LOCKED DOOR': lambda ax, ay: tall(ax,ay,39,44),
    'BOMB DOOR': lambda ax, ay: tall(ax,ay,40,42),
    'WARP MARKER': lambda ax, ay: regular(ax,ay,34,45),
    'WARP CANNON': lambda ax, ay: regular(ax+0.5,ay,39,47),
    'DIAGONAL WARP CANNON': lambda ax, ay: regular(ax+0.5,ay+0.5,39,46),
    'UP': lambda ax, ay: regular(ax,ay,35,42),
    'DOWN': lambda ax, ay: regular(ax,ay,36,42),
    'LEFT': lambda ax, ay: regular(ax,ay,37,42),
    'RIGHT': lambda ax, ay: regular(ax,ay,38,42),
    'END': lambda ax, ay: regular(ax,ay,39,42),
    'SPEED': lambda ax, ay: regular(ax,ay,35,43),
    'CLOCKWISE': lambda ax, ay: regular(ax,ay,36,43),
    'COUNTERCLOCKWISE': lambda ax, ay: regular(ax,ay,37,43),
    'CLOCKWISE BOTTOM': lambda ax, ay: regular(ax,ay,38,43),
    'COUNTERCLOCKWISE BOTTOM': lambda ax, ay: regular(ax,ay,39,43)
}

modcmd = {
    'MUSHROOM': lambda ax, ay: regular(ax,ay,19,34),
    'FIRE FLOWER': lambda ax, ay: regular(ax,ay,3,45),
    'HAMMER SUIT': lambda ax, ay: regular(ax,ay,21,46),
    'LEAF': lambda ax, ay: regular(ax,ay,23,42),
    'TANOOKI SUIT': lambda ax, ay: regular(ax,ay,23,43),
    'FROG SUIT': lambda ax, ay: regular(ax,ay,28,45),
    'BOMB SHROOM': lambda ax, ay: regular(ax,ay,29,45),
    'ICE FLOWER': lambda ax, ay: regular(ax,ay,28,46),
    'SUPER FLOWER': lambda ax, ay: regular(ax,ay,28,47),
    'CARROT': lambda ax, ay: regular(ax,ay,41,42),
    'NINJA SUIT': lambda ax, ay: regular(ax,ay,42,42),
    'BEE SHROOM': lambda ax, ay: regular(ax,ay,40,47),
    'SHELL SUIT': lambda ax, ay: regular(ax,ay,41,43),
    'PENGUIN SUIT': lambda ax, ay: regular(ax,ay,42,43),
    'PROPELLER SHROOM': lambda ax, ay: regular(ax,ay,40,44),
    'BOOMERANG FLOWER': lambda ax, ay: regular(ax,ay,0,48),
    'WALL JUMP SHROOM': lambda ax, ay: regular(ax,ay,1,48),
    'ACORN': lambda ax, ay: regular(ax,ay,2,48),
    'CLOUD FLOWER': lambda ax, ay: regular(ax,ay,3,48),
    'ROCK SHROOM': lambda ax, ay: regular(ax,ay,4,48),
    'PYRE FLOWER': lambda ax, ay: regular(ax,ay,5,48),
    'SWOOPER SUIT': lambda ax, ay: regular(ax,ay,6,48),
    'KARATE SUIT': lambda ax, ay: regular(ax,ay,7,48),
    'SUPER CROWN': lambda ax, ay: regular(ax,ay,8,48),
    'GREEN YOSHI': lambda ax, ay: regular(ax,ay,9,48),
    'RED YOSHI': lambda ax, ay: regular(ax,ay,10,48),
    'YELLOW YOSHI': lambda ax, ay: regular(ax,ay,11,48),
    'BLUE YOSHI': lambda ax, ay: regular(ax,ay,12,48),
    'KURIBO SHOE': lambda ax, ay: regular(ax,ay,13,48),
    'BABURU SHOE': lambda ax, ay: regular(ax,ay,14,48),
    'DOSSUN SHOE': lambda ax, ay: regular(ax,ay,15,48),
    'JUGEMU SHOE': lambda ax, ay: regular(ax,ay,16,48),
    '1UP': lambda ax, ay: regular(ax,ay,13,35),
    '3UP': lambda ax, ay: regular(ax,ay,17,48),
    'POISON SHROOM': lambda ax, ay: regular(ax,ay,12,35),
    'STAR': lambda ax, ay: regular(ax,ay,16,35),
    'KEY': lambda ax, ay: regular(ax,ay,18,48),
    'SPRING': lambda ax, ay: regular(ax,ay,19,48),
    'SUPER SPRING': lambda ax, ay: regular(ax,ay,20,48),
    'P-SWITCH': lambda ax, ay: regular(ax,ay,21,48),
    'E-SWITCH': lambda ax, ay: regular(ax,ay,22,48),
    'PROPELLER BLOCK': lambda ax, ay: regular(ax,ay,23,48),
    'BEANSTALK': lambda ax, ay: regular(ax,ay,24,48),
    'TEXT': lambda ax, ay: regular(ax,ay,25,48),
    'DESTINATION': lambda ax, ay: regular(ax,ay,26,48),
    'MESSAGE': lambda ax, ay: regular(ax,ay,27,48)
}

def draw_obj(match):
    ax = float(match.group(1))
    ay = float(match.group(2))
    objname = match.group(3)
    call_cmd = objcmd.get(objname, lambda ax, ay: unknown(ax,ay))
    return call_cmd(ax, ay)

def draw_warps(match):
    ax = float(match.group(1))
    ay = float(match.group(2))
    objname = match.group(3)
    call_cmd = warpcmd.get(objname, lambda ax, ay: unknown(ax,ay))
    return call_cmd(ax, ay)

def draw_mods(match):
    ax = float(match.group(1))
    ay = float(match.group(2))
    objname = match.group(3)
    call_cmd = modcmd.get(objname, lambda ax, ay: unknown(ax,ay))
    return call_cmd(ax, ay)

# The conversion loop

while john <= i:
    file_in = f'{john}.section'
    if not os.path.exists(file_in):
        print('Do not tamper with program temporary files')
        sys.exit(0)
    
    with open(file_in,'r') as file:
        file_me = file.read()
    
    width = int(float(re.search(r'(?<="WIDTH": )(.*?)(?=, )',file_me).group()))
    height = int(float(re.search(r'(?<="HEIGHT": )(.*?)(?=, )',file_me).group()))
    realwidth = width * 16
    realheight = height * 16
    file_out = re.search(r'(?<=")(?:[^"\\]|\\.)*(?=")',file_me).group() + '.' + str(realwidth) + 'x' + str(realheight) + '.JON'
    if os.path.exists(file_out):
        os.remove(file_out)
    
    bg_image = ''
    x = 0
    y = 0
    
    if do_bg_image:
        bg_image = re.search(r'(?<="BACKGROUND": ")(.*?)(?=", )',file_me).group()
        bgcmd.get(bg_image, classic)()
        if bg_image.endswith(','):
            bg_image = bg_image[:-1]
    
    if do_bg_tiles:
        bg_tiles = re.search(r'(?<="TILES_BG": {)(.*?)(?=\})',file_me).group()
        bg_tiles = re.sub(r' "([^,]+),([^"]+)": "([^,]+),([^"]+)"',r'"\1-\2":[\3,\4]',bg_tiles)
    
    if do_tiles:
        tiles = re.search(r'(?<="TILES": {)(.*?)(?=\})',file_me).group()
        tiles = re.sub(r' "([^,]+),([^"]+)": "([^,]+),([^"]+)"',r'"\1-\2":[\3,\4]',tiles)
    
    submods = '' # Ensures turnip contents and afhb position markers are drawn after objects are placed
    
    if do_obj:
        obj = re.search(r'(?<="OBJECTS": {)(.*?)(?=\})',file_me).group()
        obj = re.sub(r' "([^,]+),([^"]+)": "(.*?)"',draw_obj,obj)
    
    if do_warps:
        warps = re.search(r'(?<="MARKERS": {)(.*?)(?=\})',file_me).group()
        warps = re.sub(r' "([^,]+),([^"]+)": "(.*?)"',draw_warps,warps)
        if submods.endswith(','): # because mods is not suppported, there will be no mods that follow submods
            submods = submods[:-1]
    elif submods.endswith(','):
        submods = submods[:-1]
        warps = submods
        do_warps = 1
    
    if do_mods:
        file_me = re.sub(r'(?<!\\)"TEXT:.*?(?<!\\)"(?:,|\s)','"TEXT",',file_me) # remove mod text first
        file_me = re.sub(r'(?<!\\)"DESTINATION:.*?(?<!\\)"(?:,|\s)','"DESTINATION",',file_me)
        file_me = re.sub(r'(?<!\\)"MESSAGE:.*?(?<!\\)"(?:,|\s)','"MESSAGE",',file_me)
        mods = re.search(r'(?<="MODIFIERS": {)(.*?)(?=\})',file_me).group()
        mods = re.sub(r' "([^,]+),([^"]+)": "(.*?)"',draw_mods,mods)
        if mods.endswith(','):
            mods = mods[:-1]
    
    with open(file_out,'a') as file:
        file.write('[{')
        if do_bg_image:
            file.write(bg_image + '},{')
        if do_bg_tiles:
            file.write(bg_tiles + '},{')
        if do_tiles:
            file.write(tiles + '},{')
        if do_obj:
            file.write(obj + '},{')
        if do_warps:
            file.write(warps + '},{')
        if do_mods:
            file.write(mods + '},{')
        file.write('}]')
    
    bg_image = ''
    bg_tiles = ''
    tiles = ''
    obj = ''
    warps = ''
    submods = ''
    mods = ''
    file_me = ''
    
    print(f'File was saved to {file_out}')
    if do_png:
        # Find + check tilemap
        if os.path.exists('788eb0.png'):
            file_in = '788eb0.png'
            valid = 1
        elif os.path.exists('../788eb0.png'):
            file_in = '../788eb0.png'
            valid = 1
        elif os.path.exists('../../788eb0.png'):
            file_in = '../../788eb0.png'
            valid = 1
        else:
            file_in = input('Path to 788eb0.png: ')
        try:
            with Image.open(file_in) as img:
                if img.format == 'PNG':
                    valid = 1
                    width, height = img.size
                    if width < 1840 or height < 1616:
                        valid = 0
                        print('PNG too small')
                else:
                    valid = 0
                    print('Not valid PNG')
        except Exception as e:
            print(f'Error: {e}')
            valid = 0
        
        if valid != 1:
            sys.exit()
        print(f'Drawing level...')
        
        # Open tilemap
        texture = Image.open(file_in).convert('RGBA')
        with open(file_out,'r') as file:
            tilemap = file.read()
        
        # Open finale image
        file_me = Image.new('RGBA', (realwidth,realheight), (0,0,0,0))
        
        # Find every tile
        tilemap = re.findall(r'"(-?[^-]+)-([^"]+)":\[([^,]+),([^\]]+)\]',tilemap)
        
        # Process every tile
        for match in tilemap:
            bx, by, ax, ay = match
            
            ax = int(float(ax) * 16)
            ay = int(float(ay) * 16)
            bx = int(float(bx) * 16)
            by = int(float(by) * 16)
            tile = texture.crop((ax, ay, ax + 16, ay + 16))
            file_me.paste(tile, (bx, by), tile)
        
        # Kill JON
        kill_jon = 1
        if kill_jon:
            if os.path.exists(file_out):
                os.remove(file_out)
        
        # Save
        file_out = file_out[:-4] + '.png'
        if os.path.exists(file_out):
            os.remove(file_out)
            print('overwriting file...')
        file_me.save(file_out)
        print(f'File was saved to {file_out}')
    
    # The most important part of this entire program
    john += 1

# Get rid of residual files
john = 1
while john <= i:
    if os.path.exists(f'{john}.section'):
        os.remove(f'{john}.section')
    john += 1