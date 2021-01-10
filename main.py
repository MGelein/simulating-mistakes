print("Handeling imports...")
import sys
from gensim.models import KeyedVectors
from simulation import Simulation
from util import similar_looking_word, set_edit_dist_function
from configparser import ConfigParser

def show_help():
    print("""
    Welcome to the text transmission simulation tool, you can use the following arguments:
    --settings      -s      .ini settings file, if this is provided no other options are necessary, otherwise use the command line options
    --input         -i      [OPTIONAL] the input file, f.e. "file.txt"
    --output        -o      [OPTIONAL] the output director, this is where the output of the algorithm is saved
    --embeddings    -e      [OPTIONAL] the embeddings file, this is the word embeddings used to 
    --population    -p      [OPTIONAL], population size, defaults to 5
    --generations   -g      [OPTIONAL], amount of generations the agents get to give the text between eachother, defaults to 10
    --edit-fn       -f      [OPTIONAL], 'modified-hamming' or 'levenshtein', to set the edit distance comparison function used, default is 'modified hamming'
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

def parse_ini(url, params):
    config = ConfigParser()
    config.read(url)
    params['embeddings'] = config.get('simulation', 'embeddings')
    params['input'] = config.get('simulation', 'input')
    params['output'] = config.get('simulation', 'output_dir')
    params['population_size'] = config.get('simulation', 'population_size')
    params['generations'] = config.get('simulation', 'generations')
    return params

def parse_params():
    params = {'population_size': 5, 'generations': 10, 'edit_function': 'modified-hamming'}
    for i in range(len(sys.argv)):
        arg = sys.argv[i]
        if i + 1 < len(sys.argv): next_arg = sys.argv[i + 1]
        else: next_arg = None

        if arg in ('--input', '-i'):
            params['input'] = next_arg
        elif arg in ('--output-dir', '-o'):
            params['output'] = next_arg
        elif arg in ('--embeddings', '-e'):
            params['embeddings'] = next_arg
        elif arg in ('--population', '-p'):
            params['population_size'] = int(next_arg)
        elif arg in ('--generations', '-g'):
            params['generations'] = int(next_arg)
        elif arg in ('--edit-fn', '-f'):
            params['edit_function'] = next_arg
        elif arg in ('--settings', '-s'):
            params = parse_ini(next_arg, params)
            break

    return params

def start_simulation(params):
    print("Loading embeddings from: %s" % params['embeddings'])
    embeddings = KeyedVectors.load(params['embeddings'])
    print("Loading text from: %s" % params['input'])
    lines = load_lines(params['input'])
    set_edit_dist_function(params['edit_function'])

    simulation = Simulation(lines, embeddings, params)
    simulation.run(params['generations'])
    simulation.save_result(params['output'])

if __name__ == '__main__':

    if len(sys.argv) < 1:
        show_help()
    else:
        params = parse_params()

    start_simulation(params)