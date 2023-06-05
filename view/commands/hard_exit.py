from view.commands.command import Command


class HardExit(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Выйти без сохранения")

    def execute(self):
        self.view.set_status(False)
