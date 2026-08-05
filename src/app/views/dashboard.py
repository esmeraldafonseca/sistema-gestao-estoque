import flet as ft
import matplotlib.pyplot as plt
import io
import base64
from ..models.database import get_Connection


class DashboardViews:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        self.page.controls.clear()

        self.page.appbar = ft.AppBar(
            title=ft.Text("Dashboard", size=24, weight="bold"),
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self._go_back())
        )

        stock_chart_image = ft.Image(
            src=self._build_stock_chart(),
            width=450,
            height=300
        )
        supplier_chart_image = ft.Image(
            src=self._build_supplier_chart(),
            width=450,
            height=300
        )

        self.page.add(ft.Column([
            ft.Text("Produtos com menos stock", size=18, weight="bold"),
            stock_chart_image,
            ft.Divider(),
            ft.Text("Produtos por fornecedor", size=18, weight="bold"),
            supplier_chart_image,
        ], scroll=ft.ScrollMode.AUTO)
        )

    def _build_stock_chart(self) -> str:
        with get_Connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT name, quatity
                FROM produtos
                ORDER BY quatity ASC
                LIMIT 5
            """)
            product_rows = cursor.fetchall()

        product_names = [row[0] for row in product_rows]
        product_quantities = [row[1] for row in product_rows]

        chart, chart_area = plt.subplots()
        chart_area.bar(product_names, product_quantities, color="#4C72B0")
        chart_area.set_ylabel("Quantidade")
        chart_area.set_title("5 produtos com menor stock")
        plt.xticks(rotation=30, ha="right")
        chart.tight_layout()

        return self._chart_to_image_src(chart)

    def _build_supplier_chart(self) -> str:
        with get_Connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT fornecedores.name, COUNT(produtos.id)
                FROM produtos
                JOIN fornecedores ON produtos.fornecedor_id = fornecedores.id
                GROUP BY fornecedores.name
            """)
            supplier_rows = cursor.fetchall()

        supplier_names = [row[0] for row in supplier_rows]
        product_counts = [row[1] for row in supplier_rows]

        chart, chart_area = plt.subplots()
        chart_area.pie(product_counts, labels=supplier_names, autopct="%1.0f%%")
        chart_area.set_title("Distribuição de produtos por fornecedor")

        return self._chart_to_image_src(chart)

    def _chart_to_image_src(self, chart: plt.Figure) -> str:
        memory_buffer = io.BytesIO()
        chart.savefig(memory_buffer, format="png", bbox_inches="tight")
        memory_buffer.seek(0)
        base64_text = base64.b64encode(memory_buffer.read()).decode("utf-8")
        plt.close(chart)
        return f"data:image/png;base64,{base64_text}"

    def _go_back(self):
        from app.views.home_views import HomeView
        home = HomeView(self.page)
        home.build()