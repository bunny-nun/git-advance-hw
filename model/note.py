import datetime


class Note:
    def __init__(self, note_id, note_title, note_text):
        self.__note_id = note_id
        self.__note_title = note_title
        self.__note_text = note_text
        self.__create_datetime = datetime.datetime.now()
        self.__change_datetime = datetime.datetime.now()

    def get_note_id(self):
        return self.__note_id

    def get_note_title(self):
        return self.__note_title

    def set_note_title(self, note_title):
        self.__note_title = note_title
        self.__change_datetime = datetime.datetime.now()

    def get_note_text(self):
        return self.__note_text

    def set_note_text(self, note_text):
        self.__note_text = note_text
        self.__change_datetime = datetime.datetime.now()

    def get_create_datetime(self):
        return self.__create_datetime

    def set_create_datetime(self, create_datetime):
        self.__create_datetime = create_datetime

    def get_change_datetime(self):
        return self.__change_datetime

    def set_change_datetime(self, change_datetime):
        self.__change_datetime = change_datetime

    def __str__(self):
        create_datetime = self.__create_datetime.strftime('%d %B %Y %H:%M')
        change_datetime = self.__change_datetime.strftime('%d %B %Y %H:%M')
        return f'ID: {self.__note_id}\nЗаголовок: {self.__note_title}\n' \
               f'Время создания: {create_datetime}\n' \
               f'Время последнего изменения: {change_datetime}\n' \
               f'Заметка: {self.__note_text}\n'
