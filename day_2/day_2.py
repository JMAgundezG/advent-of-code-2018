import sys

# DAY 2

# Part 1
if len(sys.argv) < 2:
    print("i need an input file")
    exit(1)
else:
    all_strings = open(sys.argv[1], 'r').readlines()
all_strings = [i[:-1] if i[-1] == '\n' else i for i in all_strings]
twice = 0
three = 0
for i in all_strings:
    flag_2 = flag_3 = False
    for a in set(i):
        times = i.count(a)
        if times == 2 and not flag_2:
            twice += 1
            flag_2 = True
        if times == 3 and not flag_3:
            three += 1
            flag_3 = True
        
print("[PART 1] ", twice * three)

# Part 2        

solution = []
for i in range(len(all_strings)):
    for j in range(i, len(all_strings)):
        count = 0
        for k in range(len(all_strings[i])):
            if all_strings[i][k] != all_strings[j][k]:
                count+= 1
        if count == 1:
            solution.extend([all_strings[i], all_strings[j]])

final_ = ""
for i in range(len(solution[0])):
    if solution[0][i] == solution[1][i]:
        final_ += solution[0][i]

print(final_)