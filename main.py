from model.service import Service
from presenter.presenter import Presenter
from view.view import View


if __name__ == '__main__':
    # создает экземпляр представления, сервиса и презентера,
    # запускает работу представления
    view = View()
    service = Service()
    presenter = Presenter(view, service)
    view.set_presenter(presenter)
    view.start()
