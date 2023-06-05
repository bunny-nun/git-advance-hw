from view.commands.command import Command


class DeleteNote(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Удалить заметку")

    def execute(self):
        try:
            note_id = int(input('Введите ID заметки: '))
            result = self.presenter.delete_note(note_id)
            print(f'Следующая заметка была успешно удалена:')
            print(result)
        except ValueError:
            print('Некорректное значение, необходимо ввести число')
        except KeyError:
            print(f'Заметка с указанным ID не найдена')
