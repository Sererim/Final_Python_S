# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def path(absolute_path: str) -> tuple[str, str, str]:
    file_path: str = ""
    file_name: str = ""
    file_resolution: str = ""
    j = 0

    for i in range(len(absolute_path) - 1, 0, -1):
        if len(file_resolution) == 0 and absolute_path[i] == ".":
            file_resolution = absolute_path[i:]
            j = i
        if len(file_name) == 0 and absolute_path[i] == "\\":
            file_name = absolute_path[i + 1:j]
            file_path = absolute_path[:i]
            break
    return file_path, file_name, file_resolution


if __name__ == "__main__":
    print(path("C:\\Users\\Default\\Pictures\\butterfly.jpg"))
    print(path("C:\\Users\\Default\\AppData\\Local\\something.exe"))

