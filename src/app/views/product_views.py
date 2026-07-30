import flet as ft
from ..models.database import get_Connection

class ProductView:
    def __init__(self, page : ft.Page):
        self.page = page
        self.product_name = ft.TextField(label="Nome do produto")
        self.product_price = ft.TextField(label="Preço do produto")
        self.product_quantity = ft.TextField(label="Quantidade do produto")

        

    def build(self):
        self.page.controls.clear()

        self.page.appbar = ft.AppBar(
            title= ft.Text("Cadastro de produtos", size=24, weight="bold"),
            leading= ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self._go_back())
        )

        self.page.add(
            ft.Column([
                self.product_name,
                self.product_price,
                self.product_quantity,
                ft.Row([
                    ft.ElevatedButton("Cadastrar produto", on_click= self._register_product)
                ])
            ])
        )


    def _register_product(self, event):
        pass

    
    def _go_back(self):
        from app.views.home_views import HomeView
        home = HomeView(self.page)
        home.build()
