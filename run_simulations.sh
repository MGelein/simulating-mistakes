#!/bin/bash
python main.py --settings ./runs/mem_00_01.ini
python analyse.py -i ./runs/output/mem_00_01 -n 6
python main.py --settings ./runs/mem_02_03.ini
python analyse.py -i ./runs/output/mem_02_03 -n 6
python main.py --settings ./runs/mem_04_05.ini
python analyse.py -i ./runs/output/mem_04_05 -n 6
python main.py --settings ./runs/mem_06_07.ini
python analyse.py -i ./runs/output/mem_06_07 -n 6
python main.py --settings ./runs/mem_08_09.ini
python analyse.py -i ./runs/output/mem_08_09 -n 6
python main.py --settings ./runs/mem_10_10.ini
python analyse.py -i ./runs/output/mem_10_10 -n 6
python main.py --settings ./runs/mem_00_03.ini
python analyse.py -i ./runs/output/mem_00_03 -n 6
python main.py --settings ./runs/mem_02_05.ini
python analyse.py -i ./runs/output/mem_02_05 -n 6
python main.py --settings ./runs/mem_04_07.ini
python analyse.py -i ./runs/output/mem_04_07 -n 6
python main.py --settings ./runs/mem_06_09.ini
python analyse.py -i ./runs/output/mem_06_09 -n 6
python main.py --settings ./runs/mem_08_10.ini
python analyse.py -i ./runs/output/mem_08_10 -n 6
python main.py --settings ./runs/mem_00_05.ini
python analyse.py -i ./runs/output/mem_00_05 -n 6
python main.py --settings ./runs/mem_02_07.ini
python analyse.py -i ./runs/output/mem_02_07 -n 6
python main.py --settings ./runs/mem_04_09.ini
python analyse.py -i ./runs/output/mem_04_09 -n 6
python main.py --settings ./runs/mem_06_10.ini
python analyse.py -i ./runs/output/mem_06_10 -n 6