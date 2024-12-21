import sys
import pprint


def introspection_info(obj):
    print('Тип: ', type(obj))
    print('Аттрибуты:  ', [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")])
    print('Методы: ', [attr for attr in dir(obj) if callable(getattr(obj, attr)) and not attr.startswith("__")])
    print('Модуль: ', obj.__class__.__module__)
    print('Класс: ', obj.__class__.__name__)



introspection_info(42)
