import flet as ft
from app import PomidorApp

def main(page: ft.Page):
    app = PomidorApp(page)
    app.load_window_bar(page)
    app.load_timer(page)
    app.load_task_list(page)

ft.app(target=main, assets_dir="assets")