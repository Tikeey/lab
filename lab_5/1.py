import re

pattern_1 = r"\b[aA]b*\w*\b"

pattern_2 = r"\b[aA]\w*\b"

pattern_3 = r"\b[bB]\w*\b"

file_path = "example.txt.txt"

try:

    with open(file_path, "r", encoding="utf-8") as file:

        file_content = file.read()

except FileNotFoundError:

    print(f"Error: The file '{file_path}' was not found.")

    exit()

matches_1 = re.findall(pattern_1, file_content, re.IGNORECASE)

matches_2 = re.findall(pattern_2, file_content, re.IGNORECASE)

matches_3 = re.findall(pattern_3, file_content, re.IGNORECASE)

print("\nMatching Strings with that has an 'a' followed by zero or more 'b''s: ", matches_1,"\n", "\nMatching Strings with that has an 'a' int the begin: ", matches_2, "\n", "\nMatching Strings with that has an 'b' in the begin: ", matches_3, "\n")
