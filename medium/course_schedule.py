from typing import List

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    prereq_dict = {}
    for prereq in prerequisites:
        prereq_dict[prereq[0]] = prereq[1]

    first_class = prerequisites[0][1]
    while :
        first_class = prereq_dict[first_class]

    return first_class 


num_courses = 4
prereqs = [[1,0], [3,2], [0,3]]

print(can_finish(num_courses=4, prerequisites=prereqs))
