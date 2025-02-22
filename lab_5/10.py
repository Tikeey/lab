import re

def camel_to_snake(camel_str):

    snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str)
    
    return snake_str.lower()


camel_case_string = input("Enter a camelCase string: ")

snake_case_string = camel_to_snake(camel_case_string)

print("Snake Case String:", snake_case_string)
