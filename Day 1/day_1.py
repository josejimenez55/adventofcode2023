lines = open('day_1_input.txt', 'r')
sum = 0
for line in lines:
    digits = []
    for n in line:
        if n.isnumeric():
            digits.append(int(n))

    sum += 10 * digits[0] + digits[-1]

print(sum)