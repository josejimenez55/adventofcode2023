numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
lines = open('day_1_input.txt', 'r')
sum = 0
for line in lines:
    digits = []
    for i in range(len(line)):
        if line[i].isnumeric():
            digits.append(int(line[i]))
        else:
            for num_numeric, num_text in enumerate(numbers):
                if line[i:].find(num_text, 0, len(num_text)) > -1:
                    # print(line[i:])
                    digits.append(num_numeric)

    sum += 10 * digits[0] + digits[-1]
    # print(digits)

print(sum)