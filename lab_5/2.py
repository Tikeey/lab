import re

pattern_1 = r"\b[aA]bb{1,2}\w*\b"

file_path = "example.txt.txt"

try:

    with open(file_path, "r", encoding="utf-8") as file:

        file_content = file.read()

except FileNotFoundError:

    print(f"Error: The file '{file_path}' was not found.")

    exit()

matches_1 = re.findall(pattern_1, file_content, re.IGNORECASE)

print("\nMatching Strings with that has an 'a' followed by two to three 'b''s: ", matches_1)