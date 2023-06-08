from view.commands.command import Command
from view.commands.search.search_by_id import SearchByID
from view.commands.search.search_by_id_pool import SearchByIDPool
from view.commands.search.search_by_title import SearchByTitle
from view.commands.search.search_by_text import SearchByText
from view.commands.search.search_by_date import SearchByDate


class SearchNote(Command):
    __menu = list()

    def __init__(self, presenter, view):
        """
        Поиск заметок
        :param presenter: презентер
        :param view: представление
        """
        super().__init__(presenter, view)
        super().set_description("Найти заметку")
        self.__menu.append(SearchByID(presenter, view))
        self.__menu.append(SearchByIDPool(presenter, view))
        self.__menu.append(SearchByTitle(presenter, view))
        self.__menu.append(SearchByText(presenter, view))
        self.__menu.append(SearchByDate(presenter, view))

    def execute(self):
        # выводит меню для выбора метода поиска и запускает соответствующую
        # команду, обрабатывает ошибки при вводе значения
        print('Выберите действие:')
        self.show()
        choice = int(input())
        try:
            self.__menu[choice - 1].execute()
        except ValueError:
            print('Некорректная команда, необходимо ввести число')
        except IndexError:
            print('Некорректная команда, введенное число вне диапазона')

    def show(self):
        for i in range(len(self.__menu)):
            print(f'{i + 1} - {self.__menu[i]}')
