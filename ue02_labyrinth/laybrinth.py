__author__ = "Ali Gürbüz"


def read_labyrinth(file, posX, posY):
    labyrinth = []
    with open(file,"r") as file_read:
        for line in file_read:
            labyrinth.append(line.strip())
    print(labyrinth)

def path_search(laby, posX, posY):

    return 0


if __name__ == '__main__':
    laby = []
    file = r"l1.txt"
    read_labyrinth(file,0,0)
