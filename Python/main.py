# Zadanie 1.
# from math import factorial
#
# def dynamic_import(module_name, function_name):
#     try:
#         module = __import__(module_name)
#         if hasattr(module, function_name):
#             return getattr(module, function_name)
#         else:
#             raise AttributeError('Moduł nie zawiera tej funkcji')
#     except ImportError:
#         raise AttributeError('Moduł nie został znaleziony')
#
# factorial_fun = dynamic_import('math', 'factorial')
# print(factorial_fun(5))
import sys

from numpy import astype
from pandas.core.interchange.dataframe_protocol import DataFrame

# Zadanie 2.
# import dynamic_module
#
# def subtract(a, b):
#     return a - b
#
# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError('Nie dziel przez 0')
#     return a / b
#
# setattr(dynamic_module, 'subtract', subtract)
# setattr(dynamic_module, 'divide', divide)
#
# def new_add(a, b):
#     return a + b + b
#
# setattr(dynamic_module, 'add', new_add)
#
# print(dynamic_module.add(10, 5))
# print(dynamic_module.divide(10, 5))

#Zadanie 3.
# import versioned_module
# add_func = versioned_module.load_version(1)
# print(add_func(5,3))
#
# add_func = versioned_module.load_version(2)
# print(add_func(5,3))
#
# add_func = versioned_module.load_version(3)
# print(add_func(5,3))

#Zadanie 4.

# import mypackage
#
# mypackage.auto_register()

# from mypackage.module1 import function_a
#
# function_a()

# from mypackage import config
# from mypackage.module1 import function_in_module1
# from mypackage.module2 import function_in_module2
#
# function_in_module1()
# function_in_module2()
#
# config.set_option('option_1', False)
# config.set_option('option_2', 50)
#
# function_in_module1()
# function_in_module2


# Zadanie. Pandas i DataFrame/ Heart disease

import pandas as pd

data = pd.read_csv("HeartDisease.txt")

# print(data.head()) # Podgląd kilku pierwszych wierszy
# print(data.info()) # Wyświetlamy informacje o kolumnach
# print('Rozmiar danych:', data.shape) # Wyświetlamy rozmiar danych np. że mamy 462 wiersze i 11 kolumn
# print(data.describe())  # Pandas liczy podstawowe statystyki
# print(data.isnull().sum()) # zlicza wszystkie wiersze, w których jest wartość 'null'
# data = data.drop(columns=['row.names']) # usuwa konkretne kolumny
# print(data.head())
# data = data.astype(str)
# data.fillna("5", inplace=True)
# print(data.isnull().sum())
#
# columns_of_interest = ['sbp', 'alcohol', 'ldl', 'chd']
# print(data[columns_of_interest].head())
#
# print(data[data['chd'] == '1.0'].head()) # filtrowanie osób z chorobą serca
#
# print(data.sort_values(by=['age'], ascending=False).head()) # sortowanie po wieku
#
# data['obesity'] = data['obesity'].astype(float)
# data['bmi_scaled'] = data['obesity'] / 10
# data['bmi_scaled'] = data['bmi_scaled'].round(3) # zaokrąglamy do 3 m-c po przecinku
# data['bmi_scaled'] = data['bmi_scaled'].astype(str)
# print(data.head())

# szukanie korelacji między zmiennymi - macierz korelacji:

# data['famhist_encoded'] = data['famhist'].map({'Present': 1, 'Absent': 0})
# data = data.drop(columns=['famhist'])
# correlation_matrix = data.corr()
# print(correlation_matrix)
#
# grouped = data.groupby('chd')['sbp'].mean()
# print(grouped)
# import matplotlib.pyplot as plt
# data['sbp'].hist()
# plt.show() # pokazuje wykres
#
# # normalizacja:
# # 1 4 6 8
# # (xi - min) / (max - min)
# # 0, 3/7, 5/7, 1
#
# data['tobacco_normalized'] = (data['tobacco'] - data['tobacco'].mean()) / data['tobacco'].std() # jednak to był wzór na standaryzację danych
# print(data.head())
#
# data['age_group'] = pd.cut(data['age'], bins=[0,30,50,70,100], labels=['Young', 'Middle-age', 'Senior', 'Elderly'])
# age_group_summary = data.groupby('age_group')[['sbp', 'ldl']].mean()
# print(age_group_summary)
#
# import seaborn as sns
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm' )
# plt.show()

# 17.01.2025

# import os
# import sys
# from datetime import datetime
#
# current_directory = os.getcwd()
# print(current_directory)
#
# new_folder = 'nowy_katalog'
# # os.mkdir(new_folder)
#
# if os.path.exists(new_folder):
#     print('istnieje')
#     os.rmdir(new_folder)
#     #os.rmdir(new_folder)
#
# files = os.listdir(r'C:\Users\mpsch\PycharmProjects\pythonProject\Python')
# print(files)
#
# os.system('echo "Hello World"')
#
# print('Argumenty wiersza poleceń: ', sys.argv)

# if len(sys.argv) < 2:
#     print('Brak wystarczającej liczby argumentów!')
#     sys.exit()

