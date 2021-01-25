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
python main.py --settings ./runs/mem_00_07.ini
python analyse.py -i ./runs/output/mem_00_07 -n 6
python main.py --settings ./runs/mem_02_09.ini
python analyse.py -i ./runs/output/mem_02_09 -n 6
python main.py --settings ./runs/mem_04_10.ini
python analyse.py -i ./runs/output/mem_04_10 -n 6

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