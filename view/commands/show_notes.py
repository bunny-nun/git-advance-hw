from view.commands.command import Command


class ShowNotes(Command):
    def __init__(self, presenter, view):
        """
        Показывает все заметки
        :param presenter: презентер
        :param view: представление
        """
        super().__init__(presenter, view)
        super().set_description("Показать все заметки")
        self.__description = ""

    def execute(self):
        # передает презентеру команду, принимает список всех заметок и выводит
        # их на экран
        notes = self.presenter.show_notes()
        for note in notes:
            print(note)
