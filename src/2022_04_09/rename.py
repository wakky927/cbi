import os

if __name__ == '__main__':
    # user = os.environ["USER"]
    # SUPER_DIR = f"/media/{user}/ボリューム1/M2/original/2022_04_09/"
    SUPER_DIR = "E:\\M2\\original\\2022_06_22\\at_r_10_mm\\rbi\\rbi_q_2\\rest_10_s\\"

    for d in range(6, 8):
        dir_in = SUPER_DIR + f"C001H001S000{d}\\C001H001S000{d}"
        dir_out = SUPER_DIR + f"C001H001S000{d-5}\\C001H001S000{d-5}"

        for i in range(1, 22542):
            os.rename(dir_in + f"{i:06}.bmp", dir_out + f"{i:06}.bmp")

    print("fin.")
