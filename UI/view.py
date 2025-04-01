import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddAnno = None
        self._ddBrand = None
        self._ddRetail = None

        self._btnTop = None
        self._btnAnalizza = None

        self.txt_result = None


    def load_interface(self):

        # title

        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        # dropdown: row1

        self._ddAnno = ft.Dropdown(label="anno",width=200, options=[ft.dropdown.Option("Nessun filtro")])
        self._controller.fillddAnno()
        self._ddBrand = ft.Dropdown(label="brand", width=300, options=[ft.dropdown.Option("Nessun filtro")])
        self._controller.fillddBrand()
        self._ddRetail = ft.Dropdown(label="retailer", width=450, options=[ft.dropdown.Option("Nessun filtro")])
        self._controller.fillddRetail()

        row1 = ft.Row([self._ddAnno, self._ddBrand, self._ddRetail], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # button: row2

        self._btnTop = ft.ElevatedButton(text="Top vendite", on_click=self._controller.handle_top)
        self._btnAnalizza =  ft.ElevatedButton(text="Analizza vendite", on_click=self._controller.handle_analizza)

        row2 = ft.Row([self._btnTop, self._btnAnalizza],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed

        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()


