
from View.CourseScreen.course_screen import CourseScreenView


class CourseScreenController:
    """
    The `CourseScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.course_screen.CourseScreenModel
        self.view = CourseScreenView(controller=self, model=self.model)

    def get_view(self) -> CourseScreenView:
        return self.view
