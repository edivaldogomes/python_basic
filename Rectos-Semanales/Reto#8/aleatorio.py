"""
Crear un generador de números seudoaleatorios entre 1 y 100.
No puedes usar ninguna funcion 'random'(o semejante) del lenguaje de programación  selecionado

"""
import datetime, time as t

def random():
    milseconds = datetime.datetime.now().microsecond % 101
    nano_second = t.time_ns() % 101
    return nano_second


for _ in range(0, 101):
    print(random())