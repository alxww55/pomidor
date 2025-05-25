import flet as ft

class WindowBar:
    def __init__(self, white, acc_grey, red, window, page: ft.Page):
        self.WHITE = white
        self.ACC_GREY = acc_grey
        self.RED = red
        self.WINDOW = window
        self.WINDOW_BAR = ft.WindowDragArea(
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src="icon.png", width=30, height=30
                            )
                        ),
                        ft.Container(
                            content=ft.Text(
                                value="Pomidor", font_family="LexendDeca", size=20, color=self.WHITE
                            ),
                            padding=ft.Padding(left=9, top=0, right=300, bottom=0)
                        ),
                        ft.Container(
                            content=ft.Icon(
                                ft.Icons.CLOSE, color=self.RED, size=30),
                                margin=ft.Margin(left=0, top=0, right=9, bottom=0),
                                on_click=lambda e: self.WINDOW.close()
                        )
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                bgcolor=self.ACC_GREY,
                height=49,
                width=470,
                padding=ft.Padding(left=9, top=0, right=9, bottom=0),
                margin=0
            )
        )
    
    def add_window_bar(self) -> ft.WindowDragArea:
        return self.WINDOW_BAR
