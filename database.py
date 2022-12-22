import sqlite3

class DB_ACTION:
    "Basic database actions"
    def __init__(self, db_file:str, table_name:str)->None:
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file, check_same_thread = False)
        self.cur = self.conn.cursor()
        self.table_name = table_name

    def create_database(self):
        self.conn.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name}
                (ID         INT PRIMARY KEY NOT NULL);''') #You should alter columns to create more of them.
        self.conn.commit()

    def column_info(self, search:str)->list:
        info_list = []
        data = self.conn.execute(f"SELECT {search} FROM [{self.table_name}]")
        for info in data:
            info_list.append(info[0])
        return info_list

    def add_column(self, col_name:str, col_type:str):
        self.conn.execute(f"ALTER TABLE {self.table_name} ADD COLUMN {col_name} '{col_type}'")
        self.conn.commit()
    
    def total_entry(self)->int:
        data = self.conn.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        for [count] in data:
            return count