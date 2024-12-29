#urn your empty list into a list comprehension that converts each character in pascal_or_camel_cased_string into a lowercase character and prepends an underscore to it (the code you commented out before may help you write the expression). Use char to iterate over pascal_or_camel_cased_string.

snake_cased_char_list = ['_' + char.lower() for char in pascal_or_camel_cased_string]
