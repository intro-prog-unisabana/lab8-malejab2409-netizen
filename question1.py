"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""
import sys 
if len (sys.argv) != 2:
   newtons = sys.argv[1]
   puntos_soporte  = sys.argv[2]
   load_per_support = newtons / puntos_soporte
try:
    newtons = float(sys.argv[1])
    puntos_soporte  = int(sys.argv[2])
    load_per_support = newtons / puntos_soporte
