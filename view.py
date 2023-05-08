class SimpleFormatter:
    def __init__(self, title, head, body, creation_time):
        print(f"Имя файла: '{title}'\n")
        print(head + "\n")
        print(body + "\n")
        print(f"Создано/изменено {creation_time}\n")
