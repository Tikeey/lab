import re

def split_at_uppercase(text):
    
    return re.split(r'(?=[A-Z])', text)

camel_case_string = input("Enter a CamelCase string: ")

split_words = split_at_uppercase(camel_case_string)

print("Split Words:", split_words)
