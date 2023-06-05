from view.commands.command import Command
import datetime


class SearchByDate(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Найти по дате создания")

    def execute(self):
        status = False
        while not status:
            try:
                print('Введите начальную дату (значения вводятся '
                      'цифрами без пробелов и знаков препинания)')
                start_year = int(input('Введите год: '))
                start_month = int(input('Введите месяц: '))
                start_day = int(input('Введите день: '))
                start_date = datetime.date(start_year, start_month, start_day)

                print('Введите конечную дату дату (значения вводятся цифрами '
                      'без пробелов и знаков препинания):')
                end_year = int(input('Введите год: '))
                end_month = int(input('Введите месяц: '))
                end_day = int(input('Введите день: '))
                end_date = datetime.date(end_year, end_month, end_day)
                status = True
                notes = self.presenter.search_by_date(start_date, end_date)
                for note in notes:
                    print(note)
                if len(notes) == 0:
                    print('Заметок в указанном диапазоне не найдено')
            except ValueError:
                print('Некорректное значение')
                stop = int(input('Для повторного поиска нажмите 0, '
                                 'для выхода в главное меню нажмите любую '
                                 'кнопку:\n'))
                if stop != 0:
                    status = True
