#!/bin/bash

cd ../src/2022_01_23/

python3 pre.py "b" "/media/takuya/HDD/M1/original/2022_01_23/bg/" "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/" 0 3234 "min"

wait

python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_1/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_1/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &
python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_2/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_2/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &
python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_3/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_3/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &
python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_4/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_4/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &
python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_5/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_5/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &
python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_6/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_6/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &

wait

python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_05/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_05/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &
python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_15/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_15/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &
python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_25/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_25/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &
python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_35/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_35/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &
python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_45/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_45/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &
python3 pre.py "s" "/media/takuya/HDD/M1/original/2022_01_23/cbi_q_55/" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_55/" 0 3234 "/media/takuya/HDD/M1/result/2022_01_23/pre/bg/bg.bmp" &

wait

python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_1/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_1/" 0 3234 &
python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_2/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_2/" 0 3234 &
python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_3/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_3/" 0 3234 &
python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_4/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_4/" 0 3234 &
python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_5/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_5/" 0 3234 &
python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_6/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_6/" 0 3234 &

wait

python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_05/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_05/" 0 3234 &
python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_15/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_15/" 0 3234 &
python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_25/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_25/" 0 3234 &
python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_35/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_35/" 0 3234 &
python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_45/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_45/" 0 3234 &
python3 pre.py "c" "/media/takuya/HDD/M1/result/2022_01_23/pre/sub/cbi_q_55/" "/media/takuya/HDD/M1/result/2022_01_23/pre/calib/cbi_q_55/" 0 3234 &

wait

echo "all program fin."
