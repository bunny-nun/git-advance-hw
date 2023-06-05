from view.commands.command import Command


class EditTitle(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Заголовок заметки")

    def execute(self):
        try:
            note_id = int(input('Введите ID заметки: '))
            note_title = input('Введите новый заголовок заметки: ')
            note = self.presenter.edit_title(note_id, note_title)
            print('Заметка изменена')
            print(note)
        except ValueError:
            print('Некорректное значение, необходимо ввести число')
        except KeyError:
            print(f'Заметка с указанным ID не найдена')
