from model.model import Model


def run_test():
    print("--- AVVIO TEST DEL MODEL (METODO RELAZIONALE) ---")

    mio_model = Model()


    print(f"\n[FASE 1] Caricamento nodi...")
    mio_model.load_nodi(350)
    print(f"-> Nodi estratti dal DB: {len(mio_model.nodi_list)}")


    print("\n[FASE 2] Costruzione del Grafo in corso...")
    mio_model.build_graph()

    num_nodi = len(mio_model.grafo.nodes)
    num_archi = len(mio_model.grafo.edges)
    print(f"-> GRAFO COMPLETATO: Nodi = {num_nodi} | Archi = {num_archi}")





    if num_nodi > 0:

        nodo_di_prova = mio_model.nodi_list[0]
        nome_prova = nodo_di_prova.name if hasattr(nodo_di_prova, 'name') else str(nodo_di_prova)
        print(f"2. Test di Analisi sul nodo: {nome_prova}\n")


        discendenti = mio_model.get_nodi_raggiungibili(nodo_di_prova)
        print(f"-> Nodi raggiungibili (Discendenti) partendo da qui: {len(discendenti)}")
        if len(discendenti) > 0:
            for discendente in discendenti:
                nome = discendente.name if hasattr(discendente, 'name') else str(discendente)
                print(f"   - {nome}")

    else:
        print("ATTENZIONE: Il grafo è vuoto! Controlla il parametro o il DAO.")  #

    print("\n--- TEST CONCLUSO ---")


if __name__ == "__main__":
    run_test()
