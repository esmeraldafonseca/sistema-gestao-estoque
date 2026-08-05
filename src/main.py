import flet as ft
from app.views.auth_views import LoginView
from app.models.database import create_table


from app.models.database import add_fornecedor_column




def main(page: ft.Page):
    create_table()
    page.title ="Sistema de Gestão de Estoque"

    login_views = LoginView(page)
    login_views.build()

    #FAZ ISSO APENAS UMA VEZ E DEPOIS ELIMINA ESSA LINHA
    add_fornecedor_column()
    print("Coluna fornecedor_id adicionada com sucesso!")

if __name__ == "__main__":
    ft.run(main)
