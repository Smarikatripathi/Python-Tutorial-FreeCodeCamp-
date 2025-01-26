#Finally, put the last two lines of your code inside an if statement that execute when __name__ == '__main__'. In this way, your code won't run when imported as a module. Otherwise, it will call generate_password() and print the generated password.

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)