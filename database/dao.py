from database.DB_connect import DBConnect
from model.airport import Airport

class DAO:
    @staticmethod
    def get_nodi(parametro):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = '''select a.ID, a.STATE, a.AIRPORT, count(f.ID) as n_voli
                    from airports a, flights f
                    where a.ID=f.ORIGIN_AIRPORT_ID or a.ID=f.DESTINATION_AIRPORT_ID 
                    group by a.ID, a.STATE, a.AIRPORT 
                    having n_voli>=%s'''

        cursor.execute(query,(parametro,))

        for row in cursor:
            airport=Airport(ID=row['ID'], STATE=row['STATE'], AIRPORT=row['AIRPORT'], n_voli=row['n_voli'])
            result.append(airport)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_archi_relazionale(id_map):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)


        query = """
     select f1.ORIGIN_AIRPORT_ID as n1, f2.DESTINATION_AIRPORT_ID as n2, count(*) as voli
    from flights f1, flights f2, airports a1, airports a2  
    where a1.ID=f1.ORIGIN_AIRPORT_ID and a2.ID=f2.DESTINATION_AIRPORT_ID 
    and f1.ID=f2.ID  
    and f1.ORIGIN_AIRPORT_ID < f2.DESTINATION_AIRPORT_ID
    group by f1.ORIGIN_AIRPORT_ID, f2.DESTINATION_AIRPORT_ID 


                """


        cursor.execute(query)

        for row in cursor:

            n1 = id_map.get(row["n1"])
            n2 = id_map.get(row["n2"])
            voli = row["voli"]


            if n1 and n2:
                result.append((n1, n2, voli))

        cursor.close()
        conn.close()
        return result

