with open("dir-and-files/sample.txt", "r", encoding="utf-8") as file:

    num_lines = sum(1 for line in file)

print("Total number of lines:", num_lines)
