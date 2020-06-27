import os
import random

folder_path = "./files_to_corrupt"


def file_corruption():
    for filename in os.listdir(folder_path):
        file = open("files_to_corrupt/" + filename, "rb")
        byte = bytearray(file.read())

        i = 0
        while i < 200:
            num = random.randint(0, len(byte))
            num1 = random.randint(0, 255)
            byte[num] = num1
            i = i+1
        f = open("files_to_corrupt/CORRUPTED_" + filename, "wb")
        f.write(byte)
        f.close()


def folder_check():
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


if __name__ == "__main__":
    folder_check()
    file_corruption()
    print("DONE!!!")
