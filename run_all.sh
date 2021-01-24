#!/bin/bash

python main.py --settings ./runs/population_2.ini
python analyse.py -i ./runs/output/population_2 -n 2
python main.py --settings ./runs/population_3.ini
python analyse.py -i ./runs/output/population_3 -n 3
python main.py --settings ./runs/population_4.ini
python analyse.py -i ./runs/output/population_4 -n 4
python main.py --settings ./runs/population_5.ini
python analyse.py -i ./runs/output/population_5 -n 5
python main.py --settings ./runs/population_6.ini
python analyse.py -i ./runs/output/population_6 -n 6
python main.py --settings ./runs/population_7.ini
python analyse.py -i ./runs/output/population_7 -n 7
python main.py --settings ./runs/population_8.ini
python analyse.py -i ./runs/output/population_8 -n 8
python main.py --settings ./runs/population_9.ini
python analyse.py -i ./runs/output/population_9 -n 9
python main.py --settings ./runs/population_10.ini
python analyse.py -i ./runs/output/population_10 -n 10

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
python main.py --settings ./runs/it_25.ini
python analyse.py -i ./runs/output/it_25 -n 6
python main.py --settings ./runs/it_30.ini
python analyse.py -i ./runs/output/it_30 -n 6