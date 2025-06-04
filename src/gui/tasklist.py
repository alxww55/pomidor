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
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                width=430
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
            margin=ft.Margin(40,0,0,0)
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
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            width=430
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
            new_task = ft.Row(
                controls=[
                    ft.Checkbox(
                        label="",
                        value=False,
                        label_style=ft.TextStyle(
                            color=self.WHITE,
                            font_family="LexendDeca",
                            size=17
                        ),
                        on_change=self.task_line_through
                    ), ft.Row(
                        controls=[
                            ft.IconButton(
                            icon=ft.Icons.EDIT,
                            icon_size=17,
                            tooltip="Edit",
                            icon_color=self.WHITE,
                            on_click=self.edit_task
                        ), ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_size=17,
                            tooltip="Delete",
                            icon_color=self.WHITE,
                            on_click=self.delete_task
                            )
                        ]
                    )
                ], 
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )

            new_task.controls[0].label = self.TASK_INPUT_FIELD.value
            self.TASKS_COLUMN.controls.append(new_task)
            self.TASK_INPUT_FIELD.value = ""
            self.page.update()
            return
        
    def task_line_through(self, e):
        for task in self.TASKS_COLUMN.controls:
            if task.controls[0].value:
                task.controls[0].label_style.decoration = ft.TextDecoration.LINE_THROUGH
                task.controls[0].label_style.decoration_color = self.WHITE
                task.controls[0].opacity = 0.5
                task.controls[0].label_style.decoration_thickness = 3
            else:
                task.controls[0].label_style.decoration = None
                task.controls[0].label_style.decoration_color = None
                task.controls[0].opacity = 1
                task.controls[0].label_style.decoration_thickness = None
        self.page.update()
        return
    
    def delete_task(self, e):
        for task in self.TASKS_COLUMN.controls:
            if e.control == task.controls[1].controls[1]:
                self.TASKS_COLUMN.controls.remove(task)
                self.page.update()
                return
            
    def edit_task(self, e):
        for task in self.TASKS_COLUMN.controls:
            if e.control == task.controls[1].controls[0]:
                current_text = task.controls[0].label
                edit_field = ft.TextField(
                    value=current_text,
                    autofocus=True,
                    text_style=ft.TextStyle(font_family="LexendDeca"),
                    on_submit=lambda evt, t=task: self.save_edited_task(evt, t)
                )
                task.controls[0].visible = False
                task.controls.insert(1, edit_field)
                self.page.update()
                return

    def save_edited_task(self, e, task):
        new_text = e.control.value
        task.controls[0].label = new_text
        task.controls[0].visible = True
        task.controls.pop(1)
        self.page.update()