class Notebook:
    def __init__(self):
        self.__notes = dict()

    def get_notes(self):
        return self.__notes

    def add_note(self, note):
        self.__notes.update({note.get_note_id(): note})

    def delete_note(self, note_id):
        return self.__notes.pop(note_id)

    def show_notes(self):
        return [str(note) + '\n' for note in self.__notes.values()]

    def get_note_by_id(self, note_id):
        try:
            return self.__notes[note_id]
        except KeyError:
            return 'Заметка с указанным ID отсутствует'

    def __str__(self):
        return [note for note in self.__notes]
