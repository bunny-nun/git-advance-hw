from view.commands.command import Command


class SearchByIDPool(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Найти по диапазону ID")

    def execute(self):
        try:
            note_id_start = int(
                input('Введите начальное значение ID заметки: '))
            note_id_end = int(input('Введите конечное значение ID заметки: '))
            notes = self.presenter.search_by_id_pool(note_id_start,
                                                     note_id_end)
            for note in notes:
                print(note)
            if len(notes) == 0:
                print('Заметок в указанном диапазоне не найдено')
        except ValueError:
            print('Некорректное значение, необходимо ввести число')
