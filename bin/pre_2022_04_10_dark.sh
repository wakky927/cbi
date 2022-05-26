cd ../src/2022_04_10/

python3 pre_dark.py "C001H001S0001" &
python3 pre_dark.py "C001H001S0002" &
python3 pre_dark.py "C001H001S0003" &
python3 pre_dark.py "C001H001S0004" &

wait

python3 pre_dark.py "C001H001S0005" &
python3 pre_dark.py "C001H001S0006" &
python3 pre_dark.py "C001H001S0007" &

wait

python3 pre_dark.py "C001H001S0008" &
python3 pre_dark.py "C001H001S0009" &
python3 pre_dark.py "C001H001S0010" &

wait

echo "all program fin."
