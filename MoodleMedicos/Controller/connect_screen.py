
from View.ConnectScreen.connect_screen import ConnectScreenView


class ConnectScreenController:
    """
    The `ConnectScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.connect_screen.ConnectScreenModel
        self.view = ConnectScreenView(controller=self, model=self.model)

    def get_view(self) -> ConnectScreenView:
        return self.view
