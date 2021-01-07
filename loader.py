from gensim.models import KeyedVectors

def load_embeddings():
    return KeyedVectors.load('./data/embeddings.wv')

def load_lines(url):
    lines = []
    with open(url, 'r', encoding='utf8') as f:
        for line in f.readlines():
            line = line.replace('\r', '').replace('\n', '')
            if len(line) < 1: continue
            lines.append(line.split(' '))
    return lines