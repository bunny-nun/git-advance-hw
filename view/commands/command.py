from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, presenter, view):
        """
        Абстрактный класс команды меню, необходимый для построения команд
        по соответствующему шаблону
        :param presenter: презентер
        :param view: представление
        """
        self.__description = None
        self.presenter = presenter
        self.view = view

    def set_description(self, description):
        self.__description = description

    @abstractmethod
    def execute(self):
        pass

    def __str__(self):
        return str(self.__description)
