import unittest
from unittest.mock import patch, Mock
from DataBase.Sqlite import Database
from DataBase.TablesData import TableData
import sqlite3
import os


class TestDataBase(unittest.TestCase):

    @staticmethod
    def create_test_table(name:str):
        test_table = f"""CREATE TABLE IF NOT EXISTS {name} ( id INTEGER PRIMARY KEY );"""
        try:
            conn = sqlite3.connect('test.db')
            cur = conn.cursor()
            cur.execute(test_table)
            conn.commit()
        except sqlite3.Error as e:
            raise e
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_all_the_rows(test_table):
        try:
            conn = sqlite3.connect('test.db')
            cur = conn.cursor()
            cur.execute('SELECT * FROM ' + test_table)
            result = cur.fetchall()
        except sqlite3.Error as e:
            return e
        finally:
            if conn:
                conn.close()

        return result

    @staticmethod
    def get_tables_of_test_db():
        """get all tables of the test db"""
        query = """SELECT name FROM sqlite_master WHERE type='table';"""
        
        try:
            conn = sqlite3.connect('test.db')
            cur = conn.cursor()
            cur.execute(query)
            tables = cur.fetchall()
        except sqlite3.Error as e:
            return e
        finally:
            if conn:
                conn.close()
        
        return tables

    @classmethod
    def setUpClass(cls):
        Database.GetDatabasePath = Mock(return_value='test.db')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('test.db'):
            os.remove('test.db')

    def test_Initialize(self):
        Database.Initialize()

        tables = self.get_tables_of_test_db()

        # +1 is for sqlite_sequence table (this table handles autoincrement)
        self.assertEqual(len(tables), len(TableData.Tables) + 1) 

    def test_create_table(self):
        test_table = """CREATE TABLE IF NOT EXISTS test_create_table (
            id INTEGER PRIMARY KEY
            );"""
        
        Database.CreateTable(test_table)
        tables = self.get_tables_of_test_db()
        self.assertIn(('test_create_table',), tables)


    def test_drop_table(self):
        self.create_test_table('test_drop_table')

        Database.DropTable('test_drop_table')
        tables = self.get_tables_of_test_db()

        self.assertNotIn(('test_drop_table',), tables)

    # CRUD test

    def test_create(self):
        self.create_test_table('test_create')

        if Database.Create('test_create', {'id': 10}):
            result = self.get_all_the_rows('test_create')
            self.assertEqual(result, [(10,)])
        else:
            self.fail('Create failed')
        
        
    def test_read(self):
        self.create_test_table('test_read')

        # add tow rows to test_read table with id's 1 and 2
        try:
            conn = sqlite3.connect('test.db')
            cur = conn.cursor()
            records = [(1,), (2,)]
            cur.executemany("INSERT INTO test_read VALUES (?)", records)
            conn.commit()
        except sqlite3.Error as e:
            return e
        finally:
            if conn:
                conn.close()

        # test Database.Read
        first_row = Database.Read('test_read', 'id', 1)
        self.assertListEqual(first_row, [(1,)])

        # test Database.ReadAll
        all_rows = Database.ReadAll('test_read')
        self.assertListEqual(all_rows, [(1,), (2,)])

    def test_update(self):
        self.create_test_table('test_update')

        try:
            conn = sqlite3.connect('test.db')
            cur = conn.cursor()
            records = [(1,), (2,)]
            cur.executemany("INSERT INTO test_update VALUES (?)", records)
            conn.commit()
        except sqlite3.Error as e:
            return e
        finally:
            if conn:
                conn.close()

        Database.Update('test_update', 'id', 1, {'id': 3})
        Database.Update('test_update', 'id', 2, {'id': 4})

        result = self.get_all_the_rows('test_update')
        
        self.assertEqual(result, [(3,), (4,)])


    def test_delete(self):
        self.create_test_table('test_delete')

        try:
            conn = sqlite3.connect('test.db')
            cur = conn.cursor()
            records = [(1,), (2,)]
            cur.executemany("INSERT INTO test_delete VALUES (?)", records)
            conn.commit()
        except sqlite3.Error as e:
            return e
        finally:
            if conn:
                conn.close()

        Database.Delete('test_delete', 'id', 1)

        result = self.get_all_the_rows('test_delete')
        
        self.assertEqual(result, [(2,)])

    def test_create_many(self):
        self.create_test_table('test_create_many')

        records = [(1,), (2,), (3,), (4,)]
        Database.CreateMany('test_create_many', records)

        result = self.get_all_the_rows('test_create_many')
        
        self.assertEqual(result, records)
