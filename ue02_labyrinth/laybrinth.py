__author__ = "Ali Gürbüz"

import argparse


def read_labyrinth(file, posX, posY):
    laby = []
    with open(file,"r") as file_read:
        for line in file_read:
            laby.append(list(line.strip()))
    path_search(laby,posX,posY)

def path_search(laby, posX, posY):
    if posX < 0 or posY < 0 or posX > len(laby)-1 or posY > len(laby[0])-1:
        return 0
    elif laby[posX][posY] == 'A':
        print_path(laby)
    else:
        laby[posX][posY] = '*'
        if laby[posX+1][posY] == ' ' or laby[posX+1][posY] == 'A':
            path_search(laby,posX+1,posY)
        if laby[posX][posY+1] == ' ' or laby[posX][posY+1] == 'A':
            path_search(laby,posX,posY+1)
        if laby[posX-1][posY] == ' ' or laby[posX-1][posY] == 'A':
            path_search(laby,posX-1,posY)
        if laby[posX][posY-1] == ' ' or  laby[posX][posY-1] == 'A':
            path_search(laby,posX,posY-1)

def print_path(laby):
    print('---------------------------------')
    for i in laby:
        print(i)
    print('---------------------------------')


def parse_arguments():
    parser = argparse.ArgumentParser(description="die Wege")
    parser.add_argument("filename", help="File containing the labyrinth to solve")
    parser.add_argument("-x", "--xstart", type=int, help="X-coordinate to start")
    parser.add_argument("-y", "--ystart", type=int, help="Y-coordinate to start")
    return parser.parse_args()

if __name__ == '__main__':
    file = r"l3.txt"
    read_labyrinth(file,0,5)

