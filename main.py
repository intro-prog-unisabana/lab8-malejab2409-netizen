"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")
        if len(sys.argv) >= 3:
            file_path = sys.argv[1]
            comando = sys.argv[2]
            tasks = read_todo_file(file_path)
            if comando == "view":
                print("Tasks:")
                for task in tasks:
                    print(task)
            elif comando == "add":
                if len(sys.argv) < 4:
                    raise IndexError('Task description required for "add"')
                nueva_tarea = sys.argv[3]
                tasks.append(nueva_tarea)
                write_todo_file(file_path, tasks)
                print(f'Task "{nueva_tarea}" added.')
            elif comando == "remove":
                if len(sys.argv) < 4:
                    raise IndexError('Task description required for "remove"')
                tarea_a_quitar = sys.argv[3]
                if tarea_a_quitar in tasks:
                    tasks.remove(tarea_a_quitar)
                    write_todo_file(file_path, tasks)
                    print(f'Task "{tarea_a_quitar}" removed.')
                else:
                    print(f'Task "{tarea_a_quitar}" not found.')
            else:
                # Si no es ninguno de los anteriores
                raise ValueError("Command not found!")
    except IndexError as e:
        print(e)
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()