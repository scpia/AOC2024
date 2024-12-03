import re

data = open("input.in", "r").read()
mul_pattern = r"mul\((\d+),(\d+)\)"  # Matches valid mul(X,Y)
do_pattern = r"do\(\)"              # Matches do()
dont_pattern = r"don't\(\)"         # Matches don't()

def find_mul_patterns(text):
    pattern = r"mul\((\d+),\s*(\d+)\)"
    matches = re.findall(pattern, text)
    print(matches)
    return [(int(x), int(y)) for x, y in matches]


def solve1(text):
    matches = find_mul_patterns(text)
    return sum([match[0] * match[1] for match in matches ])

def solve2(instruction):

    mul_do_dont_pattern = r"mul\(\d+,\s*\d+\)|do\(\)|don't\(\)"
    matches = re.findall(mul_do_dont_pattern, instruction)

      
    do_include = True
    to_do = []
    for match in matches:
        print(match)
        if match == "do()":
            do_include = True
        elif match == "don't()":
            do_include = False
        else:
            if do_include:
                to_do.append(match)

    total = 0
    for match in to_do:
        pair = match[4:-1].split(',')
        total += int(pair[0]) * int(pair[1])

    return total
print(solve2(data))
