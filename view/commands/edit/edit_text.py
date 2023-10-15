from view.commands.command import Command


class EditText(Command):
    def __init__(self, presenter, view):
        """
        Редактирование тела заметки
        :param presenter: презентер
        :param view: представление
        """
        super().__init__(presenter, view)
        super().set_description("Текст заметки")

    def execute(self):
        # принимает идентификатор заметки и строковое содержание нового тела
        # заметки, передает значения в презентер, принимает измененную заметку,
        # выводит ее на экран, обрабатывает ошибки неправильного ввода
        # идентификатора
        try:
            note_id = int(input('Введите ID заметки: '))
            note_text = input('Введите новый текст заметки: ')
            note = self.presenter.edit_text(note_id, note_text)
            print('Заметка изменена')
            print(note)
        except ValueError:
            print('Некорректное значение, необходимо ввести число')
        except KeyError:
            print('Заметка с указанным ID не найдена')
