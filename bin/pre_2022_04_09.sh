#!/bin/bash

cd ../src/2022_04_09/

python3 pre_light.py "G:\\M2" "C001H001S0001" &
python3 pre_light.py "G:\\M2" "C001H001S0002" &
python3 pre_light.py "G:\\M2" "C001H001S0003" &
python3 pre_light.py "G:\\M2" "C001H001S0004" &
python3 pre_light.py "G:\\M2" "C001H001S0005" &
python3 pre_light.py "G:\\M2" "C001H001S0006" &
python3 pre_light.py "G:\\M2" "C001H001S0007" &
python3 pre_light.py "G:\\M2" "C001H001S0008" &
python3 pre_light.py "G:\\M2" "C001H001S0009" &
python3 pre_light.py "G:\\M2" "C001H001S00010" &

wait

echo "all program fin."
