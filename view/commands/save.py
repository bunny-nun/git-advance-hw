from view.commands.command import Command


class Save(Command):
    def __init__(self, presenter, view):
        """
        Сохранение заметок
        :param presenter: презентер
        :param view: представление
        """
        super().__init__(presenter, view)
        super().set_description("Сохранить заметки")

    def execute(self):
        # передает презентеру команду на сохранение заметок, принимает статус
        # ложь в случае успешного выполнения команды и выводит на экран
        # подтверждение успешного сохранения
        status = self.presenter.save_notes()
        if not status:
            print('Заметки сохранены')
