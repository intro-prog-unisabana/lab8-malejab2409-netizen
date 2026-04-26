"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")
        if sys.argv[1] == "--help":
            print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
            return
        file_path = sys.argv[1]
        tasks = read_todo_file(file_path)
        i = 2
        cambios_realizados = False
        while i < len(sys.argv):
            comando = sys.argv[i]
            if comando == "wiew":
                    print("Tasks:")
                    for task in tasks:
                        print(task)
                    i += 1
            elif comando == "--add":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "add".')
                nueva_tarea = sys.argv[i + 1]
                tasks.append(nueva_tarea)
                print(f'Task "{nueva_tarea}" added.')
                cambios_realizados = True
                i += 2
            elif comando == "remove":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "remove".')    
                tarea_a_quitar = sys.argv[i + 1]
                if tarea_a_quitar in tasks:
                    tasks.remove(tarea_a_quitar)
                    print(f'Task "{tarea_a_quitar}" removed.')
                    cambios_realizados = True
                else:
                    print(f'Task "{tarea_a_quitar}" not found.')
                i += 2
            else:
                raise ValueError("Command not found!")
        if cambios_realizados:
            write_todo_file(file_path, tasks)
    except IndexError as f:
        print(f)
    except ValueError as f:
        print(f)
if __name__ == "__main__":
    main()  