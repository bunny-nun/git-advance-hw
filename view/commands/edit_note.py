from view.commands.command import Command
from view.commands.edit.edit_title import EditTitle
from view.commands.edit.edit_text import EditText


class EditNote(Command):
    __menu = list()

    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Редактировать заметку")
        self.__menu.append(EditTitle(presenter, view))
        self.__menu.append(EditText(presenter, view))

    def execute(self):
        print('Что необходимо отредактировать:')
        self.show()
        choice = int(input())
        try:
            self.__menu[choice - 1].execute()
        except ValueError as e:
            print(e)
            print('Некорректная команда, необходимо ввести число')
        except IndexError:
            print('Некорректная команда, введенное число вне диапазона')

    def show(self):
        for i in range(len(self.__menu)):
            print(f'{i + 1} - {self.__menu[i]}')
