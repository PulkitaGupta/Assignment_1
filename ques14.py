def read_lines_until_empty():
    lines = []
    while True:
        line = input("Enter a line (leave empty to finish): ")
        if line == "":
            break
        lines.append(line)
    return lines

lines = read_lines_until_empty()
print("Lines entered:")
for line in lines:
    print(line)
