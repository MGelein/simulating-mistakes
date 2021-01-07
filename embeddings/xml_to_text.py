from xml.dom import minidom
import os
from tqdm import tqdm

def start_conversion():
    for file in tqdm(os.listdir('./xml/')):
        convert_file(file)

def convert_file(url):
    doc = minidom.parse('./xml/' + url)
    sentenceElements = doc.getElementsByTagName('sentence')
    sentences = []
    for sentenceElement in sentenceElements:
        words = []
        for word in sentenceElement.childNodes:
            if word.nodeName == 'word':
                words.append(word.attributes['form'].value)
        sentences.append(words)
    
    with open('./text/' + url, 'w', encoding='utf8') as f:
        for sentence in sentences:
            for word in sentence:
                f.write(word)
                f.write(' ')
            f.write('\n')

if __name__ == '__main__':
    start_conversion()