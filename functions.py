
def get_todos(file_name='textFile.txt'):
    with open(file_name, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def file_dump(todos_l, file_name='textFile.txt'):
    with open(file_name, 'w') as file:
        file.writelines(todos_l)
