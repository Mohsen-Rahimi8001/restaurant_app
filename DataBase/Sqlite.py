import sqlite3
from sqlite3 import Error
from DataBase.TablesData import TableData

class Database:

    DatabaseName = "database.db"
    DatabaseDir = "./DataBase/"


    @staticmethod
    def GetDatabasePath() -> str:
        """get location of database file"""
        return Database.DatabaseDir + Database.DatabaseName


    @staticmethod
    def Connection():
        """make an sqlite Database.Connection"""

        sqlite_file : str = Database.GetDatabasePath()
        if not sqlite_file:
            return

        connection = None

        try:
            connection = sqlite3.connect(sqlite_file)
            return connection

        except Error as e:
            return e


    @staticmethod
    def CreateTable(SqliteTableData : str):
        """add table to database"""

        try:
            handle = Database.Connection()
            curs = handle.cursor()
            curs.execute(SqliteTableData)
            handle.close()

        except Error as e:
            return e


    @staticmethod
    def Initialize():
        """create all database tables"""

        for tableData in TableData.Tables:
            Database.CreateTable(tableData)


    @staticmethod
    def DropTable(table : str):
        """delete table form database"""

        query = """DROP TABLE IF EXISTS {tablename}""".format(tablename=table)

        try:
            handle = Database.Connection()
            curs = handle.cursor()
            curs.execute(query)
            handle.commit()
            handle.close()

        except Error as e:
            return e




    # CRUD functions

    @staticmethod
    def Create(table : str, data : dict):
        """add new row to table"""

        data = dict(data)
        if not data:
            return False

        query = """ INSERT INTO {tablename} {keys} VALUES {values}""".format(tablename=table, keys=tuple(data),
                                                                             values=tuple(data.values()))
        try:
            handle = Database.Connection()
            curs = handle.cursor()
            curs.execute(query)
            handle.commit()
            handle.close()
            return curs.lastrowid

        except Error as e:
            return e


    @staticmethod
    def Read(table : str, key : str, value):
        """get a row from data base where key(column) == value"""

        query = """SELECT * FROM {tablename} WHERE {key} = '{value}'""".format(tablename=table, key=key, value=value)

        try:
            handle = Database.Connection()
            curs = handle.cursor()
            curs.execute(query)
            row = curs.fetchall()
            handle.close()
            return row


        except Error as e:
            return e


    @staticmethod
    def ReadAll(table : str) -> list:
        """get all records of a table"""

        query = """SELECT * FROM {tablename} """.format(tablename=table)

        try:
            handle = Database.Connection()
            curs = handle.cursor()
            curs.execute(query)
            rows = curs.fetchall()
            handle.close()
            return rows

        except Error as e:
            return e


    @staticmethod
    def Exists(table : str, key : str, value) -> bool:
        """check if row with key(column) == value exists or not"""

        query = """SELECT * FROM {tablename} WHERE {key} = '{value}'""".format(tablename=table, key=key, value=value)

        try:
            handle = Database.Connection()
            curs = handle.cursor()
            curs.execute(query)
            row = curs.fetchall()
            handle.close()
            return bool(row)

        except Error as e:
            return e


    @staticmethod
    def Update(table : str, key : str, value, data : dict):
        """update row where key(column) == value"""

        data = dict(data)
        if not data:
            return False

        #columns to update
        items = str()
        for k, v in data.items():
            items += f" {k} = '{v}' , "

        query = """UPDATE {tablename} SET {items} WHERE {in_key} = '{in_value}'""".format(tablename=table,
                                                                                          items=items[1:len(items) - 2],
                                                                                          in_key=key, in_value=value)

        try:
            handle = Database.Connection()
            curs = handle.cursor()
            curs.execute(query)
            handle.commit()
            handle.close()

        except Error as e:
            return e


    @staticmethod
    def Delete(table : str, key : str, value):
        "delete row where key(column) == value"

        query = """DELETE  FROM {tablename} WHERE {in_key} = '{in_value}'""".format(tablename=table, in_key=key,
                                                                                    in_value=value)
        try:
            handle = Database.Connection()
            curs = handle.cursor()
            curs.execute(query)
            handle.commit()
            handle.close()

        except Error as e:
            return e


    @staticmethod
    def Flush(table : str):
        """clear table"""

        query = """DELETE FROM {tablename}""".format(tablename=table)

        try:
            handle = Database.Connection()
            curs = handle.cursor()
            curs.execute(query)
            handle.commit()
            handle.close()

        except Error as e:
            return e