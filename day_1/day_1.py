import sys
import itertools
# DAY 1
# Part 1
print("[PART 1]")
if len(sys.argv) < 2:
    print("i need an input file")
    exit(1)
else:
    file = sys.argv[1]

all_input = open(file,'r').readlines()
all_numbers = [int(i) for i in all_input[:-1]]
print(sum(all_numbers))

# Part 2
print("[PART 2]")
current_value = 0
l = {0: 1}
cycle_numbers = itertools.cycle(all_numbers)
for i in cycle_numbers:
    current_value += i
    if current_value not in l.keys():
        l[current_value] = 1
    else:
        print(current_value)
        break
