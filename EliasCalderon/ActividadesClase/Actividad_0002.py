class Person:
    pass
Person = [Person() for _ in range(1500)]

for i in range(1, 1501):
    print(f"Objeto {i}")