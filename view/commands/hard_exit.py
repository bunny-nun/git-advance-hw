from view.commands.command import Command


class HardExit(Command):
    def __init__(self, presenter, view):
        """
        Выход без сохранения
        :param presenter: презентер
        :param view: представление
        """
        super().__init__(presenter, view)
        super().set_description("Выйти без сохранения")

    def execute(self):
        # передает представлению статус ложь для завершения работы приложения
        self.view.set_status(False)
