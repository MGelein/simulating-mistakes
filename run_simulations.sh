#!/bin/bash
python main.py --settings ./runs/it_1.ini
python analyse.py -i ./runs/output/it_1 -n 6

python main.py --settings ./runs/it_5.ini
python analyse.py -i ./runs/output/it_5 -n 6

python main.py --settings ./runs/it_10.ini
python analyse.py -i ./runs/output/it_10 -n 6

python main.py --settings ./runs/it_15.ini
python analyse.py -i ./runs/output/it_15 -n 6

python main.py --settings ./runs/it_20.ini
python analyse.py -i ./runs/output/it_20 -n 6