import re

pattern_1 = r"\b[a-z]+_[a-z]+\w*\b"

file_path = "example.txt.txt"

try:

    with open(file_path, "r", encoding="utf-8") as file:

        file_content = file.read()

except FileNotFoundError:

    print(f"Error: The file '{file_path}' was not found.")

    exit()

matches_1 = re.findall(pattern_1, file_content, re.IGNORECASE)

print("\nMatching Strings with that sequences of lowercase letters joined with a underscore: ", matches_1)