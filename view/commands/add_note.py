from view.commands.command import Command


class AddNote(Command):
    def __init__(self, presenter, view):
        """
        Добавление новой заметки
        :param presenter: презентер
        :param view: представление
        """
        super().__init__(presenter, view)
        super().set_description("Создать новую заметку")

    def execute(self):
        # запрашивает и принимает текст заголовка и тела заметки, передает
        # строковые значения в презентер, получает экземпляр созданной заметки
        # и выводит ее на экран
        note_title = input('Введите заголовок: ')
        note_text = input('Введите текст заметки: ')
        note = self.presenter.add_note(note_title, note_text)
        print('Добавлена заметка:')
        print(note)
