__author__ = "Ali Gürbüz"


def read_labyrinth(file):
    with open(file,"r") as file_read:
        counter = 0
        for line in file_read.readline():
            laby[counter] = line
            counter += 1
    rec_solve(laby)

def rec_solve(laby):
    return 0


if __name__ == '__main__':
    laby = []
    file = r"l1.txt"
