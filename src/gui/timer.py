import flet as ft

class Timer:
    def __init__(self, white):
        # Incapsulation
        self.WHITE = white
        self.TIME_VALUE = "25:00"
        self.TEXT = ft.Text(value=self.TIME_VALUE, font_family="LexendDeca", size=20, color=self.WHITE)
        self.TIMER = ft.Container(content=self.TEXT)

    def add_timer(self) -> ft.Container:
        return self.TIMER