from model.service import Service
from presenter.presenter import Presenter
from view.view import View


if __name__ == '__main__':
    view = View()
    service = Service()
    presenter = Presenter(view, service)
    view.set_presenter(presenter)
    view.start()
