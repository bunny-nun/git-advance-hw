from view.commands.command import Command


class AddNote(Command):
    def __init__(self, presenter, view):
        super().__init__(presenter, view)
        super().set_description("Создать новую заметку")

    def execute(self):
        note_title = input('Введите заголовок: ')
        note_text = input('Введите текст заметки: ')
        note = self.presenter.add_note(note_title, note_text)
        print('Добавлена заметка:')
        print(note)
