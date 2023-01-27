rucksack_file = "advent/inputs/day3_rucksack.txt"

with open(file=rucksack_file, mode="r") as ruck_data:
    ruck_list = [line.rstrip('\n') for line in ruck_data]

ruck_value_dict = {
'a':1,
'b':2,
'c':3,
'd':4,
'e':5,
'f':6,
'g':7,
'h':8,
'I':9,
'j':10,
'k':11,
'l':12,
'm':13,
'n':14,
'o':15,
'p':16,
'q':17,
'r':18,
's':19,
't':20,
'u':21,
'v':22,
'w':23,
'x':24,
'y':25,
'z':26,
'A':27,
'B':28,
'C':29,
'D':30,
'E':31,
'F':32,
'G':33,
'H':34,
'I':35,
'J':36,
'K':37,
'L':38,
'M':39,
'N':40,
'O':41,
'P':42,
'Q':43,
'R':44,
'S':45,
'T':46,
'U':47,
'V':48,
'W':49,
'X':50,
'Y':51,
'Z':52
}
score = 0
for ruck in ruck_list:
    ruck_size = len(ruck)
    ruck_mid = int(ruck_size/2)
    comp1 = ruck[0:ruck_mid]
    comp2 = ruck[ruck_mid:ruck_size]
    # print(f"ruck = {ruck}  comp1 = {comp1}  comp2 = {comp2}")
    for letter in comp1:
        if letter in comp2:
            # print(f"letter = {letter}")
            score += ruck_value_dict[letter]
            break
# print(score)

group = []
badge_sum = 0
for i, ruck in enumerate(ruck_list):
    group.append(ruck)
    if i > 0 and (i+1) % 3 == 0:
        print(f"group = {group}")
        for letter in group[0]:
            if letter in group[1] and letter in group[2]:
                print(f"letter = {letter}")
                badge_sum += ruck_value_dict[letter]
                break
        group.clear()

print(badge_sum)