from manter.database import Database

class DaoCliente:
    """
    dao == Data Access Object ou persistence
    Implementa operacoes "CRUD"
        - Create
        - Read
        - Update
        - Delete
    """
    def save(self, cliente):    # C
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO cliente (nome, cpf, email )
            VALUES (?, ?, ?)
            """,
            ( cliente.nome, cliente.cpf, cliente.email )
        )
        conn.commit()

    def find(self):    # R
        pass
    def update(self):  # U
        pass
    def delete(self):  # D
        pass
    def findall(self): # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM cliente"
        )
        return res.fetchall()
