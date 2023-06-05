from view.commands.command import Command


class Exit(Command):
    def __init__(self, presenter, view):
        """
        Выход с сохранением
        :param presenter: презентер
        :param view: представление
        """
        super().__init__(presenter, view)
        super().set_description("Сохранить все и выйти")

    def execute(self):
        # передает презентеру команду на сохранение заметок и представлению
        # - статус ложь для завершения работы приложения
        status = self.presenter.save_notes()
        if not status:
            print('Заметки сохранены')
        self.view.set_status(status)
