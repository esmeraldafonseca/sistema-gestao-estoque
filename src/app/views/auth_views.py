import flet as ft

class LoginView:
    def __init__(self, page : ft.Page):
        self.page = page

    def build(self):
        self.page.controls.clear()
        self.page.scroll = None  # <- garante que não há scroll a atrapalhar o expand

        self.page.controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text("Login", size=24, weight="bold"),
                    ft.TextField(label="User name"),
                    ft.TextField(label="Password", password=True, can_reveal_password=True),
                    ft.ElevatedButton("Login")
                ]),
                alignment=ft.Alignment.CENTER,
                expand=True
            )
        )

        self.page.update()
