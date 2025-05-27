import flet as ft
from gui.window_bar import WindowBar
from gui.timer import Timer
from gui.tasklist import TaskList

class PomidorApp:
    def __init__(self, page: ft.Page):
        self.BG_GREY = "#1E1E1E"
        self.ACC_GREY = "#252525"
        self.TOOLBAR_GREY = "#2C2C2C"
        self.RED = "#F44336"
        self.BLUE = "#0095FF"
        self.WHITE = "#FFFFFF"
        self.WINDOW = page.window
        page.route = "/concentration"
        page.window.width = 470
        page.window.height = 685
        page.bgcolor = self.BG_GREY
        page.spacing = 0
        page.padding = 0
        page.window.maximizable = False
        page.window.frameless = True
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.fonts = {"LexendDeca": "/fonts/LexendDeca-Regular.ttf"}
        page.update()

    def load_window_bar(self, page: ft.Page):
        window_bar = WindowBar(self.WHITE, self.ACC_GREY, self.RED, self.WINDOW, page)
        page.add(window_bar.add_window_bar())

    def load_timer(self, page: ft.Page):
        timer = Timer(self.WHITE, self.BG_GREY, self.TOOLBAR_GREY, self.RED, self.BLUE, page)
        page.add(timer.add_timer())

    def load_task_list(self, page: ft.Page):
        task_list = TaskList(self.WHITE, self.BG_GREY, self.RED, self.TOOLBAR_GREY, page)
        page.add(task_list.add_task_list()) 