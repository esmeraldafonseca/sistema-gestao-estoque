import flet as ft
from app.views.auth_views import LoginView
from app.models.database import create_table

def main(page: ft.Page):
    create_table()
    page.title ="Sistema de Gestão de Estoque"

    login_views = LoginView(page)
    login_views.build()
    

if __name__ == "__main__":
    ft.run(main)
