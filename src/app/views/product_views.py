import flet as ft
from ..models.database import get_Connection


class ProductView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.product_name = ft.TextField(label="Nome do produto")
        self.product_price = ft.TextField(label="Preço do produto")
        self.product_quantity = ft.TextField(label="Quantidade do produto")
        self.supplier_dropdown = ft.Dropdown(label="Fornecedor", options=[])
        self.list_product = ft.ListView()

    def build(self):
        self.page.controls.clear()

        self.page.appbar = ft.AppBar(
            title=ft.Text("Cadastro de produtos", size=24, weight="bold"),
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self._go_back())
        )

        self._fetch_suppliers()

        self.page.add(
            ft.Column([
                self.product_name,
                self.product_price,
                self.product_quantity,
                self.supplier_dropdown,
                ft.Row([
                    ft.ElevatedButton("Cadastrar produto", on_click=self._register_product)
                ]),
                ft.Divider(),
                ft.Text("Produtos cadastrados", size=20),
                self.list_product
            ], expand=True, alignment=ft.Alignment.CENTER)
        )

        self.products_list()
        self.page.update()

    def _fetch_suppliers(self):
        self.supplier_dropdown.options.clear()

        with get_Connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM fornecedores")
            for supplier_id, supplier_name in cursor.fetchall():
                self.supplier_dropdown.options.append(
                    ft.dropdown.Option(key=str(supplier_id), text=supplier_name)
                )

    def _register_product(self, event):
        name = self.product_name.value.strip()
        selected_supplier_id = self.supplier_dropdown.value

        try:
            price = float(self.product_price.value.strip())
            quantity = int(self.product_quantity.value.strip())
        except ValueError:
            print("Valor invalido, insira apenas numeros nos campos preço e quantidade")
            return

        if not name:
            print("Prencha o nome do produto")
            return

        if not selected_supplier_id:
            print("Selecione um fornecedor")
            return

        with get_Connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO produtos 
                (name, price, quatity, fornecedor_id) 
                VALUES (?,?,?,?)
                """, (name, price, quantity, selected_supplier_id))

            conn.commit()
            print("Produto cadastrado com sucesso!")

            self.product_name.value = ""
            self.product_price.value = ""
            self.product_quantity.value = ""
            self.supplier_dropdown.value = None

        self.products_list()
        self.page.update()

    def _go_back(self):
        from app.views.home_views import HomeView
        home = HomeView(self.page)
        home.build()

    def products_list(self):
        self.list_product.controls.clear()

        with get_Connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT name, price, quatity 
                FROM produtos
            """)
            for name, price, quantity in cursor.fetchall():
                price = float(price)
                quantity = int(quantity)
                self.list_product.controls.append(
                    ft.ListTile(
                        title=ft.Text(name),
                        subtitle=ft.Text(f"Preço: {price:.2f}KZ | Quantidade: {quantity}")
                    )
                )
            self.page.update()