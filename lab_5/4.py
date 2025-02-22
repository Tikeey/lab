import re

with open("example.txt.txt", "r", encoding="utf-8") as file:

    text = file.read()

    listing = re.findall(r"\b\w+\b", text)

    matches = []

    for x in listing:

        pattern = re.search("[A-Z][a-z]+", x) 

        if pattern: 

            matches.append(x)


    print(matches)