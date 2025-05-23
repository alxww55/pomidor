import flet as ft

class PomidorApp:
    def __init__(self, page: ft.Page):
        self.BG_GREY = "#1E1E1E"
        self.ACC_GREY = "#252525"
        self.RED = "#F44336"
        page.route = "/concentration"
        page.window.width = 470
        page.window.height = 685
        page.bgcolor = self.BG_GREY
        page.spacing = 0
        page.padding = 0
        page.window.maximizable = False
        page.window.frameless = True
        #page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.fonts = {"LexendDeca": "./fonts/LexendDeca-Regular.ttf"}
        page.update()

    def window_bar(self, page: ft.Page):
        BOTTOM_BAR = ft.WindowDragArea(
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(content=ft.Image(src="icon.png", width=30, height=30)),
                        ft.Container(content=ft.Text(value="Pomidor", font_family="LexendDeca", size=20), padding=ft.Padding(left=9, top=0, right=310, bottom=0)),
                        ft.Container(content=ft.Icon(ft.Icons.CLOSE, color=self.RED, size=30), margin=ft.Margin(left=0, top=0, right=9, bottom=0), on_click=lambda e: page.window.close())
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
        page.add(BOTTOM_BAR)
        page.update()



def main(page: ft.Page):
    app = PomidorApp(page)
    app.window_bar(page)
    return app