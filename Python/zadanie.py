import time

# Generator zwracający liczby podzielne przez 3
def divisible_by_three_gen(n):
    for i in range(n):
        if i % 3 == 0:
            yield i

# Funkcja zwracająca listę liczb podzielnych przez 3
def divisible_by_three_list(n):
    return [i for i in range(n) if i % 3 == 0]

# Test generatora (yield)
start_time = time.time()
for _ in divisible_by_three_gen(10_000_000):  # Iterujemy przez generator
    pass
end_time = time.time()
print(f"Generator (yield) - czas działania: {end_time - start_time:.6f} sekundy")

# Test zwracania listy (return)
start_time = time.time()
for _ in divisible_by_three_list(10_000_000):  # Iterujemy przez listę
    pass
end_time = time.time()
print(f"Zwykła funkcja (return) - czas działania: {end_time - start_time:.6f} sekundy")
