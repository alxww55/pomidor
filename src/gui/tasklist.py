import flet as ft

class TaskList:
    def __init__(self, white):
        self.WHITE = white
        self.TASK_1 = ft.Checkbox(label="HELLO", value=False, label_style=ft.TextStyle(color=self.WHITE, font_family="LexendDeca", size=17), visible=True)
        self.TASK_2 = ft.Checkbox(label="TASK2", value=False, label_style=ft.TextStyle(color=self.WHITE, font_family="LexendDeca", size=17), visible=True)
        self.TASK_3 = ft.Checkbox(label="e3e3", value=False, label_style=ft.TextStyle(color=self.WHITE, font_family="LexendDeca", size=17), visible=True)
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
            padding=ft.Padding(left=20, top=26, right=20, bottom=20)
        )
        self.TASK_INPUT = ft.Row(
            controls=[
                ft.TextField(
                label="Add a task",
                label_style=ft.TextStyle(color=self.WHITE, font_family="LexendDeca", size=17),
                border_color=self.WHITE,
                color=self.WHITE,
                width=390,
                height=56
                ),
                ft.IconButton
            ]
        )
        
        
        self.TASKLIST_CONTAINER = ft.Column(controls=[self.TASK_CONTAINER, self.TASK_INPUT], alignment=ft.MainAxisAlignment.CENTER)

    def add_task_list(self) -> ft.Container:
        return self.TASKLIST_CONTAINER