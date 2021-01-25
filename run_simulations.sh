#!/bin/bash

python main.py --settings ./runs/inf_02_03.ini
python analyse.py -i ./runs/output/inf_02_03 -n 6
python main.py --settings ./runs/inf_00_03.ini
python analyse.py -i ./runs/output/inf_00_03 -n 6