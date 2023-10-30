import sqlite3, os

class DB_SNAKE:

    def __init__(self):
        self.database_name = 'DB/snakegame.db'

    def open_connection(self):
        self.conn = sqlite3.connect(self.database_name)
        self.cur = self.conn.cursor()

    def execute(self, sql):
        if os.path.isfile(sql):
            with open(sql, 'r') as file:
                sql_script = file.read()
            self.cur.executescript(sql_script)  
            return self.cur.fetchall()  
        else:
            self.cur.execute(sql)
            return self.cur.fetchone()
            
        
    def close_connection(self):
        self.conn.commit()
        self.conn.close()

'''
db_snake = DB_SNAKE()
db_snake.open_connection()
db_snake.execute("DB/alter_tabel.sql")
db_snake.close_connection()
'''
