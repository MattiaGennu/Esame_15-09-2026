import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.nodi_list = []
        self.id_map = {}



    def load_nodi(self, parametro):
        self.nodi_list = DAO.get_nodi(parametro)
        self.id_map = {n.ID: n for n in self.nodi_list}


    def build_graph(self):
        self.grafo.clear()
        self.grafo.add_nodes_from(self.nodi_list)
        lista_archi = DAO.get_archi_relazionale(self.id_map)


        for arco in lista_archi:
            n1 = arco[0]
            n2 = arco[1]
            peso = arco[2]

            self.grafo.add_edge(n1, n2, weight=peso)




    def get_nodi_raggiungibili(self, nodo):

        if nodo not in self.grafo:
            return []
        return list(nx.descendants(self.grafo, nodo))

        nodo(key=lambda x: x[0].id) #,reverse=True ordine decrescente
        # ORDINE DECRESCENTE PER PESO DELL'ARCO (se il prof lo chiedesse!):
         # x[1] significa "guarda il secondo elemento della coppia", cioè il peso!
         #vicini_con_peso.sort(key=lambda x: x[1], reverse=True)
        return vicini_con_peso




