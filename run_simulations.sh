#!/bin/bash
python main.py --settings ./runs/rnd_00.ini
python analyse.py -i ./runs/output/rnd_00 -n 6
python main.py --settings ./runs/rnd_01.ini
python analyse.py -i ./runs/output/rnd_01 -n 6
python main.py --settings ./runs/rnd_02.ini
python analyse.py -i ./runs/output/rnd_02 -n 6
python main.py --settings ./runs/rnd_03.ini
python analyse.py -i ./runs/output/rnd_03 -n 6
python main.py --settings ./runs/rnd_04.ini
python analyse.py -i ./runs/output/rnd_04 -n 6
python main.py --settings ./runs/rnd_05.ini
python analyse.py -i ./runs/output/rnd_05 -n 6
python main.py --settings ./runs/rnd_06.ini
python analyse.py -i ./runs/output/rnd_06 -n 6
python main.py --settings ./runs/rnd_07.ini
python analyse.py -i ./runs/output/rnd_07 -n 6
python main.py --settings ./runs/rnd_08.ini
python analyse.py -i ./runs/output/rnd_08 -n 6
python main.py --settings ./runs/rnd_09.ini
python analyse.py -i ./runs/output/rnd_09 -n 6
python main.py --settings ./runs/rnd_10.ini
python analyse.py -i ./runs/output/rnd_10 -n 6