# print(sys.version)
#
# sys.stdout.write('To jest przykładowy tekst stdout\n')
# sys.stderr.write('To jest przykładowy błąd do stdeerr\n')
#
# now = datetime.now()
# print(now)
# specific_date = datetime(2025, 1, 12, 20, 30, 40)
# print(specific_date)
#
# formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
# print(formatted_date)
#
# from datetime import timedelta
#
# delta = timedelta(days=7)
# future_date = now + delta
# print(f'Data za 7 dni: {future_date}')
#
# if now > datetime(2025, 1, 15):
#     print('Bieżąca data jest późniejsza niż 15 stycznia 2025')
#
# from collections import Counter
#
# words = ['apple', 'banana', 'orange', 'apple', 'banana', 'orange','apple', 'banana', 'apple']
# word_count = Counter(words)
# print(word_count)
#
# from collections import defaultdict
#
# default_dict = defaultdict(int)
# numbers = [1, 2, 2, 2, 3, 3, 3, 3]
# for number in numbers:
#     default_dict[number] += 1
# print(default_dict)
#
# from collections import deque
#
# queue = deque(['a', 'b', 'c'])
# queue.append('d')
# queue.appendleft('z')
# print(queue)
# queue.pop()
# queue.popleft()
# print(queue)
#
# dict = {'a': 5, 'b': 2, 'c': 6}
# print(dict)
#
# from collections import OrderedDict
#
# ordered_dict = OrderedDict()
# ordered_dict['first'] = 1
# ordered_dict['second'] = 4
# ordered_dict['third'] = 3
#
# print(ordered_dict)
#
# from collections import namedtuple
#
# Point = namedtuple('Point', ('x', 'y'))
# p = Point(10, 20)
# print(p.x, p.y) # lub samo p w nawiasie
#
# # Zadanie 1. Napisz skrypt, który:
# # Wykorzysta Counter do policzenia liczby wystąpień każdego znaku w podanym łańcuchu.
# # Wyświetl wyniki w postaci uporządkowanej malejąco wg liczby wystąpień.
#
# zdanie = 'Choinko ma, choinko ma, tak śliczne masz gałązki.'
# zdanie_Counter = Counter(zdanie)
# print(zdanie_Counter)
# new_counter = sorted(zdanie_Counter.items(), key=lambda x: x[1], reverse=True)
# print(new_counter)

# Zadanie 2. Utwórz program, który:
# Grupuje słowa według ich długości (np. wszystkie słowa o tej samej długości w jednej grupie).
# Wyświetla wyniki w formacie: "Długość: [lista_słów].

# Przykładowa lista słów
# slowa = ["apple", "banana", "kiwi", "orange", "grape", "pear", "melon", "plum"]
#
# # Tworzymy słownik, który przechowa listy słów dla każdej długości
# grupy_dlugi = defaultdict(list)
#
# # Grupowanie słów według długości
# for slowo in slowa:
#     grupy_dlugi[len(slowo)].append(slowo)
#
# # Wyświetlanie wyników
# for dlugosc, slowa_group in sorted(grupy_dlugi.items()):
#     print(f"Długość {dlugosc}: {slowa_group}")

# import shutil
#
# shutil.copy('plik.txt', 'kopia_plik.txt')
# shutil.copy2('plik.txt', 'kopia_plik_1.txt')
#
# shutil.move('kopia_plik.txt', 'dane\\kopia_plik.txt')
#
# shutil.make_archive('backup', 'zip', 'dane')
#
# import glob
#
# text_files = glob.glob('**/*.py', recursive=True)
# print(text_files)
#
# if glob.glob('*.txt'):
#     print('Znaleziono plik .txt')
# else:
#     print('Brak plików .txt')
#
# import csv
#
# with open('pressure.csv', 'r') as file:
#     reader = csv.reader(file, delimiter = ';')
#     for row in reader:
#         print(row)
#
# with open('dane.cvs', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Imię', 'Wiek', 'Miasto'])
#     writer.writerow(['Anna', '20', 'Gdańsk'])
#     writer.writerow(['Joanna', '21', 'Gdynia'])
#     writer.writerow(['Mateusz', '22', 'Sopot'])
#
# with open('dane.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['Imię'], row['Wiek'])

# import json
#
# data = {'name' : 'Anna', 'age' : 25, 'city' : 'Gdansk'}
# data_json = json.dumps(data)
# print(data_json)
#
# with open ('data.json', 'w') as file:
#     json.dump(data, file)
#
# with open ('data.json', 'r') as file:
#     loaded_data = json.load(file)
#     print(loaded_data)
#
# json_string = '{"name" : "Anna", "age" : 25, "city" : "Gdansk"}'
# dara_from_string = json.loads(json_string)
# print(dara_from_string)
#
# nested_data = {
#     'person' : {"name" : "Ewa", "age" : 35},
#     'city' : "Opole",
#     'skills' : ["Python", "SQL", "JAVA"]
# }
# print(json.dumps(nested_data, indent=4))


# import threading
# import time

# def worker(name, delay):
#     for i in range(5):
#         time.sleep(delay)
#         print(f'Watek {name}: iteracja {i}')
#
# thread1 = threading.Thread(target=worker, args=('A', 1))
# thread2 = threading.Thread(target=worker, args=('B', 2))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
# print('Wszystkie wątki zakończone')
#
# # Synchronizacja wątków
#
# lock = threading.Lock()
#
# def safe_worker(name,counter):
#     with lock:
#         print(f'Wątek {name} uzyskał blokadę')
#         time.sleep(1)
#         print(f'Wątek {name} zwalnia blokadę')
#
# threads = [threading.Thread(target=safe_worker, args=(f'Thread--{i}', i)) for i in range(3)]
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()

# from multiprocessing import Process
# import time
#
# def worker(name):
#     print(f'Proces {name} rozpoczęty')
#     time.sleep(1)
#     print(f'Proces {name} zakończony')
#
# process1 = Process(target=worker, args=('A',))
# process2 = Process(target=worker, args=('B',))
#
# process1.start()
# process2.start()
#
# process1.join()
# process2.join()
# print('Wszystkie procesy zakończone')