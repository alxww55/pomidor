import flet as ft

class TaskList:
    def __init__(self, white, grey, toolbar_grey):
        self.WHITE = white
        self.BG_GREY = grey
        self.TOOLBAR_GREY = toolbar_grey
        self.TASK_1 = ft.Checkbox(label="TASK1", value=False, label_style=ft.TextStyle(color=self.WHITE, font_family="LexendDeca", size=17), visible=True)
        self.TASK_2 = ft.Checkbox(label="TASK2", value=False, label_style=ft.TextStyle(color=self.WHITE, font_family="LexendDeca", size=17), visible=True)
        self.TASK_3 = ft.Checkbox(label="TASK3", value=False, label_style=ft.TextStyle(color=self.WHITE, font_family="LexendDeca", size=17), visible=True)
        self.TASK_CONTAINER = ft.Container(
            content=ft.Column(
                controls=[
                    self.TASK_1,
                    self.TASK_2,
                    self.TASK_3
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.START
            ),
            width=430,
            height=200,
            margin=ft.Margin(left=0, top=20, right=0, bottom=0),
            padding=ft.Padding(left=20, top=20, right=20, bottom=20)
        )

        self.PLUS_BUTTON = ft.Container(
            content=ft.IconButton(
                icon=ft.Icons.ADD_OUTLINED,
                icon_color=self.BG_GREY,
                width=49,
                height=49,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5), bgcolor=self.WHITE)
            ),
            margin=ft.Margin(-10,0,10,0)
        )

        self.TASK_INPUT = ft.Container(
            content=ft.TextField(
                hint_text="Add a task",
                label_style=ft.TextStyle(color=self.TOOLBAR_GREY, font_family="LexendDeca", size=17),
                text_style=ft.TextStyle(color=self.TOOLBAR_GREY, font_family="LexendDeca", size=17),
                focused_border_color=self.WHITE,
                border_color=self.TOOLBAR_GREY,
                color=self.WHITE,
                width=300
            ),
            margin=ft.Margin(59,0,0,0)
        )

        self.TASK_INPUT_CONTAINER = ft.Container(content=ft.Row(controls=[self.TASK_INPUT, self.PLUS_BUTTON], vertical_alignment=ft.CrossAxisAlignment.CENTER), margin=ft.Margin(left=0, top=0, right=0, bottom=50))
        
        self.TASKLIST_CONTAINER = ft.Column(controls=[self.TASK_CONTAINER, self.TASK_INPUT_CONTAINER])

    def add_task_list(self) -> ft.Container:
        return self.TASKLIST_CONTAINER