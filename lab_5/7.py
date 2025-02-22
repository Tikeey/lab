import re

def snake_to_camel(snake_str):
    
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_str)

snake_case_string = input("Enter a snake_case string: ")


camel_case_string = snake_to_camel(snake_case_string)

print("CamelCase String:", camel_case_string)
