data = open("input.in", "r").read()
l1, l2 = [], []

split = data.strip().split("\n")

for elem in split:
    e1, e2 = map(int, elem.split("   "))
    l1.append(e1)
    l2.append(e2)

l1.sort()
l2.sort()

sum = 0
for e1, e2 in zip(l1, l2):
    sum += abs(e1-e2)

print(f"Summe: {sum}")
w2 = {}

for elem in l2:
    if elem not in w2:
        w2[elem] = 1
    else:
        w2[elem] += 1

score = 0
for elem in l1:
    if elem in w2:
        score += elem * w2[elem]



print(score)
