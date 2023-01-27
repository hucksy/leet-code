
rps_file = "advent/inputs/day2_rps.txt"
with open(file=rps_file, mode="r") as rps_data:
    lines = [line.rstrip("\n") for line in rps_data]

print(lines)

"""x = lose, y = draw, z = win"""
score = 0
round_dict = {
    'A X':3,
    'A Y':4,
    'A Z':8,
    'B X':1,
    'B Y':5,
    'B Z':9,
    'C X':2,
    'C Y':6,
    'C Z':7
}

for line in lines:
    score += round_dict[line]

print(score)    