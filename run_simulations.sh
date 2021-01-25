#!/bin/bash

python main.py --settings ./runs/mem_00_07.ini
python analyse.py -i ./runs/output/mem_00_07 -n 6
python main.py --settings ./runs/mem_02_09.ini
python analyse.py -i ./runs/output/mem_02_09 -n 6
python main.py --settings ./runs/mem_04_10.ini
python analyse.py -i ./runs/output/mem_04_10 -n 6