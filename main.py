from loader import load_embeddings, load_lines


def start_simulation():
    embeddings = load_embeddings()
    lines = load_lines('./data/hom.il.1.txt')

if __name__ == '__main__':
    start_simulation()  