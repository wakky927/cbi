import os

if __name__ == '__main__':
    user = os.environ["USER"]
    SUPER_DIR = f"/media/{user}/ボリューム1/M2/original/2022_04_09/"

    dir_in = SUPER_DIR + f"cbi_q_30/C001H001S0001/C001H001S0001"
    dir_out = SUPER_DIR + f"cbi_q_3/C001H001S0008/C001H001S0008"

    for i in range(1, 5001):
        os.rename(dir_in + f"{i:06}.bmp", dir_out + f"{i:06}.bmp")

    print("fin.")
