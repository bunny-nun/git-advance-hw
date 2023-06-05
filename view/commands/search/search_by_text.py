from view.commands.command import Command


class SearchByText(Command):
    def __init__(self, presenter, view):
        """
        Поиск заметки по ключевым словам в теле заметки
        :param presenter: презентер
        :param view: представление
        """
        super().__init__(presenter, view)
        super().set_description("Найти по тексту заметки")

    def execute(self):
        # принимает ключевые слова для поиска в теле заметки, передает
        # значения в презентер, принимает все найденные заметки и выводит их
        # на экран
        search_string = input('Введите ключевые слова через пробел: ')\
            .lstrip().rstrip()
        key_words = search_string.split()
        notes = self.presenter.search_by_text(key_words)
        for note in notes:
            print(note)
        if len(notes) == 0:
            print('Заметок с указанными ключевыми словами не найдено')
