from view.commands.add_note import AddNote
from view.commands.delete_note import DeleteNote
from view.commands.edit_note import EditNote
from view.commands.search_note import SearchNote
from view.commands.show_notes import ShowNotes
from view.commands.save import Save
from view.commands.hard_exit import HardExit
from view.commands.exit import Exit


class Menu:
    __menu = list()

    def __init__(self, presenter, view):
        """
        Главное меню приложения, в качестве атрибутов хранит все отображаемые
        команды
        :param presenter: презентер
        :param view: представление
        """
        self.__menu.append(AddNote(presenter, view))
        self.__menu.append(DeleteNote(presenter, view))
        self.__menu.append(EditNote(presenter, view))
        self.__menu.append(SearchNote(presenter, view))
        self.__menu.append(ShowNotes(presenter, view))
        self.__menu.append(Save(presenter, view))
        self.__menu.append(Exit(presenter, view))
        self.__menu.append(HardExit(presenter, view))

    def run(self, choice):
        # запускает метод execute экземпляра класса, соответствующего
        # выбранной пользователем команды и обрабатывает исключения в случае
        # некорректного ввода
        try:
            self.__menu[choice - 1].execute()
        except ValueError:
            print('Некорректное значение, необходимо ввести число')
        except IndexError:
            print('Некорректное значение, введенное число вне диапазона')

    def show(self):
        # отображает классы, отвечающие за команды, включенные в главное
        # меню приложения
        for i in range(len(self.__menu)):
            print(f'{i + 1} - {self.__menu[i]}')
