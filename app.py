import sqlite3
path = 'C:\\database.db'

class AgendaBD:
    def __init__(self, arquivo):
        self.comunication = sqlite3.connect(arquivo) 
        self.cursor= self.comunication.cursor() 

    def inserir(self, name, tel):
        query = 'INSERT OR IGNORE INTO agenda (name, tel) VALUE (?, ?)'
        self.cursor.execute(query, (name, tel))
        self.comunication.commit() 

    def edit(self, name, tel, id):
        query = 'UPDATE OR IGNORE agenda SET name=?, telefone=?, WHERE id=?'
        self.cursor.execute(query, (name, tel, id))
        self.comunication.commit() 
    
    def delete(self, id):
        query = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(query, (id,))
        
    def listing(self):
        self.cursor.execute('SELECT * FROM agenda') 
        for line in self.cursor.fetchall():
            print(line) 

    def close(self):
        self.cursor.close() 
        self.comunication.close() 


if __name__ == '__main__':
    agenda = AgendaBD(path)
    
