elf_filename = "advent/elf_food.txt"

# with open(elf_filename) as elf_file:
#     lines = [line.rstrip('\n') for line in elf_file]


gen_reader = (row.rstrip('\n') for row in open(elf_filename))

max_calories = 0
cur_calories = 0
cal_list = []
for row in gen_reader:
    if row == '':
        cal_list.append(cur_calories)
        cur_calories = 0
    else:
        cur_calories += int(row)

cal_list.sort(reverse=True)
print(cal_list)
print(sum(cal_list[0:3]))
