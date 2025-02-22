import re

with open("example.txt.txt", "r", encoding="utf-8") as file:
    text = file.read()

    modified_text = re.sub(r"[ ,.]", ":", text)

print(modified_text)
