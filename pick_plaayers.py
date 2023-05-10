import glob
import random
import os
import shutil


def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

players = glob.glob("all_players/*.bdot")

random.shuffle(players)

i=0
for game in divide_chunks(players, 5):
    os.makedirs(f"games/{i}")
    for p in game:
        bdot = p.split('/')[1]
        shutil.copyfile(p, f"games/{i}/{bdot}")
    i += 1




