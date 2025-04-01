import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_top(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handle_analizza(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fillddAnno(self):
        for anno in self._model.getAnno():
           self._view._ddAnno.options.append(ft.dropdown.Option(anno))

    def fillddBrand(self):
        for brand in self._model.getBrand():
            self._view._ddBrand.options.append(ft.dropdown.Option(brand))

    def fillddRetail(self):
        for retailer in self._model.getRetail():
            self._view._ddRetail.options.append(ft.dropdown.Option(key=retailer.Retailer_code,
                                                                    text=retailer.Retailer_name,
                                                                    data=retailer,
                                                                    on_click=self.read_retailer))

    def read_retailer(self, e): # memorizza l'intero oggetto retailer del dd nella variabile _retailer
        self._retailer = e.control.data

