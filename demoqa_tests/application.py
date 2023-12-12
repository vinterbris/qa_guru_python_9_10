from demoqa_tests.pages.left_panel import LeftPanel
from demoqa_tests.pages.simple_registration_page import SimpleRegistrationPage


class Application:
    def __init__(self):
        self.simple_registration = SimpleRegistrationPage()
        self.left_panel = LeftPanel()


app = Application()


app.left_panel.open('Elements', 'Text Box')