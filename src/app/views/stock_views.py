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
        self._fetch_product()

        self.page.add(ft.Column([
            self.product_dropdown,
            self.product_quantity,
            ft.Row([
                ft.ElevatedButton("Adicionar", on_click= self._product_in),
                ft.ElevatedButton("Remover", on_click= self._product_out)
            ], alignment= ft.MainAxisAlignment.CENTER)
        ], expand= True, horizontal_alignment= ft.CrossAxisAlignment.CENTER, alignment= ft.MainAxisAlignment.CENTER)
        )

    def _fetch_product(self):
        self.product_dropdown.options.clear()

        with get_Connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM produtos")
            for id_product, name in cursor.fetchall():
                self.product_dropdown.options.append(
                    ft.dropdown.Option(str(id_product), name)
                )
        self.page.update()



    def _refresh_stock(self, procuct_in: True):
        id_product = self.product_dropdown.value

        if not id_product :
            print("Selecione um produto")
            return

        try:
            quantity = int (self.product_quantity.value)
            if quantity <=0:
                raise ValueError
        except:
            print("Digite uma quantidade valida")
            return

        with get_Connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                        SELECT quantity FROM produtos
                        WHERE id = ?
                    """, (id_product))
            result = cursor.fetchone()

            if not result:
                print("Produto não encontrado")
                return

            current_quantity =result[0]
            new_quantity = current_quantity + quantity if procuct_in else current_quantity - quantity

            if new_quantity < 0:
                print("Quantidade indisponivel")
                return

            cursor.execute("""
                    UPDATE produtos SET quantity = ?
                    WHERE id = ?
                        """, (new_quantity, id_product))

            conn.commit()
            print("Estoque actualizado com sucesso!")
            self.product_quantity.value =""
            self.page.update()

        

    def _product_in(self):
        self._refresh_stock(True)

    def _product_out(self):
        self._refresh_stock(product_in = False)
        

    def _go_back(self):
        from app.views.home_views import HomeView
        home = HomeView(self.page)
        home.build()
