FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """Reads a test file line by line and returns it as a list"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Receives a list and writes it to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#print(__name__)
if __name__ == "__main__":
    print("functions.py loaded")
    print(get_todos())