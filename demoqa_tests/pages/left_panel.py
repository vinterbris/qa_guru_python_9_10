from selene import browser


class LeftPanel:
    
    def __init__(self):
        self.elements_side_panel = browser.element('.element-list').click()

    def open_elements_text_box(self):
        self.elements_side_panel.element()