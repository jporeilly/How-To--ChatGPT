# SQLite3 database for storing conversations
import sqlite3

class ChatGPTDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # Creates a new table in the database
    # The columns need to be a comma-separated str
    def create_table(self, table_name, columns):
        create_table_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})'
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    # Inserts a record into target table with values separated by a comma
    def insert_record(self, table_name, columns, record):
        sql = f'INSERT INTO {table_name} ({columns}) VALUES ({record})' 
        # print(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    # Retrieves all the conversation records from the table
    # Conditions parameter is a str that represents a SQL
    def retrieve_records(self, table_name, conditions=None):
        select_sql = f'SELECT * FROM {table_name}' 
        if conditions:
            select_sql += f'WHERE {conditions}' 
        self.cursor.execute(select_sql) 
        return self.cursor.fetchall()           
    
    def close(self):
        print('database connection closed')
        self.cursor.close()
        self.conn.close()