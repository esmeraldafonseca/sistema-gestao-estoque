import flet as ft
from ..models.database import get_Connection

class SupplierView:
    def __init__(self, page : ft.Page):
        self.page = page
        self.supplier_name = ft.TextField(label="Nome do fornecerdor")
        self.supplier_conctat = ft.TextField(label="Telefone")
        self.supplier_email = ft.TextField(label="Email")
        self.list_supplier = ft.ListView()

        

    def build(self):
        self.page.controls.clear()

        self.page.appbar = ft.AppBar(
            title= ft.Text("Fornecedores", size=24, weight="bold"),
            leading= ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self._go_back())
        )

        self.page.add(
            ft.Column([
                self.supplier_name,
                self.supplier_conctat,
                self.supplier_email,
                ft.Row([
                    ft.ElevatedButton("Cadastrar de fornecedores", on_click= self._register_supplier)
                    ]),
                ft.Divider(),
                ft.Text("Fornecedores cadastrados", size=20),
                self.list_supplier,
            ], expand=True, alignment= ft.Alignment.CENTER)
        )

        self.supplier_list()
        self.page.update()

    def _register_supplier(self, event):
        name = self.supplier_name.value.strip()
        email = self.supplier_email.value.strip()
        
        try:    
            conctat = int(self.supplier_conctat.value.strip())
        except:
            print("Valor invalido, insira apenas numeros.")
            return

        if not name or not email:
            print("Prencha todos os campos")
            return

        with get_Connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO fornecedores
                (name, contact, email) 
                VALUES (?,?,?)
                """, (name, conctat, email))
            
            conn.commit()
            print("Fornecedor cadastrado com sucesso!")

            self.supplier_name.value = ""
            self.supplier_conctat.value = ""
            self.supplier_email.value = ""

            self.supplier_list()
            self.page.update()
    
    def _go_back(self):
        from app.views.home_views import HomeView
        home = HomeView(self.page)
        home.build()


    def supplier_list(self):
        self.list_supplier.controls.clear()

        with get_Connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT name, contact, email 
                FROM fornecedores
            """)
            for name, contact, email in cursor.fetchall():
            
                self.list_supplier.controls.append(
                    ft.ListTile(
                        title=ft.Text(name), 
                        subtitle= ft.Text(f"Contato: +244{contact} | email: {email}")
                    )
                )
                self.page.update()
