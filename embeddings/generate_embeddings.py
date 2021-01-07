from os import cpu_count
print("Importing gensim")
from gensim.models import Word2Vec
print("Loading text data")
lines = []
with open('./words.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        parts = line.replace('\n', '').split(' ')
        words = []
        for part in parts:
            if len(part) > 0:
                words.append(part)
        lines.append(words)

print("Training model, stand by")
model = Word2Vec(sentences=lines, min_count=1, workers=cpu_count())
print("Saving model...")
model.wv.save("embeddings.wv") # Save the KeyedVector instance to disk, can be reloaded by KeyedVectors.load("word2vec.wordvectors", mmap='r')