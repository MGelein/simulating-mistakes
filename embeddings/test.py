from gensim.models import KeyedVectors

embeddings = KeyedVectors.load("embeddings.wv")
foundWord = 'Θουκυδίδης' in embeddings
print("Found the word 'Θουκυδίδης': " + str(foundWord))
print("The embedding is: ")
print(embeddings['Θουκυδίδης'])