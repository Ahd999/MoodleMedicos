from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.navigationbar import MDNavigationItem, MDNavigationBar, MDNavigationItemIcon, MDNavigationItemLabel
from kivymd.uix.screenmanager import MDScreenManager
import os

class BaseMDNavigationItem(MDNavigationItem):
    screen_name = StringProperty()

    def __init__(self, screen_name, icon, text, **kwargs):
        super().__init__(**kwargs)
        self.screen_name = screen_name
        self.add_widget(MDNavigationItemIcon(icon=icon))
        self.add_widget(MDNavigationItemLabel(text=text))


class BottomNav(MDNavigationBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.radius = "15dp"
        self.add_widget(BaseMDNavigationItem("Home", "home", "Home", active=True))
        self.add_widget(BaseMDNavigationItem("Courses", "book-education-outline", "Courses"))
        self.add_widget(BaseMDNavigationItem("Connect", "chat", "Connect"))
        self.add_widget(BaseMDNavigationItem("Notifications", "bell-badge-outline", "Notifications"))

