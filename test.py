def interpreter(*args):
    for arg in args:
        with open('interpreter.octo', 'a') as file:
            
            if isinstance(arg, str):  # Check if the argument is a string
                file.write(f'{arg} is a string\n')
            if isinstance(arg, int):
                file.write(f'{arg} is an int\n')
            if isinstance(arg, float):
                file.write(f'{arg} is a float\n')

            
        

# Example usage
interpreter('Hello World', 42, 3.14, 'Python')
