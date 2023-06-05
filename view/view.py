from view.menu.menu import Menu


class View:
    def __init__(self):
        self.__presenter = None
        self.__status = True

    def set_presenter(self, presenter):
        self.__presenter = presenter

    def set_status(self, status):
        self.__status = status

    def start(self):
        if self.__presenter.load_notes():
            print('Заметки успешно загружены')
        menu = Menu(self.__presenter, self)
        while self.__status:
            print('Выберите действие:')
            menu.show()
            choice = int(input())
            menu.run(choice)
