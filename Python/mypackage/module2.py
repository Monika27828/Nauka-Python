# from module1 import function_a
#
# def function_b():
#     print("Funkcja b z modułu 2")
#     function_a()  # Wywołanie funkcji z modułu B
# if __name__ == "__main__":
#     function_a()

from .config import get_option

def function_in_module2():
    print(f"Opcja w module 2: {get_option('option_2')}")