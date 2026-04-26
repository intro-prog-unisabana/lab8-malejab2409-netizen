"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file, write_todo_file
def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")
        if len(sys.argv) >= 3:
            comando = sys.argv[2]
            file_path = sys.argv[1]
            if comando == "view":
                tasks = read_todo_file(file_path)
                print("Tasks:")
                for task in tasks:
                    print(task)
            else:
                raise ValueError("Command not found!")
    except IndexError as f:
        print(f)
    except ValueError as f:
        print(f)
if __name__ == "__main__":
    main()