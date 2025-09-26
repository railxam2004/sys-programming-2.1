import os

def walk_dir(path):
    result = []
    for name in os.listdir(path):
        full_path = os.path.join(path, name)  # полный путь к файлу
        if os.path.isfile(full_path):  # если это файл
            size = os.path.getsize(full_path)  # размер файла
            mode = oct(os.stat(full_path).st_mode)[-3:]  # права доступа
            result.append((full_path, size, mode))
        elif os.path.isdir(full_path):  # если это папка
            result.extend(walk_dir(full_path))  # рекурсивный обход
    return result

path = input("Введите путь к папке: ")

files = walk_dir(path)

for f in files:
    print(f)
