import re

def insert_spaces(camel_str):
    
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', camel_str)

camel_case_string = input("Enter a CamelCase string: ")

spaced_string = insert_spaces(camel_case_string)

print("Formatted String:", spaced_string)
