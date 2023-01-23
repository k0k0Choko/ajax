from framework.page import Page


class MainPage(Page):
    SIDE_BAR = 'com.ajaxsystems:id/menuDrawer'
    ADD_HUB_SIDE = 'com.ajaxsystems:id/addHub'
    APP_SETTINGS = 'com.ajaxsystems:id/settings'
    HELP = 'com.ajaxsystems:id/help'
    REPORT_A_PROBLEM = 'com.ajaxsystems:id/logs'
    VIDEO_SURVEILLANCE = 'com.ajaxsystems:id/camera'

    def press_side_bar(self):
        self.click(MainPage.SIDE_BAR)

    def press_add_hub(self):
        self.press_side_bar()
        self.click(MainPage.ADD_HUB_SIDE)

    def press_app_settings(self):
        self.press_side_bar()
        self.click(MainPage.APP_SETTINGS)

    def press_help(self):
        self.press_side_bar()
        self.click(MainPage.HELP)

    def press_report_a_problem(self):
        self.press_side_bar()
        self.click(MainPage.REPORT_A_PROBLEM)

    def press_video_surveillance(self):
        self.press_side_bar()
        self.click(MainPage.VIDEO_SURVEILLANCE)
