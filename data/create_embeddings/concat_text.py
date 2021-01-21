import os
from tqdm import tqdm

lines = []
for file in tqdm(os.listdir('./text/')):
    with open('./text/' + file, 'r', encoding='utf8') as f:
        for line in f.readlines():
            lines.append(line)

with open('./words.txt', 'w', encoding='utf8') as f:
    for line in tqdm(lines):
        f.write(line)