print("Handeling imports...")
import sys
from gensim.models import KeyedVectors
from simulation import Simulation
from util import set_edit_dist_function
from iniparser import parse_params

def show_help():
    print("""Welcome to the text transmission simulation tool, you can use the following arguments:
    --settings      -s      .ini settings file location""")
    exit()

def load_lines(url):
    lines = []
    with open(url, 'r', encoding='utf8') as f:
        for line in f.readlines():
            line = line.replace('\r', '').replace('\n', '')
            if len(line) < 1: continue
            lines.append(line.split(' '))
    return lines

def start_simulation(params):
    print("Loading embeddings from: %s" % params.embeddings)
    embeddings = KeyedVectors.load(params.embeddings)
    print("Loading text from: %s" % params.input)
    lines = load_lines(params.input)
    set_edit_dist_function(params.edit_function)

    simulation = Simulation(lines, embeddings, params)
    simulation.run(params.iterations)
    simulation.save_result(params.output)

if __name__ == '__main__':

    if len(sys.argv) < 1:
        show_help()
    else:
        params = parse_params()
    if params is None: show_help()

    start_simulation(params)