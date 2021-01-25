#!/bin/bash

python main.py --settings ./runs/arr_000_001.ini
python analyse.py -i ./runs/output/arr_000_001 -n 6
python main.py --settings ./runs/arr_020_021.ini
python analyse.py -i ./runs/output/arr_020_021 -n 6
python main.py --settings ./runs/arr_040_041.ini
python analyse.py -i ./runs/output/arr_040_041 -n 6
python main.py --settings ./runs/arr_060_061.ini
python analyse.py -i ./runs/output/arr_060_061 -n 6
python main.py --settings ./runs/arr_080_081.ini
python analyse.py -i ./runs/output/arr_080_081 -n 6
python main.py --settings ./runs/arr_100_100.ini
python analyse.py -i ./runs/output/arr_100_100 -n 6
python main.py --settings ./runs/arr_000_010.ini
python analyse.py -i ./runs/output/arr_000_010 -n 6
python main.py --settings ./runs/arr_020_030.ini
python analyse.py -i ./runs/output/arr_020_030 -n 6
python main.py --settings ./runs/arr_040_050.ini
python analyse.py -i ./runs/output/arr_040_050 -n 6
python main.py --settings ./runs/arr_060_070.ini
python analyse.py -i ./runs/output/arr_060_070 -n 6
python main.py --settings ./runs/arr_080_090.ini
python analyse.py -i ./runs/output/arr_080_090 -n 6
python main.py --settings ./runs/arr_000_030.ini
python analyse.py -i ./runs/output/arr_000_030 -n 6
python main.py --settings ./runs/arr_020_050.ini
python analyse.py -i ./runs/output/arr_020_050 -n 6
python main.py --settings ./runs/arr_040_070.ini
python analyse.py -i ./runs/output/arr_040_070 -n 6
python main.py --settings ./runs/arr_060_090.ini
python analyse.py -i ./runs/output/arr_060_090 -n 6
python main.py --settings ./runs/arr_080_100.ini
python analyse.py -i ./runs/output/arr_080_100 -n 6
python main.py --settings ./runs/arr_000_060.ini
python analyse.py -i ./runs/output/arr_000_060 -n 6
python main.py --settings ./runs/arr_020_080.ini
python analyse.py -i ./runs/output/arr_020_080 -n 6
python main.py --settings ./runs/arr_040_100.ini
python analyse.py -i ./runs/output/arr_040_100 -n 6
python main.py --settings ./runs/arr_060_100.ini
python analyse.py -i ./runs/output/arr_060_100 -n 6