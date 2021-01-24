#!/bin/bash
python main.py --settings ./runs/it_25.ini
python analyse.py -i ./runs/output/it_25 -n 6

python main.py --settings ./runs/it_30.ini
python analyse.py -i ./runs/output/it_30 -n 6