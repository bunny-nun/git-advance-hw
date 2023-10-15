from view.commands.command import Command


class DeleteNote(Command):
    def __init__(self, presenter, view):
        """
        Удаление заметки
        :param presenter: презентер
        :param view: представление
        """
        super().__init__(presenter, view)
        super().set_description("Удалить заметку")

    def execute(self):
        # запрашивает и принимает числовое значение идентификатора заметки,
        # передает команду в презентер, принимает удаленную заметку и выводит
        # ее на экран пользователя в качестве подтверждения, обрабатывает
        # ошибки некорректного ввода идентификатора
        try:
            note_id = int(input('Введите ID заметки: '))
            result = self.presenter.delete_note(note_id)
            print('Следующая заметка была успешно удалена:')
            print(result)
        except ValueError:
            print('Некорректное значение, необходимо ввести число')
        except KeyError:
            print('Заметка с указанным ID не найдена')
