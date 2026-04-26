"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""
import sys 
def main():
   try:
    if len (sys.argv) != 3:
        print("Error: Invalid input! Enter numeric values only.")
        return 
    newtons = float(sys.argv[1])
    puntos_de_soporte = float(sys.argv[2])
    if puntos_de_soporte == 0:
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
        return
    load_per_support = newtons / puntos_de_soporte
    print(f"Load per support point: {load_per_support:.2f} N")
   except ValueError:
    print("Error: Invalid input! Enter numeric values only.")
   except:
        print("Error: Invalid input! Enter numeric values only.")
if __name__ == "__main__":
    main()