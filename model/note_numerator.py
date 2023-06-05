class NoteNumerator:
    def __init__(self):
        self.__max_id = 0

    def get_max_id(self):
        return self.__max_id

    def set_max_id(self, note_id):
        self.__max_id = note_id

    def next_id(self):
        self.__max_id += 1
        return self.__max_id
