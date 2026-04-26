"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file, write_todo_file
def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")
        print("Command-line arguments:")
        for arg in sys.argv[1:]:
            print(arg)
        file_path = sys.argv[1]
        tasks = read_todo_file(file_path)
        print("Tasks:")
        for task in tasks:
            print(task)
    except IndexError as f:
        print(f)
if __name__ == "__main__":
    main()