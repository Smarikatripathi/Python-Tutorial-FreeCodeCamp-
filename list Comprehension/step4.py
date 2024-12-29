#Inside the for loop, add an if statement to check if the current character is uppercase. Move the pass statement inside the new if statement.

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
           pass