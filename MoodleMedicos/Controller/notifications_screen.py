
from View.NotificationsScreen.notifications_screen import NotificationsScreenView


class NotificationsScreenController:
    """
    The `NotificationsScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.notifications_screen.NotificationsScreenModel
        self.view = NotificationsScreenView(controller=self, model=self.model)

    def get_view(self) -> NotificationsScreenView:
        return self.view
