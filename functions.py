FILEPATH = "venv/Scripts/todos.txt"

def get_todos(filepath=FILEPATH):

    """reads a text file and returns the
    list of to-do list items
    """

    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_argument, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_argument)