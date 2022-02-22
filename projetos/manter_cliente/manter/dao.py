
class DaoCliente:
    """
    dao == Data Access Object ou persistence
    Implementa operacoes "CRUD"
        - Create
        - Read
        - Update
        - Delete
    """
    def save(self):    # C
        pass
    def find(self):    # R
        pass
    def update(self):  # U
        pass
    def delete(self):  # D
        pass
    def findall(self): # R
        # pegar da Database a conexao com o BD
        from manter.database import Database
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM cliente"
        )
        return res.fetchall()
