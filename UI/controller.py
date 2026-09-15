import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self._nodo_selezionato = None

    def handle_creaGrafo(self, e):

        try:
            parametro_utente = float(self._view.txtNumVoliMinimo.value)
        except ValueError:
            self._view.show_alert("Attenzione: Inserire un valore numerico valido!")
            return

        if parametro_utente < 1:
         self._view.show_alert("Attenzione: Inserire un valore numerico non negativo!")
         return


        self._model.load_nodi(parametro_utente)
        self._model.build_graph()

        self._view.txt_result.controls.clear()
        num_nodi = len(self._model.grafo.nodes)
        num_archi = len(self._model.grafo.edges)
        self._view.txt_result.controls.append(ft.Text(f"Nodi: {num_nodi} | Archi: {num_archi}"))
        self._view.update_page()




        self._view.ddStatoPartenza.options.clear()
        for nodo in self._model.grafo.nodes:
            self._view.ddStatoPartenza.options.append(ft.dropdown.Option(key=str(nodo.ID), text=nodo.STATE))
        self._view.update_page()

    def handle_statiRaggiungibili(self, e):

        if self._view.ddStatoPartenza.value is None:
            self._view.show_alert("Attenzione: Selezionare prima uno stato dal menu a tendina!")
            return

        id_selezionato = int(self._view.ddStatoPartenza.value)
        self._nodo_selezionato = self._model.id_map[id_selezionato]

        componente = self._model.get_nodi_raggiungibili(self._nodo_selezionato)


        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero stati raggiungibili: {len(componente)} "))


        self._view.update_page()





