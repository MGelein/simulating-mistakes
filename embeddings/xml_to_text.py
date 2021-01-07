from xml.dom import minidom
import os
from tqdm import tqdm

def start_conversion():
    for file in tqdm(os.listdir('./xml/')):
        convert_file(file)

def convert_file(url):
    doc = minidom.parse('./xml/' + url)
    wordElements = doc.getElementsByTagName('word')
    words = [word.attributes['form'].value for word in wordElements]
    with open('./text/' + url, 'w', encoding='utf8') as f:
        for word in words:
            f.write(word)
            f.write('\n')

if __name__ == '__main__':
    start_conversion()