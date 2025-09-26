from pathlib import Path

def walk_dir(path):
    result = []
    base_path = Path(path)

    for name in base_path.rglob('*'):  # рекурсивно ищем
        full_path = name  # full_path объект Path
        if full_path.is_file():  # проверка, что это файл
            size = full_path.stat().st_size  # размер файла
            mode = oct(full_path.stat().st_mode)[-3:]  # права доступа
            result.append((str(full_path), size, mode))  # добавляем в список

    return result

path = input("Введите путь к папке: ")
files = walk_dir(path)

for f in files:
    print(f)
