import csv
from datetime import datetime
import os.path


class Note:
    def __init__(self):
        self.title = None
        self.head = None
        self.body = None
        self.creation_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def add_new_data(self):
        self.title = input("Введите имя заметки:\n")
        self.head = input("Введите заголовок заметки:\n")
        self.body = input("Введите тело заметки:\n")
        self.creation_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


class NoteLibrary:
    def __init__(self, reader_api):
        self.notes = []
        if (os.path.exists("notes.csv")):
            with open("notes.csv", "r") as file:
                reader = reader_api(file)
                initial_data = list(reader)
                final_data = []

                for row in initial_data:
                    s = "".join(row)
                    if s:  # Проверяет, не пуста ли строка
                        final_data.append(s)

                for i in range(0, len(final_data), 4):
                    note = Note()
                    note.title = "".join(final_data[i])
                    note.head = "".join(final_data[i + 1])
                    note.body = "".join(final_data[i + 2])
                    note.creation_time = "".join(final_data[i + 3])
                    self.notes.append(note)


