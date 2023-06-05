class NoteNumerator:
    def __init__(self):
        """
        Класс NoteNumerator (единый нумератор заметок)
        """
        self.__max_id = 0

    def get_max_id(self):
        return self.__max_id

    def set_max_id(self, note_id):
        # сеттер используется для задания значения
        # при загрузке заметок из файла
        self.__max_id = note_id

    def next_id(self):
        # возвращает следующее значение идентификатора заметки
        self.__max_id += 1
        return self.__max_id
