from view.commands.command import Command


class EditText(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Текст заметки")

    def execute(self):
        try:
            note_id = int(input('Введите ID заметки: '))
            note_text = input('Введите новый текст заметки: ')
            note = self.presenter.edit_text(note_id, note_text)
            print('Заметка изменена')
            print(note)
        except ValueError:
            print('Некорректное значение, необходимо ввести число')
        except KeyError:
            print(f'Заметка с указанным ID не найдена')

