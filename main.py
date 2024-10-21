import json

# Відкриваємо файл
with open('test.json', 'r') as file:
    data = json.load(file)

# Визначаємо тварину і звук
animal_sounds = {
    "dog": "bark",
    "cat": "meow",
    "cow": "moo",
    "rat": "pipi",
    "alien": "KILL"
}

# Перевіряємо на схожість "animal"
animal = data.get('animal')

# Виводимо звук
if animal in animal_sounds:
    print(animal_sounds[animal])
else:
    print("Unknown animal")
