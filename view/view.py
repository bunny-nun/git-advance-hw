from view.menu.menu import Menu


class View:
    def __init__(self):
        """
        Класс View (Представление) приложения, отвечает за консольное
        взаимодействие с пользователем,
        устанавливает статус правда при инициализации, работает до тех пор,
        пока статус не меняется на ложь

        """
        self.__presenter = None
        self.__status = True

    def set_presenter(self, presenter):
        self.__presenter = presenter

    def set_status(self, status):
        self.__status = status

    def start(self):
        # запускает работу приложения, при запуске автоматически загружает
        # заметки из сохраненного файла и отображает главное меню приложения
        if self.__presenter.load_notes():
            print('Заметки успешно загружены')
        menu = Menu(self.__presenter, self)
        while self.__status:
            print('Выберите действие:')
            menu.show()
            choice = int(input())
            menu.run(choice)
