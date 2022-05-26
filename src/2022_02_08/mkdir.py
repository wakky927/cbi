import os


if __name__ == '__main__':
    path = "E:\\M1\\result\\2022_02_08\\pathline\\"

    for i in range(1, 50):
        os.mkdir(path + f'_{i}')

    print(0)
