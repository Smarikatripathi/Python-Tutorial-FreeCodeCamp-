#Modify the return statement by chaining to ''.join(snake_cased_char_list) a call to the .strip() method to remove any leading or trailing underscores.

return ''.join(snake_cased_char_list).strip('_')