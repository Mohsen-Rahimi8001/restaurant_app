import sqlite3
from sqlite3 import Error


class Database:

    DatabaseName = "database.db"
    DatabaseDir = ".\\"


    @staticmethod
    def GetDatabasePath() -> str:
        """get location of database file"""
        return Database.DatabaseDir + Database.DatabaseName


    @staticmethod
    def Connection():
        """make an sqlite connection"""

        sqlite_file = Database.GetDatabasePath()
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
            handle = connection( Database.GetDatabasePath() )
            curs = handle.cursor()
            curs.execute(SqliteTableData)
            handle.close()

        except Error as e:
            return e