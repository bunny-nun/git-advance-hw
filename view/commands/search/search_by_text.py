from view.commands.command import Command


class SearchByText(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Найти по тексту заметки")

    def execute(self):
        search_string = input('Введите ключевые слова через пробел: ')\
            .lstrip().rstrip()
        key_words = search_string.split()
        notes = self.presenter.search_by_text(key_words)
        for note in notes:
            print(note)
        if len(notes) == 0:
            print('Заметок с указанными ключевыми словами не найдено')
