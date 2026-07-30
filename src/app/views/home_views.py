import flet as ft

class HomeView:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        self.page.controls.clear()

        self.page.drawer = ft.NavigationDrawer(
            controls=[
                ft.Container(height=50),
                ft.NavigationDrawerDestination(icon=ft.Icons.HOME, label="Dashboard"),
                ft.NavigationDrawerDestination(icon=ft.Icons.INVENTORY, label="Produtos"),
                ft.NavigationDrawerDestination(icon=ft.Icons.LOCAL_SHIPPING, label="Fornecedores"),
                ft.NavigationDrawerDestination(icon=ft.Icons.STORAGE, label="Estoque"),
                ft.NavigationDrawerDestination(icon=ft.Icons.LOGOUT, label="Sair")
            ]
            )

        self.page.appbar = ft.AppBar(
            title= ft.Text("SGE", 
                           size=24, weight="bold"),
            leading= ft.IconButton(icon= ft.Icons.MENU, on_click= lambda e: self._open_drawer())
        )

        self.page.add(
            ft.Column([
                ft.Text("Bem-vinda(o) ao sistema de gestão de estoque", size=20)
            ])
        )

        self.page.update()


    def _open_drawer(self, event=None):
        self.page.run_task(self._show_drawer)
        self.page.drawer.on_change = self._navegate 

    async def _show_drawer(self):
        await self.page.show_drawer()

    def _navegate(self, e):
        #dashbord
        if self.page.drawer.selected_index == 0:
            pass

        #product
        elif self.page.drawer.selected_index == 1:
            from app.views.product_views import ProductView
            prducts = ProductView(self.page)
            prducts.build()
            
        #suppliers
        elif self.page.drawer.selected_index == 2:
            pass

        #stock
        elif self.page.drawer.selected_index == 3:
            pass       

        #logout
        elif self.page.drawer.selected_index == 4:
            pass
     