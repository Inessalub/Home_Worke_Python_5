# Задача №38:
# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = input("Введите текст через пробел:\n")
print(f"Исходный текст: {text}")
find = "абв"
list = [i for i in text.split() if find not in i]
print(f'Результат: {" ".join(list)}')