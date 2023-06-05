from view.commands.command import Command


class Exit(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Сохранить все и выйти")

    def execute(self):
        status = self.presenter.save_notes()
        if not status:
            print('Заметки сохранены')
        self.view.set_status(status)
