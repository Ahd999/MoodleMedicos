"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.behaviors import focus_behavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.screenmanager import MDScreenManager

from View.bottom_nav import BottomNav
from View.screens import screens
Window.left = 1000

class MoodleMedicos(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Yellow"
        self.manager_screens = MDScreenManager(
            theme_bg_color='Custom',
            md_bg_color=self.theme_cls.tertiaryContainerColor
        )
        
    def build(self) -> MDScreenManager:
        self.generate_application_screens()
        root = MDBoxLayout(
            orientation="vertical",
        )
        root.add_widget(self.manager_screens)
        bar = BottomNav()
        bar.bind(on_switch_tabs = self.on_switch_tabs)
        root.add_widget(
            MDBoxLayout(
                bar,
                adaptive_height=True,
                padding="10dp",
                theme_bg_color="Custom",
                md_bg_color=[0.9254901960784314, 0.9137254901960784, 0.8392156862745098, 1.0],
            ),
        )
        return root

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

    def on_switch_tabs(self, bar, item, item_icon, item_text):
        self.manager_screens.current = item.screen_name
MoodleMedicos().run()
