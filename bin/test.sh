#!/bin/bash

cd ../src/2022_01_23/

python3 pre.py "s" "../../data/2022_01_23/cbi_q_1/" "../../data/2022_01_23/test/" 0 10 "../../data/2022_01_23/test/bg.bmp"
python3 pre.py "c" "../../data/2022_01_23/cbi_q_1/" "../../data/2022_01_23/test/" 0 10

wait

echo "all program fin."
