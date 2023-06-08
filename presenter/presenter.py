class Presenter:
    def __init__(self, view, service):
        """
        Класс Presenter используется для взаимодействия между моделью приложения
        и его представлением
        :param view: экземпляр представления приложения
        :param service: экземпляр сервиса модели приложения
        """
        self.__view = view
        self.__service = service

    def load_notes(self):
        return self.__service.load_notes()

    def add_note(self, note_title, note_text):
        return self.__service.add_note(note_title, note_text)

    def delete_note(self, note_id):
        return self.__service.delete_note(note_id)

    def search_by_id(self, note_id):
        return self.__service.search_by_id(note_id)

    def search_by_id_pool(self, note_id_start, note_id_end):
        return self.__service.search_by_id_pool(note_id_start, note_id_end)

    def search_by_title(self, key_words):
        return self.__service.search_by_title(key_words)

    def search_by_text(self, key_words):
        return self.__service.search_by_text(key_words)

    def search_by_date(self, start_date, end_date):
        return self.__service.search_by_date(start_date, end_date)

    def edit_title(self, note_id, node_title):
        return self.__service.edit_title(note_id, node_title)

    def edit_text(self, note_id, node_text):
        return self.__service.edit_text(note_id, node_text)

    def show_notes(self):
        return self.__service.show_notes()

    def save_notes(self):
        return self.__service.save_notes()
