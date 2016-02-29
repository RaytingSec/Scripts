codes_long=["11110", "01001", "10100", "10101", "01010", "01011", "01110", "01111", "10010", "10011", "10110", "10111", "11010", "11011", "11100", "11101"]
# codes_short=["11110", "01001", "10100", "10101"]
progression = 1

for code1 in codes_long:
    row = []
    for x in range(0, progression):
        row.append(' ')
    for code2 in codes_long[progression:]:
        xored = bin(int(code1, 2) ^ int(code2, 2))
        row.append(xored.count("1"))
    print(''.join([str(distance)+',' for distance in row]))
    progression += 1

# 11110 01110 1