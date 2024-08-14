import psycopg2

class Conexion:
    
    """Metodo constructor
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=veterinaria-db user=postgres password=Filter777")
    
        """getConexion
        
            retorna la in stancia de la base de datos
        """
    def getConexion(self):
       return self.con