__author__ = "Ali Gürbüz"


def read_labyrinth(file, posX, posY):
    laby = []
    with open(file,"r") as file_read:
        for line in file_read:
            laby.append(list(line.strip()))
    path_search(laby,posX,posY)

def path_search(laby, posX, posY):
    # Rekursion Break-out
    if posX < 0 or posY < 0:
        raise Exception("Ware fast index out of bounds")
    elif posX >= len(laby)-1 or posY >= len(laby[0])-1:
        print_path(laby)
    else:
        laby[posX][posY] = '*'
        if laby[posX+1][posY] == ' ':
            path_search(laby,posX+1,posY)
        if laby[posX][posY+1] == ' ':
            path_search(laby,posX,posY+1)
        if laby[posX-1][posY] == ' ':
            path_search(laby,posX-1,posY)
        if laby[posX][posY-1] == ' ':
            path_search(laby,posX,posY-1)
        print_path(laby)
        
def print_path(laby):
    print('---------------------------------')
    for i in laby:
        print(i)
    print('---------------------------------')

if __name__ == '__main__':
    file = r"l1.txt"
    read_labyrinth(file,0,6)

