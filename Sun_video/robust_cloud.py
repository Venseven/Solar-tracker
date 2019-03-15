import sqlite3
class Db:
    def __init__(self,i):
        self.i=i
    def store(self):
        conn = sqlite3.connect('ROBUST.sqlite')
        cur = conn.cursor()
        cur.execute('INSERT INTO storage (name, value) values("a",{})'.format(self.i))
        conn.commit()
        conn.close()
    def show(self):
        print(self.i)
def retrieve():    
        conn = sqlite3.connect('ROBUST.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT * FROM storage WHERE name="a"')
        data_3 = cur.fetchall()
        conn.commit()
        conn.close()
        return data_3
    
