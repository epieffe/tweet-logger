
class DBConnection:
    """
    Interface representing a generic connection to a RDBMS.
    WARNING: objects of this class are NOT thread safe
    """
    @staticmethod
    def new(**config):
        if config["db_backend"] == "MySQLdb":
            return _MySQLdbConnection(**config)
        
    def update(self, sql, data):
        """
        @sql: string
        @data: list or tuple
        ------
        execute sql query with parameters in data.
        parameters are marked with %s in sql
        """
        pass
        

# following classes are concrete implementations
# of the DBConnection interface
class _MySQLdbConnection(DBConnection):
    """
    Implements DBConnection interface using MySQLdb API.
    WARNING: objects of this class are NOT thread safe
    """
    def __init__(self, **config):
        import MySQLdb
        self.connection = MySQLdb.connect(
            config["db_host"], 
            config["db_user"], 
            config["db_password"], 
            config["db_name"], 
            use_unicode = True,
            charset = "utf8mb4" )
        
    def update(self, sql, data):
        cursor = self.connection.cursor()
        cursor.execute(sql, data)
        self.connection.commit()
        cursor.close()
        
      
