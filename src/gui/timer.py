import flet as ft
import time

class Timer:
    def __init__(self, white, bg_grey,toolbar_grey, red, blue, page):
        # Incapsulation
        self.WHITE = white
        self.page = page
        self.RED = red
        self.BG_GREY = bg_grey
        self.TOOLBAR_GREY = toolbar_grey
        self.BLUE = blue
        self.minutes = 25
        self.seconds = 0
        self.is_running = False
        self.is_paused = False
        self.time_value = f"{self.minutes:02}:{self.seconds:02}"
        self.TEXT = ft.Text(value=self.time_value, font_family="LexendDeca", size=126, color=self.WHITE)
        self.START_BUTTON = ft.FilledButton(text="START", bgcolor=self.WHITE, width=160, style=ft.ButtonStyle(color=self.BG_GREY, text_style=ft.TextStyle(font_family="LexendDeca", size=17), shape=ft.RoundedRectangleBorder(radius=12)), visible=True, on_click=self.start_timer)
        self.PAUSE_BUTTON = ft.FilledButton(text="PAUSE", bgcolor=self.WHITE, width=160, style=ft.ButtonStyle(color=self.BG_GREY, text_style=ft.TextStyle(font_family="LexendDeca", size=17), shape=ft.RoundedRectangleBorder(radius=12)), visible=False, on_click=self.pause_timer)
        self.CONCENTRATION_BUTTON = ft.TextButton(text="Concentration",style=ft.ButtonStyle(color=self.WHITE, bgcolor=self.RED, text_style=ft.TextStyle(font_family="LexendDeca", size=17), shape=ft.RoundedRectangleBorder(radius=5), padding=ft.Padding(left=12, top=29, right=12, bottom=29)), width=150, on_click=self.change_mode)
        self.BREAK_BUTTON = ft.TextButton(text="Take a Break",style=ft.ButtonStyle(color=self.WHITE, text_style=ft.TextStyle(font_family="LexendDeca", size=17), shape=ft.RoundedRectangleBorder(radius=5), padding=ft.Padding(left=12, top=29, right=12, bottom=29)), width=150, on_click=self.change_mode)
        self.TOOLBAR = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(content=self.CONCENTRATION_BUTTON),
                    ft.Container(content=self.BREAK_BUTTON)
                ],
                spacing=0,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            bgcolor=self.TOOLBAR_GREY,
            height=64,
            width=301,
            border_radius=8,
            margin=ft.Margin(left=0, top=26, right=0, bottom=0)
        )
        self.TIMER = ft.Column(controls=[self.TOOLBAR, ft.Container(content=self.TEXT, height=150, margin=ft.Margin(left=0, top=-10, right=0, bottom=18)), ft.Container(content=self.START_BUTTON), ft.Container(content=self.PAUSE_BUTTON, margin=ft.Margin(left=0, top=-10, right=0, bottom=0))], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def add_timer(self) -> ft.Container:
        return self.TIMER

    def start_timer(self, e):
        if self.is_running:
            return
        self.is_running = True
        self.is_paused = False
        self.START_BUTTON.visible = False
        self.PAUSE_BUTTON.visible = True
        while self.minutes > 0 or self.seconds > 0:
            if not self.is_running:
                break
            time.sleep(1)
            if self.seconds == 0:
                self.minutes -= 1
                self.seconds = 59
            else:
                self.seconds -= 1
            self.time_value = f"{self.minutes:02}:{self.seconds:02}"
            self.TEXT.value = self.time_value
            self.page.update()
            if self.minutes == 0 and self.seconds == 0:
                self.is_running = False
                self.is_paused = True
                self.START_BUTTON.visible = True
                self.PAUSE_BUTTON.visible = False
                self.change_mode(e)
                self.page.update()

    def pause_timer(self, e):
        self.is_paused = True
        self.is_running = False
        self.START_BUTTON.visible = True
        self.PAUSE_BUTTON.visible = False

    def change_mode(self, e):
        match (self.CONCENTRATION_BUTTON.style.bgcolor):
            case (self.RED):
                self.BREAK_BUTTON.style.bgcolor = self.BLUE
                self.CONCENTRATION_BUTTON.style.bgcolor = self.TOOLBAR_GREY
                self.minutes = 5
                self.seconds = 0
            case (self.TOOLBAR_GREY):
                self.BREAK_BUTTON.style.bgcolor = self.TOOLBAR_GREY
                self.CONCENTRATION_BUTTON.style.bgcolor = self.RED
                self.minutes = 25
                self.seconds = 0
        self.time_value = f"{self.minutes:02}:{self.seconds:02}"
        self.TEXT.value = self.time_value
        self.page.update()
        