from view.commands.command import Command


class Save(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Сохранить заметки")

    def execute(self):
        status = self.presenter.save_notes()
        if not status:
            print('Заметки сохранены')
