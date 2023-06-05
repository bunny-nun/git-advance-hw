from view.commands.command import Command


class SearchByID(Command):
    def __init__(self, presenter, view):
        """
        Поиск заметки по идентификатору
        :param presenter: презентер
        :param view: представление
        """
        super().__init__(presenter, view)
        super().set_description("Найти по ID")

    def execute(self):
        # принимает числовое значение идентификатора заметки, передает его
        # презентеру и выводит принятую заметку на экран, обрабатывает
        # исключения
        try:
            note_id = int(input('Введите ID заметки: '))
            note = self.presenter.search_by_id(note_id)
            print(note)
        except ValueError:
            print('Некорректное значение, необходимо ввести число')

