print("Handeling imports...")
import sys
from gensim.models import KeyedVectors
from simulation import Simulation

def show_help():
    print("""
    Welcome to the text transmission simulation tool, you can use the following arguments:
    --input         -i      the input file, f.e. "file.txt"
    --output        -o      the output file, this is where the output of the algorithm is saved
    --embeddings    -e      the embeddings file, this is the word embeddings used to 
    --population    -p      [OPTIONAL], population size, defaults to 100
    --generations   -g      [OPTIONAL], amount of generations the agents get to give the text between eachother, defaults to 100
    """)
    exit()

def load_lines(url):
    lines = []
    with open(url, 'r', encoding='utf8') as f:
        for line in f.readlines():
            line = line.replace('\r', '').replace('\n', '')
            if len(line) < 1: continue
            lines.append(line.split(' '))
    return lines

def parse_params():
    params = {'population_size': 100, 'generations': 100}
    for i in range(len(sys.argv)):
        arg = sys.argv[i]
        if i + 1 < len(sys.argv): next_arg = sys.argv[i + 1]
        else: next_arg = None

        if arg in ('--input', '-i'):
            params['input'] = next_arg
        elif arg in ('--output', '-o'):
            params['output'] = next_arg
        elif arg in ('--embeddings', '-e'):
            params['embeddings'] = next_arg
        elif arg in ('--population', '-p'):
            params['population_size'] = int(next_arg)
        elif arg in ('--generations', '-g'):
            params['generations'] = int(next_arg)

    return params

def start_simulation(params):
    print("Loading embeddings from: %s" % params['embeddings'])
    embeddings = KeyedVectors.load(params['embeddings'])
    print("Loading text from: %s" % params['input'])
    lines = load_lines(params['input'])

    simulation = Simulation(lines, embeddings, params)
    simulation.run(params['generations'])
    simulation.save_result(params['output'])

if __name__ == '__main__':

    if len(sys.argv) < 1:
        show_help()
    else:
        params = parse_params()

    start_simulation(params)