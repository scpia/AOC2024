def checkConstraints(x, y):
    return not (1 <= abs(int(y) - int(x)) <= 3)


def create_subsets(input_list):
    return [input_list[:i] + input_list[i + 1:] for i in range(len(input_list))]


def is_safe(line):
    asc = des = False
    for i in range(1, len(line)):
        if int(line[i]) < int(line[i - 1]):
            if des or checkConstraints(line[i - 1], line[i]):
                return False
            asc = True
        elif int(line[i]) > int(line[i - 1]):
            if asc or checkConstraints(line[i - 1], line[i]):
                return False
            des = True
    return True


def solve2(nums):
    safelines = 0
    for line in nums:
        if is_safe(line):  # Check if the line is safe as is
            safelines += 1
            continue

        # Check if removing one level makes the line safe
        print(list(is_safe(line) for line in create_subsets(line)),)
        if any(is_safe(line) for line in create_subsets(line)):
            safelines += 1
            break
    return safelines


# Example usage
data = open("test.in", "r").read()
raw = data.strip().split("\n")
numbers = [line.split(" ") for line in raw]

print(solve2(numbers))
