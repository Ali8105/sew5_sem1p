__author__ = "Ali Gürbüz"


def read_labyrinth(file, posX, posY):
    with open(file,"r") as file_read:
        counter = 0
        for line in file_read.readline():
            laby[counter] = line
            counter += 1
    path_search(laby,posX,posY)

def path_search(laby, posX, posY):

    return 0


if __name__ == '__main__':
    laby = []
    file = r"l1.txt"
    read_labyrinth(file,0,0)
