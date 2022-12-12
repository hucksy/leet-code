from typing import List

def floodFill(image: List[List[int]], x: int, y: int, color: int) -> List[List[int]]:
    columns = len(image[0])
    rows = len(image)
    match_color = image[x][y]

    def traverse(x: int, y: int):
        if -1 < x < columns and -1 < y < rows and image[x][y] == match_color:
            image[x][y] = color
            traverse(x+1, y)
            traverse(x-1, y)
            traverse(x, y+1)
            traverse(x, y-1)
        else:
            return

    if color != match_color:
        traverse(x, y)

    return image


image = [[1,1,1],[1,1,0],[1,0,1]]
# image = [[0,0,0],[0,0,0]]
sr = 1
sc = 1
color = 2

print(floodFill(image, sr, sc, color))