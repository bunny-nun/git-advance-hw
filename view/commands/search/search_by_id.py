from view.commands.command import Command


class SearchByID(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Найти по ID")

    def execute(self):
        try:
            note_id = int(input('Введите ID заметки: '))
            note = self.presenter.search_by_id(note_id)
            print(note)
        except ValueError:
            print('Некорректное значение, необходимо ввести число')

