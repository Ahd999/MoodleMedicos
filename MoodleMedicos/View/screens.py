# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.course_screen import CourseScreenModel
from Controller.course_screen import CourseScreenController
from Model.connect_screen import ConnectScreenModel
from Controller.connect_screen import ConnectScreenController
from Model.notifications_screen import NotificationsScreenModel
from Controller.notifications_screen import NotificationsScreenController

screens = {
    'Home': {
        'model': MainScreenModel,
        'controller': MainScreenController,
    },
    'Connect': {
        'model': ConnectScreenModel,
        'controller': ConnectScreenController,
    },
    'Courses': {
        'model': CourseScreenModel,
        'controller': CourseScreenController,
    },
    'Notifications': {
        'model': NotificationsScreenModel,
        'controller': NotificationsScreenController,
    },
}