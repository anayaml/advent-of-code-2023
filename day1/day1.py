def part2(src):
    valid = [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine",
    ]
    total_sum = 0

    for line in src.splitlines():
        if line.strip():  # Check if the line is not empty
            digits = []
            for i, pattern in enumerate(valid):
                start = 0
                while True:
                    pos = line[start:].find(pattern)
                    if pos == -1:
                        break
                    digits.append(((i % 9) + 1, start + pos))
                    start += pos + len(pattern)
            digits.sort(key=lambda x: x[1])
            result = digits[0][0] * 10 + digits[-1][0]
            print(f"{result}")
            total_sum += result
    print(total_sum)

part2(open("input.txt").read())