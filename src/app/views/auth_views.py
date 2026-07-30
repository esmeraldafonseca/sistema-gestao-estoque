import flet as ft
from ..models.database import get_Connection
from passlib.hash import pbkdf2_sha256
from app.views.home_views import HomeView

class LoginView:
    def __init__(self, page : ft.Page):
        self.user_name = ft.TextField(label="User name")
        self.password = ft.TextField(label="Password", password=True, can_reveal_password=True)
        self.page = page

    def build(self):
        self.page.controls.clear()
        self.page.scroll = None  

        self.page.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text("Login", size=24, weight="bold"),
                    self.user_name,
                    self.password,
                    ft.ElevatedButton("Login", on_click=self._handle_login),
                    ft.ElevatedButton("Cadastrar", on_click=self._handle_register)
                ]),
                alignment=ft.Alignment.CENTER,
                expand=True
            )
        )

        self.page.update()


    def _handle_login(self, event):
        user = self.user_name.value.strip()
        passw = self.password.value.strip()

        if not user or not passw:
            print("Prencha todos os campos")
            return  

        with get_Connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT password FROM usuarios
                WHERE username = ?
            """, (user,))
            resultado = cursor.fetchone() #devolve uma lista

            if resultado and pbkdf2_sha256.verify(passw, resultado[0]): #
                print("Login feito com sucesso!")

                #tela inicial
                home_view = HomeView(self.page)
                home_view.build()

            else:
                print("Nome de utilizador ou senha incorreto")
            conn.commit()

    def _handle_register(self, event):
        user = self.user_name.value.strip()
        passw = self.password.value.strip()

        if not user or not passw:
            print("Prencha todos os campos")
            return  

        hasded_password = pbkdf2_sha256.hash(passw)

        try:
            with get_Connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO usuarios (username, password)
                    VALUES (?, ?)
                """, (user, hasded_password))
                print("Usuario cadastrado com sucesso")
                conn.commit()
        except Exception as E:
            print(f"Erro: {E} ao cadastrar")

