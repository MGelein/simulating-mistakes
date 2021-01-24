from random import choice, random, randint
from util import similar_looking_word, closest_word

class Agent:
    
    def __init__(self, simulation, number):
        self.simulation = simulation
        self.canonical_text = simulation.text[:]
        self.written_text = self.canonical_text[:]
        self.remembered_text = self.canonical_text[:]
        self.memory = simulation.sample_memory()
        self.arrogance = simulation.sample_arrogance()
        self.influence = simulation.sample_influence()
        self.vocabulary = simulation.sample_vocabulary()
        self.position = simulation.sample_position(number)
        self.known_words = {}

    def in_vocab(self, word):
        if word in self.known_words: return self.known_words[word]
        known = random() < self.vocabulary
        self.known_words[word] = known
        return known
    
    def skip_line(self, sentences):
        sentence, next_sentence = sentences
        if random() < self.arrogance: 
            return [next_sentence]
        
        for word in next_sentence:
            if word in sentence:
                start = sentence.index(word)
                end = next_sentence.index(word)
                return [sentence[:start] + next_sentence[end:]]

        return sentences

    def substitute_word(self, word):
        if random() > self.arrogance and self.in_vocab(word):
            return word
        try:
            top_ten = self.simulation.embeddings.most_similar(positive=[word], topn=10)
        except:
            return word
        return choice(top_ten)[0]

    def mutate_letter(self, word, alphabet):
        rnd_index = randint(0, len(word) - 1) if len(word) > 1 else 0
        letter = choice(alphabet)
        new_word = word[:rnd_index] + letter + word[rnd_index + 1:]
        if self.in_vocab(new_word):
            return new_word
        else:
            return new_word if random() < self.arrogance else word

    def read_word(self, word, line):
        if random() > self.memory:
            return self.mutate_letter(word, line)
        return word

    def make_canonical(self):
        self.canonical_text = self.written_text

    def write_word(self, word):
        if self.in_vocab(word): 
            return self.substitute_word(word)
        else:
            if random() > self.memory:
                return similar_looking_word(word, self.simulation.embeddings.vocab)
            else: 
                return word

    def read(self, agent):
        read_text = []
        skipped_text = []

        i = 0
        while i < len(agent.canonical_text) - 1:
            line = agent.canonical_text[i]
            next_line = agent.canonical_text[i + 1]
            after_skip_lines = self.skip_line([line, next_line]) if random() > self.memory else [line, next_line]
            
            for l in after_skip_lines: skipped_text.append(l)
            i += 2

        for line in skipped_text:
            read_line = []
            joined_line = "".join(line).replace("·", '').replace('\'', '').replace('.', '')
            for word in line:
                read_line.append(self.read_word(word, joined_line))
            read_text.append(read_line)
        self.remembered_text = read_text

    def write(self):
        write_text = []
        for line in self.remembered_text:
            written_line = []
            for word in line:
                written_line.append(self.write_word(word))
            write_text.append(written_line)
        self.written_text = write_text

