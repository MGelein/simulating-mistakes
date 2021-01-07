from gensim.models import KeyedVectors

def load_embeddings():
    return KeyedVectors.load('./data/embeddings.wv')

def load_lines(url):
    lines = []
    with open(url, 'r', encoding='utf8') as f:
        for line in f.readlines():
            lines.append(line.replace('\n', ''))
    return lines