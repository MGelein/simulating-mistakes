import numpy as np
from tqdm import tqdm
from numpy import dot
from numpy.linalg import norm
import sys
from types import SimpleNamespace
from itertools import permutations

def parse_params():
    params = {'input': '.', 'number': 5}
    for i, arg in enumerate(sys.argv):
        if arg in ['-i', '--input']:
            params['input'] = sys.argv[i + 1]
        elif arg in ['-n', '--number-of-agents']:
            params['number'] = int(sys.argv[i + 1])

    return SimpleNamespace(**params)

def term_frequency(texts):
    words_collection = []

    # Split each text into list of words
    for text in texts:
        words_collection.append(text.split(' '))
    
    # Make a set of all unique terms in every doc
    terms = set()
    for words in words_collection:
        for word in words: terms.add(word)

    # Create the empty vectors for every text
    terms_collection = []
    for _ in words_collection:
        terms_collection.append(np.zeros(len(terms)))

    # Count every word in every text
    for i, term in enumerate(terms):
        for words, text_terms in zip(words_collection, terms_collection):
            text_terms[i] = count_words(words, term)

    return terms_collection
    
def cosine_similarity(terms_a, terms_b):
    return dot(terms_a, terms_b) / (norm(terms_a) * norm(terms_b))

def count_words(words, term):
    total = 0
    for word in words:
        if word == term:
            total += 1
    return total

def load_textfile(url):
    lines = []
    try:
        with open(url + ".txt", 'r', encoding='utf8') as f:
            for line in f.readlines():
                lines.append(line.replace('\n', ''))
    except:
        pass
    return " ".join(lines)

if __name__ == '__main__':
    params = parse_params()
    files = []
    print("Analysing %d files in directory: %s" % (params.number, params.input))
    for i in range(params.number):
        files.append(load_textfile(params.input + '/agent_%d' % i))
    tfs = term_frequency(files)

    cossims = []
    for tf_a, tf_b in permutations(tfs, 2):
        cossims.append((cosine_similarity(tf_a, tf_b)))

    mean = sum(cossims) / len(cossims)
    minimum = min(cossims)
    maximum = max(cossims)

    with open(params.input + "/results.txt", 'w') as f:
        f.write('values: ')
        for value in cossims: f.write('%f, ' % value)
        f.write('\n')
        f.write('mean: %f\n' % mean)
        f.write('range: %f to %f' % (minimum, maximum))
    print('Analysis of %s directory saved to %s' % (params.input, params.input + "/results.txt"))