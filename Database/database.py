import queue
import sqlite3
from aem import Query
from flask import jsonify

class Database:
    def __init__(self,db_name):
        self.databasename = db_name
        with sqlite3.connect(self.databasename) as con:
                cur = con.cursor()
                querie = """CREATE TABLE IF NOT EXISTS URLS (
                            Short_Url	TEXT,
                            Long_Url	TEXT,
                            PRIMARY KEY(Short_Url));
                            """
                cur.execute(querie)

    def __connect_database(self):
        con = sqlite3.connect(self.databasename)
        con.row_factory = sqlite3.Row
        return con

    def is_exitst_long(self,url):
        cur = self.__connect_database().cursor()
        cur.execute("SELECT Short_Url FROM URLS WHERE Long_Url = ? ",
                            (url,))
        print(len(list(cur)))
        return cur.rowcount
    
    def is_exitst_short(self,url):
        cur = self.__connect_database().cursor()
        cur.execute("SELECT Long_Url FROM URLS WHERE Short_Url = ? ", 
                            (url,))
        print(len(list(cur)))
        return cur.rowcount
    
    def search(self,url, key):
        cur = self.__connect_database().cursor()
        if key == "Long":
            cur.execute("SELECT Short_Url FROM URLS WHERE Long_Url = ? ",
                            (url,))
        else:
            cur.execute("SELECT Long_Url FROM URLS WHERE Short_Url = ? ",
                            (url,))

        return cur.fetchall()


    def add_url(self, url_short, url_long):
        #try:
            with sqlite3.connect("ulr_databse.db") as con:
                cur = con.cursor()
                cur.execute(
                    "Insert Into URLS Values(?, ?)",
                    (url_short,url_long,)
                )
                #return jsonify({'Success': True, 'msg': 'Url is added to DB'})
        #except:
            #return jsonify({'Success': False, 'msg': 'Url is already at DB'})

    def show_urls(self,key):

        cur = self.__connect_database().cursor()
        if key == "Long":
            cur.execute("SELECT Long_Url From URLS")
        elif key == "Short":
            cur.execute("SELECT Short_Url From URLS")
        else:
            cur.execute("SELECT * From URLS")
        return cur.fetchall()
    
