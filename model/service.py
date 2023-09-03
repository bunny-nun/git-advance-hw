import datetime

from model.notebook import Notebook
from model.note import Note
from model.note_numerator import NoteNumerator
import json


def convert_datetime(datetime_data):
    """
    Конвертирует строковое представление даты, сохраненной
    в файле в формат datetime
    :param datetime_data: строковое представление даты
    :return: объект класса datetime
    """
    datetime_list = datetime_data.split(';')
    date_list = datetime_list[0].split('-')
    for i in range(len(date_list)):
        date_list[i] = int(date_list[i])
    time_list = datetime_list[1].split(':')
    for i in range(len(time_list)):
        time_list[i] = int(time_list[i])
    date = datetime.datetime(date_list[0], date_list[1], date_list[2],
                             hour=time_list[0], minute=time_list[1],
                             second=time_list[2])
    return date


class Service:
    def __init__(self):
        '''
        Класс Service выполняет сервисные функции приложения
        При инициализации класса в качестве атрибутов создаются экземпляры
        класса Notebook для хранения заметок и нумератор
        '''
        self.__notebook = Notebook()
        self.__numerator = NoteNumerator()

    def add_note(self, note_title, note_text):
        # создание новой заметки
        note = Note(self.__numerator.next_id(), note_title, note_text)
        self.__notebook.add_note(note)
        return note

    def delete_note(self, note_id):
        # удаление заметки по идентификатору
        return self.__notebook.delete_note(note_id)

    def show_notes(self):
        # возвращает список со всеми заметками
        return self.__notebook.show_notes()

    def search_by_id(self, note_id):
        # поиск заметки по идентификатору
        return self.__notebook.get_note_by_id(note_id)

    def search_by_id_pool(self, note_id_start, note_id_end):
        # поиск заметки по диапазону идентификаторов, возвращает список заметок
        notes = self.__notebook.get_notes().values()
        result_notes = list()
        for note in notes:
            if note.get_note_id() >= note_id_start:
                if note.get_note_id() <= note_id_end:
                    result_notes.append(note)
        return result_notes

    def search_by_title(self, key_words):
        # поиск заметки по вхождению в заголовок ключевых слов
        # в качестве подстроки, приводит все значения слов к нижнему регистру,
        # возвращает список заметок, в которых встречаются все искомые слова
        notes = self.__notebook.get_notes().values()
        result_notes = list()
        for note in notes:
            result = True
            for key_word in key_words:
                if note.get_note_title().lower().find(key_word.lower()) == -1:
                    result = False
            if result:
                result_notes.append(note)
        return result_notes

    def search_by_text(self, key_words):
        # поиск заметки по вхождению в тело заметки ключевых слов
        # в качестве подстроки, приводит все значения слов к нижнему регистру,
        # возвращает список заметок, в которых встречаются все искомые слова
        notes = self.__notebook.get_notes().values()
        result_notes = list()
        for note in notes:
            result = True
            for key_word in key_words:
                if note.get_note_text().lower().find(key_word.lower()) == -1:
                    result = False
            if result:
                result_notes.append(note)
        return result_notes

    def search_by_date(self, start_date, end_date):
        # поиск заметок по диапазону дат
        # возвращает список всех заметок, созданных в пределах
        # данного диапазона
        notes = self.__notebook.get_notes().values()
        result_notes = list()
        for note in notes:
            if note.get_create_datetime().date() >= start_date:
                if note.get_create_datetime().date() <= end_date:
                    result_notes.append(note)
        return result_notes

    def edit_title(self, note_id, note_title):
        # изменяет заголовок заметки по ее идентификатору и возвращает
        # измененную заметку
        note = self.__notebook.get_notes()[note_id]
        note.set_note_title(note_title)
        return note

    def edit_text(self, note_id, note_text):
        # изменяет тело заметки по ее идентификатору и возвращает
        # измененную заметку
        note = self.__notebook.get_notes()[note_id]
        note.set_note_text(note_text)
        return note

    def load_notes(self):
        # загружает сохраненный файл формата json, парсит поля и добавляет
        # каждую загруженную заметку
        # дополнительно вычисляет максимальное значение идентификатора и
        # сохраняет его
        try:
            with open('notes.json', 'r',
                      encoding='UTF-8') as file:
                notes = json.load(file)
                id_list = list()
                for element in notes['notes']:
                    id_list.append(element['note_id'])
                    note = Note(element['note_id'],
                                element['note_title'],
                                element['note_text'])
                    note.set_create_datetime(
                        convert_datetime(element['create_datetime']))
                    note.set_change_datetime(
                        convert_datetime(element['change_datetime']))
                    self.__notebook.add_note(note)
                self.__numerator.set_max_id(max(id_list))
            return True
        except ValueError as e:
            print(e)
            return False

    def save_notes(self):
        # сохраняет все заметки, добавленные в данный экземпляр класса
        # в формате json и возвращает значение ложь для реализации метода
        # завершения работы приложения с сохранением
        notes = {'notes': list()}
        for note in self.__notebook.get_notes().values():
            notes['notes'].append({'note_id': note.get_note_id(),
                                   'note_title': note.get_note_title(),
                                   'note_text': note.get_note_text(),
                                   'create_datetime': note.get_create_datetime(
                                   ).strftime('%Y-%m-%d;%H:%M:%S'),
                                   'change_datetime': note.get_change_datetime(
                                   ).strftime('%Y-%m-%d;%H:%M:%S')})
        with open('notes.json', 'w',
                  encoding='UTF-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        return False
