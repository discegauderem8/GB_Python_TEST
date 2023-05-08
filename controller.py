import csv
from datetime import datetime
import model as m


class UserInterface:

    def __init__(self, formatter):
        self.my_library = m.NoteLibrary(
            csv.reader)  # передаем нужный формат чтения, ВЫЗЫВАЕМ его в конструкторе класса)
        self.format = formatter

    def add_note(self):
        note = m.Note()
        note.add_new_data()
        self.my_library.notes.append(note)
        with open("notes.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(f"{note.title}")
            writer.writerow(f"{note.head}")
            writer.writerow(f"{note.body}")
            writer.writerow(f"{note.creation_time}")

    def print_all_notes(self):
        for i in self.my_library.notes:
            self.format(i.title, i.head, i.body, i.creation_time)

    def print_some_notes(self, note_array):
        for item in note_array:
            self.format(item.title, item.head, item.body, item.creation_time)

    def print_single_note(self, note):
        self.format(note.title, note.head, note.body, note.creation_time)

    def find_by_title(self):
        target_title = input("Введите название заметки:\n")
        target_notes = []
        for item in self.my_library.notes:
            if item.title == target_title:
                target_notes.append(item)

        self.print_some_notes(target_notes)

    def find_by_date(self):
        target_date = input("Введите дату и/или время создания заметки(ок) в формате ММ/ДД/ГГГГ:\n")
        target_notes = []
        for item in self.my_library.notes:
            if target_date in item.creation_time:
                target_notes.append(item)

        self.print_some_notes(target_notes)

    def remove_notes(self):
        user_choice = int(input("\n1.Найти заметки для удаления по названию. 2. Найти заметки для удаления по дате\n"))
        if user_choice == 1:
            target_title = input("Введите название заметки:\n")
            target_notes = []
            for item in self.my_library.notes:
                if item.title == target_title:
                    target_notes.append(item)
            for item in self.my_library.notes:
                if item in target_notes:
                    self.my_library.notes.remove(item)
            print("Заметки успешно удалены\n")
        elif user_choice == 2:
            target_date = input("Введите дату и/или время создания заметки(ок) в формате ММ/ДД/ГГГГ:\n")
            target_notes = []
            for item in self.my_library.notes:
                if target_date in item.creation_time:
                    target_notes.append(item)
            for item in self.my_library.notes:
                if item in target_notes:
                    self.my_library.notes.remove(item)
        self.update_file()

    def modify_notes(self):
        target_title = input("Введите название заметки:\n")
        for item in self.my_library.notes:
            if item.title == target_title:
                print("Заметка найдена")
                item.title = input("Введите новое название заметки:\n")
                item.head = input("Введите новый заголовок заметки:\n")
                item.body = input("Введите новое тело заметки:\n")
                item.creation_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            else:
                print("Заметка не найдена\n")

        self.update_file()

    def update_file(self):
        with open("notes.csv", "w") as file:
            writer = csv.writer(file)
            for item in self.my_library.notes:
                writer.writerow(f"{item.title}")
                writer.writerow(f"{item.head}")
                writer.writerow(f"{item.body}")
                writer.writerow(f"{item.creation_time}")

    def start(self):
        while True:
            user_input = int(input("1. Добавить новую заметку\n"
                                   "2. Вывести на экран все заметки\n"
                                   "3. Найти заметки по названию\n"
                                   "4. Найти заметки по дате\n"
                                   "5. Редактировать заметку\n"
                                   "6. Удалить выбранные заметки\n"
                                   "0. Выйти из программы\n"))

            if user_input == 0:
                break
            elif user_input == 1:
                self.add_note()
            elif user_input == 2:
                self.print_all_notes()
            elif user_input == 3:
                self.find_by_title()
            elif user_input == 4:
                self.find_by_date()
            elif user_input == 5:
                self.modify_notes()
            elif user_input == 6:
                self.remove_notes()
