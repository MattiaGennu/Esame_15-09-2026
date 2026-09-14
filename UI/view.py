import flet as ft
from UI.alert import AlertManager

class View():
    def __init__(self, page: ft.Page):
        super().__init__()

        self._page = page
        self._page.title = "Programmazione avanzata - Esame del 15 settembre 2026"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT

        self._controller = None

        self._alert = AlertManager(page)

        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None

    def set_controller(self, controller):
        self._controller = controller

    def update_page(self):
        self._page.update()

    def show_alert(self, message):
        self._alert.show_alert(message)

    def load_interface(self):

        self._title = ft.Text("Gestione voli tra Stati", color="blue", size=24)
        self._page.controls.append(self._title)


        self.txtNumVoliMinimo = ft.TextField(label="Numero minimo di voli", width=250)
        self.btnCreaGrafo = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handle_creaGrafo)
        row1 = ft.Row([self.txtNumVoliMinimo, self.btnCreaGrafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.ddStatoPartenza = ft.Dropdown(label="Stato iniziale", width=250, disabled=True)
        self.btnStatiRaggiungibili = ft.ElevatedButton(text="Stati raggiungibili", width=180, disabled=True, on_click=self._controller.handle_statiRaggiungibili)
        row2 = ft.Row([self.ddStatoPartenza, self.btnStatiRaggiungibili],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.txtNumStati = ft.TextField(label="Numero di Stati da visitare", width=250, disabled=True)
        self.btnCercaItinerario = ft.ElevatedButton(text="Cerca itinerario", disabled=True)
        row3 = ft.Row([self.txtNumStati, self.btnCercaItinerario],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()
