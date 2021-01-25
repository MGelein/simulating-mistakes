#!/bin/bash

python main.py --settings ./runs/voc_00_01.ini
python analyse.py -i ./runs/output/voc_00_01 -n 6
python main.py --settings ./runs/voc_02_03.ini
python analyse.py -i ./runs/output/voc_02_03 -n 6
python main.py --settings ./runs/voc_04_05.ini
python analyse.py -i ./runs/output/voc_04_05 -n 6
python main.py --settings ./runs/voc_06_07.ini
python analyse.py -i ./runs/output/voc_06_07 -n 6
python main.py --settings ./runs/voc_08_09.ini
python analyse.py -i ./runs/output/voc_08_09 -n 6
python main.py --settings ./runs/voc_10_10.ini
python analyse.py -i ./runs/output/voc_10_10 -n 6
python main.py --settings ./runs/voc_00_03.ini
python analyse.py -i ./runs/output/voc_00_03 -n 6
python main.py --settings ./runs/voc_02_05.ini
python analyse.py -i ./runs/output/voc_02_05 -n 6
python main.py --settings ./runs/voc_04_07.ini
python analyse.py -i ./runs/output/voc_04_07 -n 6
python main.py --settings ./runs/voc_06_09.ini
python analyse.py -i ./runs/output/voc_06_09 -n 6
python main.py --settings ./runs/voc_08_10.ini
python analyse.py -i ./runs/output/voc_08_10 -n 6
python main.py --settings ./runs/voc_00_05.ini
python analyse.py -i ./runs/output/voc_00_05 -n 6
python main.py --settings ./runs/voc_02_07.ini
python analyse.py -i ./runs/output/voc_02_07 -n 6
python main.py --settings ./runs/voc_04_09.ini
python analyse.py -i ./runs/output/voc_04_09 -n 6
python main.py --settings ./runs/voc_06_10.ini
python analyse.py -i ./runs/output/voc_06_10 -n 6
python main.py --settings ./runs/voc_00_07.ini
python analyse.py -i ./runs/output/voc_00_07 -n 6
python main.py --settings ./runs/voc_02_09.ini
python analyse.py -i ./runs/output/voc_02_09 -n 6
python main.py --settings ./runs/voc_04_10.ini
python analyse.py -i ./runs/output/voc_04_10 -n 6