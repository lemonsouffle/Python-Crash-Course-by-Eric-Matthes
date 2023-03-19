# Изменение, добавление и удаление элементов

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop()
print("The first motorcycle I owned was a " + first_owned.title() + ".")

print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'ktm', 'ducati']
print(motorcycles)
too_expensive = 'ktm'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.upper() + " is too expensive for me.")