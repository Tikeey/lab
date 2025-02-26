my_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

with open("dir-and-files/text.txt", "w", encoding="utf-8") as file:

    for item in my_list:

        file.write(item + "\n")

print("List has been written to text.txt")
