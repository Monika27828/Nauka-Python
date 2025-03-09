# def auto_register():
#     from . import module1, module2
#     module1.register()
#     module2.register()

# print('Pakiet mypackage załadowany')


from .config import set_option, get_option
from .module1 import function_in_module1
from .module2 import function_in_module2

__all__ = ['set_option', 'get_option', 'function_in_module1', 'function_in_module2']
print('pakiet załadowany')