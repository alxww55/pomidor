import flet as ft
import time

class TaskList:
    def __init__(self, white, grey, red, toolbar_grey, page):
        self.page = page
        self.WHITE = white
        self.BG_GREY = grey
        self.RED = red
        self.TOOLBAR_GREY = toolbar_grey

        self.TASKS_COLUMN = ft.Column(
                controls=[],
                spacing=10,
                alignment=ft.MainAxisAlignment.START
        )

        self.TASK_CONTAINER = ft.Container(
            content=self.TASKS_COLUMN,
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
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5), bgcolor=self.WHITE),
                on_click=self.add_task
            ),
            margin=ft.Margin(-10,0,10,0)
        )

        self.TASK_INPUT_FIELD = ft.TextField(
                hint_text="Add a task",
                width=300,
                label_style=ft.TextStyle(color=self.TOOLBAR_GREY, font_family="LexendDeca", size=17),
                text_style=ft.TextStyle(color=self.TOOLBAR_GREY, font_family="LexendDeca", size=17),
                focused_border_color=self.WHITE,
                border_color=self.TOOLBAR_GREY,
                color=self.WHITE,
                on_submit=self.add_task
        )

        self.TASK_INPUT_FIELD_CONTAINER = ft.Container(
            content=self.TASK_INPUT_FIELD,
            margin=ft.Margin(59,0,0,0)
        )

        self.TASK_INPUT_CONTAINER = ft.Container(
            content=ft.Row(
                controls=[
                    self.TASK_INPUT_FIELD_CONTAINER,
                    self.PLUS_BUTTON
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER),
                margin=ft.Margin(left=0, top=0, right=0, bottom=50
            )
        )
        
        self.TASKLIST_CONTAINER = ft.Column(
            controls=[
                self.TASK_CONTAINER,
                self.TASK_INPUT_CONTAINER
            ]
        )

    def add_task_list(self) -> ft.Container:
        return self.TASKLIST_CONTAINER
    

    def add_task(self, e):
        self.TASK_INPUT_FIELD.border_color = self.TOOLBAR_GREY
        self.TASK_INPUT_FIELD.hint_text = "Add a task"
        if self.TASK_INPUT_FIELD.value == "":
            self.TASK_INPUT_FIELD.border_color = self.RED
            self.TASK_INPUT_FIELD.hint_text = "You need to enter something!"
            self.page.update()
            time.sleep(1.5)
            self.TASK_INPUT_FIELD.border_color = self.TOOLBAR_GREY
            self.TASK_INPUT_FIELD.hint_text = "Add a task"
            self.page.update()
            return
            
        if len(self.TASKS_COLUMN.controls) == 4:
            self.TASK_INPUT_FIELD.border_color = self.RED
            self.TASK_INPUT_FIELD.value = ""
            self.TASK_INPUT_FIELD.hint_text = "It's too much for the one time!"
            self.page.update()
            time.sleep(1.5)
            self.TASK_INPUT_FIELD.border_color = self.TOOLBAR_GREY
            self.TASK_INPUT_FIELD.hint_text = "Add a task"
            self.page.update()
            return
            
        else:
            new_task = ft.Checkbox(label="", value=False, label_style=ft.TextStyle(color=self.WHITE, font_family="LexendDeca", size=17), visible=True)
            new_task.label = self.TASK_INPUT_FIELD.value
            self.TASKS_COLUMN.controls.append(new_task)
            self.TASK_INPUT_FIELD.value = ""
            # if new_task.value:
            #     new_task.label_style.decoration=ft.TextDecoration.LINE_THROUGH
            #     new_task.label_style.decoration_color=self.TOOLBAR_GREY
            #     new_task.label_style.decoration_thickness=4
            #     self.page.update()
            self.page.update()
            return
        