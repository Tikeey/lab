import re

with open("example.txt.txt", "r", encoding="utf-8") as file:
    text = file.read()

    listing = re.findall(r"\b\w+\b", text)

    matches = []

    for x in listing:
        pattern = re.search(r"^.+[aAbB]$", x)
        
        if pattern:

            matches.append(x)

    print(matches)
