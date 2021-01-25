#!/bin/bash
python main.py --settings ./runs/inf_00_01.ini
python analyse.py -i ./runs/output/inf_00_01 -n 6
python main.py --settings ./runs/inf_02_03.ini
python analyse.py -i ./runs/output/inf_02_03 -n 6
python main.py --settings ./runs/inf_04_05.ini
python analyse.py -i ./runs/output/inf_04_05 -n 6
python main.py --settings ./runs/inf_06_07.ini
python analyse.py -i ./runs/output/inf_06_07 -n 6
python main.py --settings ./runs/inf_08_09.ini
python analyse.py -i ./runs/output/inf_08_09 -n 6
python main.py --settings ./runs/inf_10_10.ini
python analyse.py -i ./runs/output/inf_10_10 -n 6
python main.py --settings ./runs/inf_00_03.ini
python analyse.py -i ./runs/output/inf_00_03 -n 6
python main.py --settings ./runs/inf_02_05.ini
python analyse.py -i ./runs/output/inf_02_05 -n 6
python main.py --settings ./runs/inf_04_07.ini
python analyse.py -i ./runs/output/inf_04_07 -n 6
python main.py --settings ./runs/inf_06_09.ini
python analyse.py -i ./runs/output/inf_06_09 -n 6
python main.py --settings ./runs/inf_08_10.ini
python analyse.py -i ./runs/output/inf_08_10 -n 6
python main.py --settings ./runs/inf_00_05.ini
python analyse.py -i ./runs/output/inf_00_05 -n 6
python main.py --settings ./runs/inf_02_07.ini
python analyse.py -i ./runs/output/inf_02_07 -n 6
python main.py --settings ./runs/inf_04_09.ini
python analyse.py -i ./runs/output/inf_04_09 -n 6
python main.py --settings ./runs/inf_06_10.ini
python analyse.py -i ./runs/output/inf_06_10 -n 6
python main.py --settings ./runs/inf_00_07.ini
python analyse.py -i ./runs/output/inf_00_07 -n 6
python main.py --settings ./runs/inf_02_09.ini
python analyse.py -i ./runs/output/inf_02_09 -n 6
python main.py --settings ./runs/inf_04_10.ini
python analyse.py -i ./runs/output/inf_04_10 -n 6