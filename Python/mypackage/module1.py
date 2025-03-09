# from module2 import function_b
#
# def function_a():
#     print("Funkcja a z modułu 1")
#     function_b()  # Wywołanie funkcji z modułu B
# if __name__ == "__main__":
#     function_b()

from .config import get_option

def function_in_module1():
    print(f"Opcja w module 1: {get_option('option_1')}")