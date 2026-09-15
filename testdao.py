from database.dao import DAO


print("--- TEST NODI ---")
nodi = DAO.get_nodi(350)
print(f"Trovati {len(nodi)} nodi nel database.")



if len(nodi) > 0:
    print("\n--- TEST COLLEGAMENTI ---")


    id_map = {n.ID: n for n in nodi}

    archi = DAO.get_archi_relazionale(id_map)

    print(f"Trovati {len(archi)} archi pronti per il grafo!")

    for arco in archi[:3]:

        print(f"Arco tra '{arco[0].ID}' e '{arco[1].ID}' | Peso: {arco[2]}")
else:
    print("Nessun nodo trovato, impossibile testare i collegamenti.")



