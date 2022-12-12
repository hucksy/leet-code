from typing import List
from collections import deque

def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    num_rows = len(mat)
    num_cols = len(mat[0])
    new_mat = mat

    def check_inbounds(row: int, col: int):
        if row < num_rows - 1 and row >= 0 and col < num_cols - 1 and col >= 0:
            return True
        else:
            return False


    def search_surrounding(row: int, col: int) -> tuple[int, int]:
        """do a BFS for moving in 4 directions"""
        visited = deque()
        checked = deque()
        visited.append((row,col))
        while visited:
            cur = visited.popleft()
            neighbors= [(cur[0]-1, cur[1]), (cur[0]+1, cur[1]), (cur[0], cur[1]-1), (cur[0], cur[1]+1)]
            for i, val in enumerate(neighbors):
                breakpoint()
                if check_inbounds(val[0], val[1]) and (val[0], val[1]) not in checked:
                    checked.append((val[0], val[1]))
                    if mat[val[0]][val[1]] == 0:
                        return (val[0], val[1])
                    else:
                        visited.append((val[0], val[1]))


    
    for row, val1 in enumerate(mat):
        for col, val2 in enumerate(mat[row]):
            nearest = search_surrounding(row,col)
            new_mat[row][col] = abs(nearest[0]-row) + abs(nearest[1]-col)

            
    return new_mat



test_mat = [[1,1,1],[1,1,0],[1,0,0]]

print(update_matrix(test_mat))