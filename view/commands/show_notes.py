from view.commands.command import Command


class ShowNotes(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Показать все заметки")
        self.__description = ""

    def execute(self):
        notes = self.presenter.show_notes()
        for note in notes:
            print(note)
