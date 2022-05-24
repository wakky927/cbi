#!/bin/bash

cd ../src/2022_04_10/

python3 pre_dark_linux2.py "C001H001S009" 6001 &
python3 pre_dark_linux2.py "C001H001S009" 7001 &
python3 pre_dark_linux2.py "C001H001S009" 8001 &
python3 pre_dark_linux2.py "C001H001S009" 9001 &
python3 pre_dark_linux2.py "C001H001S0010" 6001 &
python3 pre_dark_linux2.py "C001H001S0010" 7001 &
python3 pre_dark_linux2.py "C001H001S0010" 8001 &
python3 pre_dark_linux2.py "C001H001S0010" 9001 &

wait

echo "all program fin."
