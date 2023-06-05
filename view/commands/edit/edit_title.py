from view.commands.command import Command


class EditTitle(Command):
    def __init__(self, presenter, view):
        """
        Редактирование заголовка заметки
        :param presenter: презентер
        :param view: представление
        """
        super().__init__(presenter, view)
        super().set_description("Заголовок заметки")

    def execute(self):
        # принимает идентификатор заметки и строковое содержание нового
        # заголовка заметки, передает значения в презентер, принимает
        # измененную заметку, выводит ее на экран, обрабатывает ошибки
        # неправильного ввода идентификатора
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
