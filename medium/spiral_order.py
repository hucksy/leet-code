from typing import List

def spiral_order(matrix: List[List[int]]) -> List[int]:
    visited = [matrix[0][0]]
    direction = 1
    row = 0
    col = 0

    
    def check_direction(col: int, row: int, dir: int):
        if direction % 4 == 1:
            walled = check_wall(col+1,row, dir)
        elif direction % 4 == 2:
            walled = check_wall(col,row+1, dir)
        elif direction % 4 == 3:
            walled = check_wall(col-1,row, dir)
        elif direction % 4 == 0:
            walled = check_wall(col,row-1, dir) 

        visited = False
        if not walled:
            visited = check_visited(col,row)
        if visited and walled:
            return -1
        elif visited or walled:
           breakpoint()
           dir += 1

        return dir



    def check_wall(col: int, row: int, dir):
        if col == len(matrix[0]) or col < 0 or row == len(matrix) or row < 0:
            return True
        else:
            return False

    def check_visited(col: int, row: int):
        if matrix[row][col] in visited:
            return True
        else: 
            return False


# travel conditions:
    while direction:
        direction = check_direction(col, row, direction)
        if direction % 4 == 1: # right
            col += 1
            visited.append(matrix[row][col])
        if direction % 4 == 2: #(down)
            row += 1
            visited.append(matrix[row][col])
        if direction % 4 == 3:  # (left)
            col -= 1
            visited.append(matrix[row][col])
        if direction % 4 == 0:  # up
            row -= 1
            visited.append(matrix[row][col])

    


test1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
test2 = [[1,2,3],[4,5,6],[7,8,9]]

print(spiral_order(test1))