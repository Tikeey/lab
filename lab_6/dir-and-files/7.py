with open("dir-and-files/text.txt", "r", encoding="utf-8") as source_file, open("test.txt", "w", encoding="utf-8") as dest_file:

    dest_file.write(source_file.read())

print("File contents copied successfully from text.txt to test.txt.")
