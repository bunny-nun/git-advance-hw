class Notebook:
    def __init__(self):
        """
        Класс Notebook для хранения заметок
        """
        self.__notes = dict()

    def get_notes(self):
        return self.__notes

    def add_note(self, note):
        # добавляет заметку в словарь по идентификатору в качестве ключа
        self.__notes.update({note.get_note_id(): note})

    def delete_note(self, note_id):
        # удаляет заметку по идентификатору
        return self.__notes.pop(note_id)

    def show_notes(self):
        # возвращает список со всеми заметками
        return [str(note) + '\n' for note in self.__notes.values()]

    def get_note_by_id(self, note_id):
        # возвращает заметку по ее идентификатору либо строку с указанием,
        # что заметка с таким идентификатором не найдена
        try:
            return self.__notes[note_id]
        except KeyError:
            return 'Заметка с указанным ID отсутствует'

    def __str__(self):
        return [str(note) + '\n' for note in self.__notes.values()]
