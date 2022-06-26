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
