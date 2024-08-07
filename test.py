def interpreter(*args):
    for arg in args:
        with open('interpreter.octo', 'a') as file:
            
            if isinstance(arg, str):  # Check if the argument is a string
                file.write(f'{arg} is a string\n')
            if isinstance(arg, int):
                file.write(f'{arg} is an int\n')
            if isinstance(arg, float):
                file.write(f'{arg} is a float\n')

def readFile(path):

    if path.endswith('.octo'): #checks if the file is in octo format

        with open(path, 'r') as file:
            data = file.read() #reads the file
            print(f"Fetched data: {data}") #prints the data
            for index, line in enumerate(data.split('\n'), start=1):
                print(f"Line {index}: {line.strip()}")
        
    else:
        print("Invalid file format") #prints an error message if the file is not in octo format

# Example usage
interpreter('Hello World', 42, 2, 'Python')
readFile('interpreter.octo')
