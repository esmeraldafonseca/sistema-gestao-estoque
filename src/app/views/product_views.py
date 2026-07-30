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
        name = self.product_name.value.strip()
        #força os dados a terem os tipos que precisamos
        try:    
            price = float(self.product_price.value.strip())
            quantity = int(self.product_quantity.value.strip())
        except:
            print("Valor invalido, insira apenas numeros nos campos preço e quantidade")
            return

        if not name:
            print("Prencha o nome do produto")
            return

        with get_Connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO produtos 
                (name, price, quatity) 
                VALUES (?,?,?)
                """, (name, price, quantity))
            
            conn.commit()
            print("Produto cadastrado com sucesso!")

            self.product_name.value = ""
            self.product_price.value = ""
            self.product_quantity.value = ""

            self.page.update()
    
    def _go_back(self):
        from app.views.home_views import HomeView
        home = HomeView(self.page)
        home.build()
