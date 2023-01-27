section_file = "advent/inputs/day4_sections.txt"

with open(file=section_file, mode="r") as section_data:
    sections = [[section.strip('\n').split(",")[0].split("-"), section.strip('\n').split(",")[1].split("-")] for section in section_data]

overlap_count = 0
for i, section in enumerate(sections):
    if int(section[0][0]) >= int(section[1][0]) and int(section[0][0]) <= int(section[1][1]):
        overlap_count += 1
        print(f"{section[0][0]} >= {section[1][0]} and {section[0][0]} <= {section[1][1]}")
        print(f"i = {i} overlapped: {section}")
    elif int(section[0][1]) >= int(section[1][0]) and int(section[0][1]) <= int(section[1][1]):
        overlap_count += 1
        print(f"{section[0][1]} >= {section[1][0]} and {section[0][1]} <= {section[1][1]}")
        print(f"i = {i} overlapped: {section}")
    elif int(section[1][0]) >= int(section[0][0]) and int(section[1][0]) <= int(section[0][1]):
        overlap_count += 1
        print(f"{section[1][0]} >= {section[0][0]} and {section[1][0]} <= {section[0][1]}")
        print(f"i = {i} overlapped: {section}")
    elif int(section[1][1]) >= int(section[0][0]) and int(section[1][1]) <= int(section[0][1]):
        overlap_count += 1
        print(f"{section[1][1]} >= {section[0][0]} and {section[1][1]} <= {section[0][1]}")
        print(f"i = {i} overlapped: {section}")

print(f"overlap count = {overlap_count}")

#876