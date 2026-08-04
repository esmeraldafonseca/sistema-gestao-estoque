import flet as ft
from ..models.database import get_Connection

class StockViews:
    def __init__(self, page: ft.Page):
        self.page = page
        self.product_dropdown = ft.Dropdown(label="Produtos", options=[])
        self.product_quantity = ft.TextField(label="Quantidades")

    def build(self):
        self.page.controls.clear()

        self.page.appbar = ft.AppBar(
            title= ft.Text("Stock", size=24, weight="bold"),
            leading= ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self._go_back())
        )

        self.page.add(ft.Column([
            self.product_dropdown,
            self.product_quantity,
            ft.Row([
                ft.ElevatedButton("Adicionar", on_click= self._product_in),
                ft.ElevatedButton("Remover", on_click= self._product_out)
            ], alignment= ft.MainAxisAlignment.CENTER)
        ], expand= True, horizontal_alignment= ft.CrossAxisAlignment.CENTER, alignment= ft.MainAxisAlignment.CENTER)
        )

    def _product_in(self, e):
        pass

    def _product_out(self, e):
        pass

    def _go_back(self):
        from app.views.home_views import HomeView
        home = HomeView(self.page)
        home.build()
