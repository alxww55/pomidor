import flet as ft

class Toolbar:
    def __init__(self, white, toolbar_grey):
        self.WHITE = white
        self.TOOLBAR_GREY = toolbar_grey
        self.CONCENTRATION_BUTTON = ft.TextButton(
            text="Concentration", 
            style=ft.ButtonStyle(color=self.WHITE, text_style=ft.TextStyle(font_family="LexendDeca", size=19), shape=ft.RoundedRectangleBorder(radius=5), padding=ft.Padding(left=12, top=26, right=12, bottom=26)),
            width=150
        )
        self.PAUSE_BUTTON = ft.TextButton(
            text="Take a Break",
            style=ft.ButtonStyle(color=self.WHITE, text_style=ft.TextStyle(font_family="LexendDeca", size=19), shape=ft.RoundedRectangleBorder(radius=5), padding=ft.Padding(left=12, top=26, right=12, bottom=26)),
            width=150
        )
        self.TOOLBAR = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(content=self.CONCENTRATION_BUTTON),
                    ft.Container(content=self.PAUSE_BUTTON)
                ],
                spacing=0,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            bgcolor=self.TOOLBAR_GREY,
            height=64,
            width=301,
            border_radius=8,
            margin=ft.Margin(left=0, top=28, right=0, bottom=0)
        )
    
    def add_toolbar(self) -> ft.Container:
        return self.TOOLBAR